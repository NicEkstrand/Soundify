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
    #Gets playlist
    results = sp.recommendations(listArtists, sp.recommendation_genre_seeds(), listSongs)
    for track in results['tracks']:
        playlist.append(convertResults(track))

    return playlist

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes

@app.route("/", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign-in.html")
    else:
        #For Sign in
        username = request.form["username"]
        password = request.form["password"]
        #Matches inputs with users database
        target = db_session.query(User).where(User.username == username and User.password == password).first()
        if target != None:
            return redirect(url_for("home"))
        else:
            return redirect(url_for("sign_in"))


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
    return render_template("home.html")
    
@app.route("/results", methods=["POST"])
def results():
    song_title = request.form["song-title"]
    songs = recomendPlaylist(song_title)
    return render_template("results.html", results = songs)
                        
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("sign-up.html")
    else:
        user = User(username = request.form["username"], password = request.form["password"])
        db_session.add(user)
        db_session.commit()
        return redirect(url_for("home"))

    

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

