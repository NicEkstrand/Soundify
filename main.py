"""
    Project: Soundify is an add on to spotify where you can input a song that you like and you will be returned with
    a playlist of songs that are similar to the given song. It also includes side functions such as a search bar that
    spotify has so you don't have to switch between the two, and a text input to search for a song in the given playlist.
    Each song that is printed is linked to the song in spotif and when clicked, will play the song in spotify. When
    setting the queue, I print the sample links that I would have used to play the songs in Soundify. However, I did not
    have the time nor the resources to know how to play sounds or get mp3 files in python.

    @Author Nicolas Ekstrand
    @version 05/13/2022

"""
from Playlist import Playlist
from Song import Song
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
#Main app display variables
window = Tk()
window.title("Soundify")
window.geometry('1700x1000')
T = Text(window, height = 40, width = 200)
searchX = 10
searchY = 30
recommendedX = 700
recommendedY = 30
searchResults = Playlist([])
searchedLabels = []
recommendResults = Playlist([])
queueLabels = []

#Text entries and labels
recommend = Entry(window, width=10)
recommend.grid(column=5,row=0)

#The two functions that set the queue in specified order
def shuffle():
    recommendResults.setQueue("shuffle")
    printQueue(recommendResults.queue)

def inOrder():
    recommendResults.setQueue("in order")
    printQueue(recommendResults.queue)

#Converts spotipy search results into readable song data
def convertResults(data):
        return Song(data["name"], data['album']['artists'][0]['name'], data['album']['name'], data['uri'],
                             data['album']['images'][0]['url'], data['external_urls']['spotify'], data['preview_url'])

#Returns and prints a resulting list of songs with statistics that match input in the queue
def searchInQueue():
    results = []
    input = searchInQueueInput.get().lower()
    for i in range(len(recommendResults.songs)):
        if recommendResults.songs[i].getTitle().lower() == input:
            results.append(recommendResults.songs[i])

        elif recommendResults.songs[i].getAlbum().lower() == input:
            results.append(recommendResults.songs[i])

        elif recommendResults.songs[i].getArtist().lower() == input:
            results.append(recommendResults.songs[i])

    for i in range(len(results)):
        placeLabel(Label(window, text=results[i].__repr__(), cursor="hand2"), results[i].getUri(), 5, 600 + (i*50))

#Takes song and makes a playlist out of similar songs(includes button)
def recomendPlaylist():
    clearWindow(recommendResults.songs)
    #Gets the first song that the search comes up with
    results = sp.search(q=recommend.get())['tracks']['items'][0]
    givenSong = convertResults(results)

    #Sets results to lists bc the function parameters need lists
    listArtists = []
    listArtists.append(results['album']['artists'][0]['uri'])
    listSongs = []
    listSongs.append(givenSong.getUri())

    results = sp.recommendations(listArtists, sp.recommendation_genre_seeds(), listSongs)
    for track in results['tracks']:
        recommendResults.songs.append(convertResults(track))
    printText(recommendResults, recommendedX, recommendedY)

def clearWindow(list):
    #Resets the results playlist data
    for i in range(len(list)):
        list.pop()
    #Deletes the text on screen
    searchedLabels.clear()


#Places a label given x, y, and url to link the label to
def placeLabel(label, link, xVal, yVal):
    label.place(x=xVal, y=yVal)
    label.bind("<Button-1>", lambda e: callback(link))

#These two methods display the results of a search
def printText(list, x, y):
    for i in range(len(list.songs)):
        searchedLabels.append(Label(window, text=list.songs[i].__repr__(), cursor="hand2"))
        placeLabel(searchedLabels[i],  list.songs[i].getUri(), x, y + (i*50))

#Same purpose as function above but uses while loop because its a queue
#Prints sample urls in terminal bc window crashes when I try to link it to text
def printQueue(queue):
    i = 0
    while queue.qsize() != 0:
        i = i+1
        currentSong = queue.get()
        print(str(i+1) + ") " + str(currentSong.getSampleUrl()))
        currentLabel = Label(window,text=currentSong.__repr__(),cursor="hand2")
        placeLabel(currentLabel, currentSong.getUri(), recommendedX, recommendedY + (i*50))

    print("____________________________________________")

#Imports a link into text
def callback(url):
   webbrowser.open_new_tab(url)

#Returns a list of songs when search bar is used
def search(input):
    songs = []
    results = sp.search(q=input.get())
    #Sets the playlist data to search results
    for idx, track in enumerate(results['tracks']['items']):
        songs.append(convertResults(track))

#Buttons
playShuffled = Button(window, text="Play Shuffled", command=shuffle)
playShuffled.grid(column=6, row=0)

playInOrder = Button(window, text="Play in order", command=inOrder)
playInOrder.grid(column=7,row=0)

getRecommendedPlaylist = Button(window, text="get recommended playlist", command=recomendPlaylist)
getRecommendedPlaylist.grid(column=4, row=0)

window.mainloop()