# TEAM MAKESMART
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# LAB11
# 11-24-17

# Game Description:
# An explorer has fallen down an hole in the ground and into a cave.  He/She cannot climb back out.
# Many people have died in the cave.  The explorer must explore the cave to find objects to climb back out
# Steps to win:
# 1) Find the MATCHES and TORCH items
# 2) Use MATCHES and TORCH in the darkRoom to find the LATTER
# 3) Use the LATTER as a bridge to get the lakeRoom
# 4) Find the ROPE in the lakeRoom
# 5) use the ROPE in the startRoom to climb out of the cave and win the game


class Room():
    navigate = ''

    # starting position with posible moves
    currentRoom = [['startRoom', 'darkRoom', 'islandRoom'],
                   ['skeletonRoom', 'batRoom']]

    roomsSize = len(currentRoom)
    row = 0
    col = 0

    def __init__(self, roomName=None, description=None, items=None):
        """initializes variables with parameters when object is declared"""
        
        self.roomName = roomName
        self.description = description
        self.items = items
        self.navigate = self.printDirections(roomName)

    def getItems(self):
        return self.items

    def printDetails(self):
        print ('************************')
        print(self.description)
        print('Items in room: ' + self.items)
        print self.navigate
        print('************************')

    def printDirections(self, roomName):
        if roomName == 'startRoom':
            self.navigate = 'You can go east or south'
        elif roomName == 'darkRoom':
            self.navigate = 'You can go east, south or west'
        elif roomName == 'batRoom':
            self.navigate = 'You can go north or west'
        elif roomName == 'skeletonRoom':
            self.navigate = 'You can go north or east'
        elif roomName == 'islandRoom':
            self.navigate = 'You can go only west, back to the dark room '
        return self.navigate

    def getHelp(self):
        return "What to do to win the game\n" \
               "and what are the commands to navigate"

    def wellcomeMessage(self):
        return '\t\t*** Welcome to 205 Adventure Land! ***\n ' \
               'In each room you will be told which directions you can go\n You\'ll be' \
               ' able to go north, south, east or west by typing that direction\n' \
               ' Type help to redisplay this introduction exit to quit at any time\n' \
               'Please enter direction to start: '

    def onBounds(self):
        """
        checks the bounds of the rooms
        :return:true if the user is inside the rooms
        """
        if self.col == 2 and self.row == 0:
            return 0 <= self.row < self.roomsSize and 0 <= self.col < len(self.currentRoom[0])
        else:
            return 0 <= self.row < self.roomsSize and 0 <= self.col < len(self.currentRoom[1])

    def goEast(self):

        self.col += 1
        if self.onBounds():
            return True
        else:
            self.col -= 1
        return False

    def goWest(self):

        self.col -= 1
        if self.onBounds():
            return True
        else:
            self.col += 1
        return False

    def goNorth(self):
        self.row -= 1
        if self.onBounds():
            return True
        else:
            self.row += 1
        return False

    def goSouth(self):
        self.row += 1
        if self.onBounds():
            return True
        else:
            self.row -= 1
        return False

    # --------------------------------
    def getCurrentRoom(self):
        if self.onBounds():
            return self.currentRoom[self.row][self.col]
        return False

    def whichRoom(self, roomName):
        if roomName == skeletonRoom.roomName:
            return skeletonRoom
        elif roomName == startRoom.roomName:
            return startRoom
        elif roomName == darkRoom.roomName:
            return darkRoom
        elif roomName == batRoom.roomName:
            return batRoom
        else:
            return islandRoom


startRoom = Room("startRoom", 'This area is big and expansive.\nYou can see light coming from where you fell from\n'
                              'If only you could climb up!', 'NONE')
darkRoom = Room("darkRoom", 'The room is dark and you cannot see anything', 'LATTER')
skeletonRoom = Room("skeletonRoom", 'Stalagmites fill this cavern.  You see skeletons of past victims that'
                                    ' fell down the well', 'MATCHES')
batRoom = Room("batRoom", 'This walls of the cavern are filled with thousands of twitchy, hanging bats\n'
                          'It smells of bat guano and you worry if you are bitten, you may get rabbies', 'TORCH')
islandRoom = Room("islandRoom",
                  'The room is surrounded by a lake, it looks pristine\n'
                  'The water is almost blue',
                  'ROPE')





currentPosition = startRoom

currentPosition.goEast()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goEast()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goSouth()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goWest()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goWest()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName
currentPosition.goWest()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goSouth()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName

currentPosition.goWest()
currentRoom = currentPosition.whichRoom(currentPosition.getCurrentRoom())
print currentRoom.roomName
