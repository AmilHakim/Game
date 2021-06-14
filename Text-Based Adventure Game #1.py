print('Would you like to play?')
answer = input()

if answer == 'yes':
    print('Type in your name: ')
    name = input()
    print('Welcome to a simple text-based adventure game ' + name + '.')
    print('You are getting chased by your pursuers for stealing their treasures. As you\'re running, the path ahead split into two')
    print('1. Go right')
    print('2. Go left')
    answer = input()
    if answer == '1':
        print('You encountered a group of pursuers in front of you. What do you do?')
        print('1. Fight them')
        print('2. Try to run past them')
        if answer == '1':
            print('As you try to fight them, the pursuers behind you managed to catch up to you. You were stabbed as you were fighting and died. Game Over')
        elif answer == '2':
            print('You tried to run past the group and succeeded.')
            print('You managed to outrun your pursuers and secured the treasures for yourself. THE END')   

    elif answer == '2':
        print('It turns out to be a dead end. Game Over.')
    else:
        print('Invalid Entry')
else:
    print('Goodbye!')