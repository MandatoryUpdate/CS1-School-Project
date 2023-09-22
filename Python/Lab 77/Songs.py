class Songs:
    #Constructor
    def __init__(self, a, sT, d):
        self.artist = a
        self.songTitle = sT
        self.duration = d
    #Getters/Accessors
    def getArtist(self):
        return self.artist

    def getSongTitle(self):
        return self.songTitle

    def getDuration(self):
        return self.duration

    #Setters/Modifiers
    def setArtist(self, newArtist):
        self.artist = newArtist

    def setSongTitle(self, newSongTitle):
        self.songTitle = newSongTitle

    def setDuration(self, newDuration):
        self.duration = newDuration

    #String method to print
    def __str__(self):
        return "Artist is: "+self.artist+", song title is: "+self.songTitle+" and the duration is: "+str(self.duration)
