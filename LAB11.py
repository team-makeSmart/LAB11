#TEAM MAKESMART 
#Maco Doussias, Pavlos Papadonikolakis, Jake McGhee 
#LAB11
#11-24-17

#Game Description:
#An explorer has fallen down an hole in the ground and into a cave.  He/She cannot climb back out.
#Many people have died in the cave.  The explorer must explore the cave to find objects to climb back out
#Steps to win:
# 1) Find the MATCHES and TORCH items
# 2) Use MATCHES and TORCH in the darkRoom to find the LATTER
# 3) Use the LATTER as a bridge to get the lakeRoom
# 4) Find the ROPE in the lakeRoom
# 5) use the ROPE in the startRoom to climb out of the cave and win the game


class Room():
 
  def __init__(self, roomName, description, items, contentsBool, up, down, left, right):
    """initializes variables with parameters when object is declared"""
    """TODO roomName may be superfluous to the program"""
    """TODO contentsBool may be superfluous to program... Intended make sure user knows if no items in room but can be done in other ways """
    """ Description: holds a description of the room. Items: holds items found in room"""
    """ up,down,left,right: holds info on adjacent room, False if there is no adjacent room in that direction"""
    self.roomName = roomName
    self.description = description
    self.items = items
    self.contentsBool = contentsBool
    self.up = up
    self.down = down
    self.left = left
    self.right = right

  def printDetails(self):
    printNow('************************')
    printNow(self.description)
    printNow('ITEMS IN ROOM:'+self.items) 
    printNow('************************')

class GameHero:
  '''This is the class of the hero that is playing the game'''
  inventory = [] #This array holds the inventory that the user collects
  userInput = "" #TODO not sure this variable should be here
  location = "startRoom" #initialized to startRoom because this is where game starts
  
def welcomeMsg():
  """ This is the welcome message that displays at the beginning and also whenever the user enters help"""
  """ Welcome message also displays a list of commands
  #TODO makes this function output a little more clear
  printNow('************************')
  printNow('CAVE ESCAPE.  You have fallen down a cave and you must get out.\nSearch the cave for items that will help you escape.')
  printNow('COMMANDS: ENTER UP, DOWN, LEFT, OR RIGHT TO MOVE.  \nENTER HELP TO SEE THIS MESSAGE.\n ENTER EXIT TO QUIT') 
  printNow('************************')
    
#TODO find where best ot put a menuOptions function to print menu options for user to input
#TODO Menu options should include EXIT, HELP, GET (To GET ITEMS FROM ROOM), USE (TO USE ITEMS IN ROOM)
#TODO Menu options should also include up, down, left, right to move from room to room.


#initialize all the rooms
#TODO These are intialized as global objects, fix to be local
#TODO Fix code so it is less than 80 characters across to be more readable code
startRoom = Room("startRoom",'This area is big and expansive.\nYou can see light coming from where you fell from\nIf only you could climb up!','NONE',false, false, "darkRoom", false, "skeletonRoom")
darkRoom = Room("darkRoom",'The room is dark and you cannot see anything','LATTER',true, false, "batRoom","startRoom", "islandRoom")
skeletonRoom = Room("skeletonRoom",'Stalagmites fill this cavern.  You see skeletons of past victims that fell down the well','MATCHES',true, "startRoom", false, false, "batRoom")
batRoom = Room("batRoom",'This walls of the cavern are filled with thousands of twitchy, hanging bats\nIt smells of bat guano and you worry if you are bitten, you may get rabbies','TORCH',true, "darkRoom", false, "skeletonRoom", false)
islandRoom = Room("islandRoom",'The room is surrounded by a lake, it looks pristine\n The water is almost blue','ROPE',true, false, false, "darkRoom", false)


  #TODO fix main.... Does not work.  
  #TODO Fix main so that use can move throughout the cavern
  #TODO Idea is that user input will be EXIT, HELP, USE, GET or a direction based on the available directions in the room  
def main():
  explorer = GameHero
  welcomeMsg()
  while(true):
    userInput = requestString('INPUT COMMAND')
    userInput = userInput.upper()    
    if(userInput == "HELP"):
      welcomeMsg()
    elif userInput == "EXIT":
      printNow('Even though you\'re a quiter, Thank you for playing!')
      break #ends loop and program execution
    elif userInput == "GET":
      printNow("Figure out how to get items from a room")
    elif userInput == "USE":
      printNow('You just used an item')  
    elif userInput == "UP":
      printNow("You just went up")
    elif userInput == "DOWN":
      printNow("You just went down")
    elif userInput == "RIGHT":
      printNow("You just went right")
    elif userInput == "LEFT":
      printNow("You just went left")
