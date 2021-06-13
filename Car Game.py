command = ''
started = False
while command.lower() != "end":
    command = input('  >    ')
    if command.lower() == 'help':
        print('''                 Start - Start the car
                 Stop- Stop the car
                 End - Quit game''')
    elif command.lower() == 'start':
        if not started:
            print('Car Started, Ready to go...')
            started = True
        else:
            print('Car already Started, You little ass')
    elif command.lower() == 'stop':
        if started:
            print('Car stopped')
            started = False
        else:
            print('Car already stopped you bitch')
    else:
        print(" I'm nerd, cannot Understand")
print('Game end')
