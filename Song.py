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
import webbrowser
import spotipy
class Song:
    def __init__(self, title, artist, album, uri, album_cover, link, sampleUrl):
        self.title = title
        self.artist = artist
        self.album = album
        self.album_cover = album_cover
        self.uri = uri
        self.link = link
        self.sampleUri = sampleUrl

    def __repr__(self):
        return f'''{self.title} | {self.artist} | {self.album}
        ____________________________________________________________________________________________
                '''

    def callback(self):
        webbrowser.open_new_tab(self.getLink())

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def getGenre(self):
        return self.genre

    def getUri(self):
        return self.uri

    def getLink(self):
        return self.link

    def getSampleUrl(self):
        return self.sampleUri