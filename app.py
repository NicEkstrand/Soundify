from flask import *
from database import init_db, db_session
from models import *
from Playlist import Playlist
from song import Song
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
from tkinter import *

#Spotify data
cid = '294cd5ae40994904ba97d1a47b7c92b7'
secret = '93a9ea99b9f341da8b09b961e33ada94'
Oauth_token = 'BQD3GhMTvsm2iVlW4uq0vyxrYenWJJbwplKPmZblr5kYh5RA4MwLKOF3NLe4HmBaQofS1aEE7OcS8mnXhn21PRWuqzcrAqeoOivHYMlBeonNtBvTcbuI0xCc5xJXU7MscPXFRosL7Ylng04V8ig_6wJwjA'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def convertResults(data):
        return Song(data["name"], data['album']['artists'][0]['name'], data['album']['name'], data['uri'],
                             data['album']['images'][0]['url'], data['external_urls']['spotify'], data['preview_url'])

def recomendPlaylist(input):
    #Gets the first song that the search comes up with
    results = sp.search(input)['tracks']['items'][0]
    givenSong = convertResults(results)

    #Sets results to lists bc the function parameters need lists
    playlist = []
    listArtists = []
    listArtists.append(results['album']['artists'][0]['uri'])
    listSongs = []
    listSongs.append(givenSong.getUri())

    results = sp.recommendations(listArtists, sp.recommendation_genre_seeds(), listSongs)
    for track in results['tracks']:
        playlist.append(convertResults(track))

    return playlist

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes

@app.route("/")
def sign_in():
    return render_template("sign-in.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    #For Sign in
    username = request.form["sign-in-username"]
    password = request.form["sign-in-password"]
    #Matches inputs with users database
    target = db_session.query(User).where(User.username == username and User.password == password).first()
    if target != None:
        return render_template("home.html")
    else:
        return render_template("sign-in.html")
    
    #For Sign up
    username = request.form["sign-up-username"]
    password = request.form["sign-up-password"]
    person = User(username, password)
    db_session.add(person)
    db_session.commit()
    return render_template("home.html")
    
    

@app.route("/results", methods=["POST"])
def results():
    song_title = request.form["song-title"]
    songs = recomendPlaylist(song_title)
    return render_template("results.html", results = songs)
                        
@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")
    


@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)

