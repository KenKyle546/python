name = input("Welcome Detective!  What is your last name? ")

print(f"""\n
Mrs. White: 
            "Thank you for coming so late Detective {name.capitalize()}.  We were having a dinner party with our friends this evening.  
             After dinner, our guests stayed for games.  Unfortunately at 9pm, my butler discovered Mr. Green dead on the 
             floor of the Library with a large gash on the back of his head. 
             All our guests are together in the lounge if you would like to question them.

Task:        Discover who killed Mr Green - do not let him/her get away!

What we know: 
            1. The staff have been ruled out as suspects
            2. All Suspects will be in the lounge waiting for questioning

What would you like to do first?
""")

choice1 = input("Type SUS to question the suspects or type LIB to visit the Library: ")

while not (choice1.lower() == "sus" or choice1.lower() == "lib"):
    choice1 = input("\nType SUS to question the suspects or type LIB to visit the Library: ")

# CHOICE 1: Go to the Lounge
if choice1.lower() == "sus":
    import subprocess as sp
    sp.call('cls', shell=True)
    print(f"""
    Welcome to the Lounge!

    When you enter the room, you find the remaining guests and question them.  You discover Col. Mustard 
    and Prof. Plum were playing pool in the billiard room at the time of the murder.  Miss. Scarlett
    and Mrs. Peacock were in the lounge playing the piano.  

    Everyone has an alibi!  What would you like to do now?
    """)

    choice11 = input("Type QUESTION to question everyone again and get more information or type OTHER to look for more clues: ")

    #Choice 11 =  Question Again
    if choice11.lower() == "question":
        import subprocess as sp
        sp.call('cls', shell=True)
        print(f"""
        You separate the suspects and interrogate them one at a time in separate rooms.  Unfortunately, 
        their stories are air tight.  There is no way that it can be one of them...

        What are you missing?... or rather, WHO are you missing?

        MRS. WHITE!!!!!!

        Why didn't you think to question her!  Let's find her!
        """)

        choice111 = input("Do you you want to check the HALL or DINING room?: ")

        if choice111.lower() == "hall":
            import subprocess as sp
            sp.call('cls', shell=True)
            result = True
        else:
            import subprocess as sp
            sp.call('cls', shell=True)
            result = False

    #Choice 11 == Think Again

    else:
        import subprocess as sp
        sp.call('cls', shell=True)
        print(f"""
        There must be something else you are missing.  Or rather.. SOMEONE else!

        MRS. WHITE!!!!!!

        Col Mustard said he saw her leave while you were questioning them.  He said 
        she went toward the Hall!
        """)

        choice112 = input("Do you trust Col Mustard and go to the HALL or is he trying to give her more time to escape? Would you rather go to the DINING room? ")

        if choice112.lower() == "hall":
            import subprocess as sp
            sp.call('cls', shell=True)
            result = True
        else:
            import subprocess as sp
            sp.call('cls', shell=True)
            result = False   

# CHOICE 2: Go to the Library
else:
    import subprocess as sp
    sp.call('cls', shell=True)
    print(f"""\n
    Welcome to the Library!

    You take a look around the crime scene and gather all the information you can.  Unfortunately there are no
    additional clues that can help you.  You decide to go to the Lounge.  On your way, you see the Study Door is open.
    You enter and find a bloody candlestick burried in the trash can.

    What do you want to do next?
    """)
    choice21 = input("Type LOUNGE to go question the suspects or type CANDLE to learn more about it: ")

    if choice21.lower() == "candle":
        import subprocess as sp
        sp.call('cls', shell=True)
        print(f"""
        Good idea Det. {name}.  You go find the Butler and question him about the candlestick.
        You find out that the candlestick is from Mrs. White's bedroom and she is the only one
        with a key to the study.  FIND HER!!
        """)

        choice211 = input("Where do you want to check? The closest rooms are the HALL and DINING room: ")

        if choice211.lower() == "hall":
            import subprocess as sp
            sp.call('cls', shell=True)
            result = True
        else:
            import subprocess as sp
            sp.call('cls', shell=True)
            result = False

    else:
        import subprocess as sp
        sp.call('cls', shell=True)
        print(f"""
        That was an odd choice, but ok!  You go to the Lounge and proceed to interrogate the suspects
        one at a time in separate rooms.  Unfortunately, their stories are air tight.  There is no way that it can be one of them...

        What are you missing?... or rather, WHO are you missing?

        MRS. WHITE!!!!!!

        Why didn't you think to question her!  Let's find her!
        """)

        choice221 = input("Do you you want to check the HALL or DINING room?: ")

        if choice221.lower() == "hall":
            import subprocess as sp
            sp.call('cls', shell=True)
            result = True
        else:
            import subprocess as sp
            sp.call('cls', shell=True)
            result = False

# Result = True etc.  
if result:
    print(f"\nThere she is!  Arrest her!  Great work Det. {name}!")
else:
    print(f"""\n
    She is not here!  You make a dash for the Hall...

    You enter the Hall and find an open window.  She is gone.
       
    Sorry Det. {name}, you took too much time.  She realized you 
    were on to her and she got away...  Better Luck next time.
    """)

end = input("\nPress ENTER to close the game: ")

