game = input('Greetings, Professor Falken.  Shall we play a game? (Y/N): ')
while game != 'Y':
    if game == 'Y':
        continue
    if game == 'y':
        game = 'Y'
    if game != 'Y':
        game = input('Well, I want to play a game.  I will not quit until you give me the repsonse I want! Enter "Y": ')        
print()
game_choice = input('How about a nice game of Mad Libs? (Y/N): ')
print()
if game_choice == 'Y':
    print('Great!  This is my favourite game. Much better than that pointless game of Global Thermonuclear War where the only move is not to play.')
elif game_choice == 'y':
    print('Great!  This is my favourite game. Much better than that pointless game of Global Thermonuclear War where the only move is not to play.')
else:
    print('Besides Mad Libs, the only other game that I know is Global Thermonuclear War. That was a strange game.  We all know the only winning move is not to play.\nInstead, your only choice is a nice game of Mad Libs')

print()

while True:

    print("Let's begin:")
    print()
    print('Please provide one word for the following:')
    print()
    adj = input('Adjective: ')
    animal = input('Animal: ')
    verb1 = input('Verb: ')
    excl = input('Exclamation: ')
    verb2 = input('Verb: ')
    verb3 = input('Verb: ')
    print()
    print('Your story is:')
    print()
    output = f'The other day, I was really in trouble. It all started when I saw a very\n{adj.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{excl.capitalize()}!" I yelled. But all\nI could think to do was to {verb2.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3.lower()} \nright in front of my family.' 

    print(output)
    print()
    again = input('Want to play again? Enter 1 for YES or 2 for NO: ')
    print()
    print()
    if again == "2":
        break

print() 
print('Thanks for playing!')
print()
print('Jashua has gone to sleep...')
print()


