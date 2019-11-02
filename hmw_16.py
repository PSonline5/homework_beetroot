# Implement a simple Audio Streaming Service class architecture
# It'll include 3 classes - Song, Album and Artist
#
# Artist class:
#   - name: str
#   - country: str
#   - songs: list = []
#   - albums: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - albums_number: int - must be declared using property decorator as the
#   length of albums list
#
# Album class:
#   - name: str
#   - year: int
#   - genre: str
#   - artist: Artist
#   - songs: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - duration: float - must be declared using property decorator. Album
#   duration is the sum of all songs' (from songs list) duration.
#
# Song class:
#   - name: str
#   - artist: Artist
#   - features: list[Author] = [] (can feature 1 or more Artists)
#   - year: int
#   - duration: float
#   - album: Album (can be None if it's a single)
#
#   when you specify an album, make sure add the song to album's [songs] list.
#   the same with Arist albums/songs lists
#
#   Also, you need implement a custom exception WrongArtistError which is
#   raised when you try to add a song to an album and artists don't match.


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.songs_list = []
        self.album_list = []

    @property
    def songs_number(self):
        return len(self.songs_list)

    @property
    def albums_number(self):
        return len(self.album_list)


class Album:
    def __init__(self, name, year, genre, artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        self.artist.album_list.append(self)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return sum([song.duration for song in self.songs])


class Song:
    def __init__(self, name, artist, features, year, duration, album=None):
        self.name = name
        self.artist = artist
        self.features = features
        self.year = year
        self.duration = duration
        self.album = album
        self.artist.songs_list.append(self)

        try:
            if self.artist == self.album.artist:
                self.album.songs.append(self)
            else:
                raise WrongArtistError("This is a wrong artist")
        except AttributeError:
            print("This should be a song")
        finally:
            print('All is done')
