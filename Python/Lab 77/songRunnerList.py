# Runner List Methods
from Songs import *

def createSongsList():
    artists = ["EimOut", "Ofpuns", "SoSoree"]
    songTitles = ["My Apologies", "I'll Do Better", "Until Next Time"]
    durations = [214, 175, 236]

    songs = []
    for i in range(3):
        songs.append(Songs(artists[i], songTitles[i], durations[i]))
    return songs

def printAllSongs(songs):
    for s in songs:
        print(s)

def addNewSong(songs):
    songs.append(Songs("FunTimes", "Let's Get Going", 195))

# Main program

songlist = []

songList = createSongsList()
printAllSongs(songList)
print()

addNewSong(songList)
printAllSongs(songList)
songList[1].setArtist("Stickmin")
songList[1].setSongTitle("Distraction")

print()
printAllSongs(songList)
