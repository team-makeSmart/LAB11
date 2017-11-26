# TEAM MAKESMART
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# LAB11
# 11-24-17

# CAVE ESCAPE Game Description:
# An explorer has fallen down a hole in the ground and into a cave.  He/She cannot climb back out.
# Many people have died in the cave.  The explorer must explore the cave to find objects to climb back out
# Steps to win:
# 1) Find the MATCHES and TORCH items
# 2) Use MATCHES and TORCH in the darkRoom to find the LATTER
# 3) Use the LATTER as a bridge to get to the lakeRoom
# 4) Find the ROPE in the lakeRoom
# 5) Use the ROPE in the startRoom to climb out of the cave and win the game
#
# MAP OF CAVE
#  [startRoom]    -  [darkRoom]  -  [islandRoom]
#      |                 |    
#  [skeletonRoom] -  [batRoom] 

#TODO change the above program description... the winning conditions and items are not needed for lab 11, but will be needed for lab 12

def map(): #Serves as the additional feature required per classroom instruction
  """This function prints map of the cave"""
  printNow('************************')
  printNow('MAP OF CAVE:')
  printNow("[startRoom]    -  [darkRoom]  -  [islandRoom]")
  printNow("     |                 |")    
  printNow("[skeletonRoom] -  [batRoom]") 
  printNow('************************')

def getHelp(): #TODO help message may need fixed according to classroom insturction
  printNow("What to do to win the game") 
  printNow("and what are the commands to navigate")
  return 

def welcomeMessage(): #TODO carefully read instructions from class, do we need to display welcomeMessage every time user enters HELP?
  return '\t\t*** Welcome to 205 Adventure Land! ***\n ' \
  'In each room you will be told which directions you can go\n You\'ll be' \
  ' able to go north, south, east or west by typing that direction\n' \
  ' Type help to redisplay this introduction exit to quit at any time\n' \
  'Please enter direction to start: '

def printDetails(description):
  printNow('************************')
  printNow(description)
  printNow('************************')

def getCommand(roomSpecificCommands):
  """ Gets a command from the user, ensure it is an acceptable command for the program and returns command"""
  """If the command is not a valid entry, displays error message and requests user to enter a valid command"""
  acceptableCommands = ['EXIT','HELP','MAP'] + roomSpecificCommands
  allAcceptableCommandsInOneString = "COMMANDS: " 
  for i in range(0,len(acceptableCommands)): #This for loops puts all the acceptable commands into a single string
    allAcceptableCommandsInOneString += acceptableCommands[i] + " " #TODO Yes these variables could be renamed to be shorter
  while true:
  #TODO find a good exception handling technique if user presses cancel or other buttons on the requestString() pop-up box.  Otherwise the program crash.
    command = requestString(allAcceptableCommandsInOneString + '\nEnter Command:')  #TODO Fix needs that acceptable commands must be stated in requestString()  Need to add acceptableCommands to the prompt
    command = command.upper()    
    if command not in acceptableCommands:
      printNow('************************')
      printNow("ERROR! Not a valid entry!")
      printNow("Acceptable Commands for this room are")
      printNow(acceptableCommands)     
      printNow('************************')
    else:
      return command    

def startRoom(): #TODO make these text line length less than 80 characters long for better viewability of code
  description = 'START ROOM!\nThis area is big and expansive.\nYou can see light coming from where you fell.\nIf only you could climb up!'
  printDetails(description)
  userCommand = getCommand(['RIGHT','DOWN'])
  return userCommand

def darkRoom(): #TODO make these text line length less than 80 characters long for better viewability of code
  description = 'DARK ROOM!\nThe room is dark and you cannot see much\nIt smells damp and you can hear critters in the nearby water.\nIf only you had more light!'
  printDetails(description)
  userCommand = getCommand(['RIGHT','DOWN','LEFT'])
  return userCommand

def skeletonRoom():#TODO make these text line length less than 80 characters long for better viewability of code
  description = 'SKELETON ROOM!\nStalagmites fill this cavern.\nYou see skeletons of past victims that fell down the well.\nPoor souls!'
  printDetails(description)
  userCommand = getCommand(['UP','RIGHT'])
  return userCommand
  
def batRoom():#TODO make these text line length less than 80 characters long for better viewability of code
  description = 'BATROOM!\n The walls of the cavern are filled with thousands of hanging bats\n It smells of bat guano... Yuck.\nIf you are bitten, you may get rabbies!'
  printDetails(description)
  userCommand = getCommand(['LEFT','UP'])
  return userCommand  
  
def islandRoom():#TODO make these text line length less than 80 characters long for better viewability of code
  description = 'ISLAND ROOM!\nThe room is surrounded by a large lake that looks pristine\nThe water is blue and it refracts light on the cavern walls.\nThe water is very cold!'
  printDetails(description)
  userCommand = getCommand(['LEFT'])
  return userCommand           

def main():
  x = 0  #represents an x cartestian coordinate
  y = 0  #represents a y cartestian coordinate
  
  #Get input from user by calling the room functions.  Input will be specific to each room
  while true:
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
    
    #Process off of what user input or userCommand is
    if userCommand == 'HELP':
      getHelp()
    elif userCommand == 'EXIT':
      printNow("Even though you are a quiter, thank you for playing!")
      return #effectively exit the program
    elif userCommand == 'MAP':
      map()                               
    elif userCommand == 'UP':
      y += 1 
    elif userCommand == 'DOWN':
      y -= 1           
    elif userCommand == 'RIGHT':
      x += 1
    elif userCommand == 'LEFT':
      x -= 1 

