#TEAM MAKESMART 
#Maco Doussias, Pavlos Papadonikolakis, Jake McGhee 
#LAB11
#11-24-17


class Room():
  def __init__(self, roomName, description, items, contentsBool, up, down, left, right):
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
  inventory = [] #This array holds the inventory that the user collects
  userInput = ""
  location = "startRoom" #initialized to startRoom because this is where game starts
  
 
    
  

#class Items 
#initialize all the rooms
startRoom = Room("startRoom",'This area is big and expansive.\nYou can see light coming from where you fell from\nIf only you could climb up!','NONE',false, false, "darkRoom", false, "skeletonRoom")
darkRoom = Room("darkRoom",'The room is dark and you cannot see anything','KEY',true, false, "batRoom","startRoom", "islandRoom")
skeletonRoom = Room("skeletonRoom",'Stalagmites fill this cavern.  You see skeletons of past victims that fell down the well','MATCHES',true, "startRoom", false, false, "batRoom")
batRoom = Room("batRoom",'This walls of the cavern are filled with thousands of twitchy, hanging bats\nIt smells of bat guano and you worry if you are bitten, you may get rabbies','TORCH',true, "darkRoom", false, "skeletonRoom", false)
islandRoom = Room("islandRoom",'The room is surrounded by a lake, it looks pristine\n The water is almost blue','ROPE',true, false, false, "darkRoom", false)

def main():  
  explorer = GameHero
  while(explorer.userInput != "EXIT"):
    if (explorer.location == "startRoom"):  
      startRoom.printDetails()
    elif (explorer.location == "darkRoom"):  
      startRoom.printDetails()
    elif (explorer.location == "skeletonRoom"):  
      startRoom.printDetails()
    elif (explorer.location == "batRoom"):  
      startRoom.printDetails()
    elif (explorer.location == "lakeRoom"):  
      startRoom.printDetails()
    explorer.location = "batRoom"
    requestString('no')
    





