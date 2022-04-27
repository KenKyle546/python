from collections import deque

song_title = deque()
song_artist = deque()

class Song:
    def __init__(self):
        self.title = ""
        self.artist = ""

    def prompt1(self):
        self.title = input("Enter the Title: ")
        song_title.append(self.title)
        
        self.artist = input("Enter the Artist: ")
        song_artist.append(self.artist)

    def prompt2(self):
        self.title = input("Enter the Title: ")
        song_title.appendleft(self.title)
        
        self.artist = input("Enter the Artist: ")
        song_artist.appendleft(self.artist)

    def display(self):
        print()
        print("Playing song:")                 
        print("{} by {}".format(song_title[0], song_artist[0]))
        
def main():
    s = Song()
    selection = "0"
    while selection != "4":
        print("""
Options:
1. Add a new song to the end of the playlist
2. Insert a new song to the beginning of the playlist
3. Play the next song
4. Quit""")
        selection = input("Enter Selection: ")

        if selection == "1":
            print()            
            s.prompt1()

        elif selection == "2":
            print()            
            s.prompt2()

        elif selection == "3":
            if song_artist:
                s.display()
                song_title.popleft()
                song_artist.popleft()
            else:
                print()
                print("The playlist is currently empty.")

        elif selection == "4":
            selection ="4"

        else:
            print("make a better selection!")
            selection = "0"
        
    print()
    print("Goodbye.")

if __name__ == "__main__":
    main()