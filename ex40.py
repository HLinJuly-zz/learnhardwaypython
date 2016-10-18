class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy = Song(["happy birthday to you",
              "i don't want to get sued"])

bulls = Song(["They rally around tha family", "hula"])

happy.sing_me_a_song()
bulls.sing_me_a_song()