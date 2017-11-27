# TEAM MAKESMART
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# LAB11
# 11-24-17

# CAVE ESCAPE Game Description:
# An explorer has fallen down a hole in the ground and into a cave. In order to navigate through the cave,
# s/he has to use specific commands that lead to specific directions inside the cave. If the user is lost
# or confused, there is a map or a help description available.
# MAP OF CAVE
#  [startRoom]    -  [darkRoom]  -  [islandRoom]
#      |                 |
#  [skeletonRoom] -  [batRoom]


# map() Serves as the additional feature required per classroom instruction
# It has a special output in the Dark Room
def map():  
    """ Prints map of the cave """
    """ Map can only be read in rooms with sufficient lighting """
    printNow('************************')
    printNow('MAP OF CAVE:')
    printNow("[startRoom]    -  [darkRoom]  -  [islandRoom]")
    printNow("     |                                  |")
    printNow("[skeletonRoom] -  [batRoom]")
    printNow('************************')


def getHelp():
    """ Prints help instructions to the user, if the user enters the 'HELP' command """
    printNow (welcomeMessage())


def welcomeMessage():
    """ displays a wellcome message that displays the rules of the game """
    return '*** WELLCOME TO THE CAVE ESCAPE GAME! ***\n' \
           '-- In each room you will be told which directions you can go\n-- You\'ll be' \
           'able to go UP, DOWN, LEFT or RIGHT by typing that direction\n' \
           '-- Type HELP to redisplay this introduction --\n' \
           '-- Type MAP for a cave map\n' \
           '-- Type EXIT to quit at any time\n'


def printDetails(description):
    """ prints the details of each room """

    printNow('************************')
    printNow ('YOU ARE CURRENTLY in :')
    printNow(description)
    printNow('************************')


def getCommand(roomSpecificCommands):
    """ Gets a command from the user, ensure it is an acceptable command for the program and returns command
        If the command is not a valid entry, displays error message and requests user to enter a valid command
        :param roomSpecificCommands (list) the specific commands for the given room
        :return command (string) the command typed by the user
    """

    acceptableCommands = ['EXIT', 'HELP', 'MAP'] + roomSpecificCommands
    allValidCommands = "COMMANDS: "

    for i in range(0, len(acceptableCommands)):  # This for loops puts all the acceptable commands into a single string
        allValidCommands += acceptableCommands[i] + ' '

    while True:

        command = requestString(
            allValidCommands + '\nEnter Command:')
        command = command.upper()

        if command not in acceptableCommands:
            printNow('************************')
            printNow("ERROR! Not a valid entry!")
            printNow("Acceptable Commands for this room are")
            printNow(acceptableCommands)
            printNow('************************')
        else:
            return command


def startRoom():
    """ the first room
         :return userCommand (string) the command typed by the user
    """
    description = 'START ROOM!\nThis area is big and expansive.\n' \
                  'You can see light coming from where you fell.\nIf only you could climb up!'
    printDetails(description)
    userCommand = getCommand(['RIGHT', 'DOWN'])
    return userCommand


def darkRoom():
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'DARK ROOM!\nThe room is dark and you cannot see much\n' \
                  'It smells damp and you can hear critters in the nearby water.\n' \
                  'If only you had more light!'
    printDetails(description)
    userCommand = getCommand(['RIGHT', 'DOWN', 'LEFT'])
    return userCommand


def skeletonRoom():
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'SKELETON ROOM!\nStalagmites fill this cavern.\n' \
                  'You see skeletons of past victims that fell down the well.\nPoor souls!'
    printDetails(description)
    userCommand = getCommand(['UP', 'RIGHT'])
    return userCommand


def batRoom():
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'BATROOM!\n The walls of the cavern are filled with thousands of hanging bats\n ' \
                  'It smells of bat guano... Yuck.\nIf you are bitten, you may get rabbies!'
    printDetails(description)
    userCommand = getCommand(['LEFT', 'UP'])
    return userCommand


def islandRoom():
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'ISLAND ROOM!\nThe room is surrounded by a large lake that looks pristine\n' \
                  'The water is blue and it refracts light on the cavern walls.\nThe water is very cold!'
    printDetails(description)
    userCommand = getCommand(['LEFT'])
    return userCommand


def main():
    """main function, starts the game """

    printNow (welcomeMessage())
    x = 0  # represents an x cartestian coordinate
    y = 0  # represents a y cartestian coordinate

    # Get input from user by calling the room functions.  Input will be specific to each room
    while True:

        if x == 0 and y == 0:
            userCommand = startRoom()
        elif x == 0 and y == -1:
            userCommand = skeletonRoom()
        elif x == 1 and y == 0:
            userCommand = darkRoom()
        elif x == 2 and y == 0:
            userCommand = islandRoom()
        elif x == 1 and y == -1:
            userCommand = batRoom()

        # Process off of what user input or userCommand is
        if userCommand == 'HELP':
            getHelp()

        elif userCommand == 'EXIT':
            print("Even though you are a quiter, thank you for playing!")
            return  # effectively exit the program
        elif userCommand == 'MAP':
            if x == 1 and y == 0:
                printNow('************************')
                printNow('You squint and try, but you cannot read your map in the Dark Room!')
                printNow('************************')
            else:
                map() #Display the map to the console
        elif userCommand == 'UP':
            y += 1
        elif userCommand == 'DOWN':
            y -= 1
        elif userCommand == 'RIGHT':
            x += 1
        elif userCommand == 'LEFT':
            x -= 1

#executes the main function on load
main()
