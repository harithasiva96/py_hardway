class Song(): 
     # Passing two attributes to the function.  
    def __init__(self, lyrics):
        # storing the object as list in self.lyrics. Objects enter one after the other based on calling.
        self.lyrics = lyrics  
       
    def sing_me_a_song(self):
        for line in self.lyrics:
                print(line)
# Instances or objects 
happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()