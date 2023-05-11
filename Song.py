import webbrowser
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

                '''

    def callback(self):
        webbrowser.open_new_tab(self.link)

    def getUri(self):
        return self.uri