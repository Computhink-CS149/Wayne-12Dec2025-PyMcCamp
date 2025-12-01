# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def teleport ():
    agent.teleport_to_player()
def move_forward (steps):
    agent.move(FORWARD, steps)
def move_back (steps):
    agent.move(BACK,steps)
def move_up (height):
    agent.move(UP, height)
def turn_right ():
    agent.turn(TurnDirection.LEFT)
def turn_left ():
    agent.turn(LEFT)
def move_down (height):
    agent.move(DOWN, height)
def obby1 ():
   agent.move(FORWARD, 4) 
   agent.move(LEFT, 4)
   agent.move(FORWARD, 3)
   agent.move(UP, 1)
   agent.move(FORWARD, 1)
   agent.move(UP, 1)
   agent.move(FORWARD, 1)
   agent.move(UP, 1)
   agent.move(FORWARD, 1)
   agent.move(FORWARD, 1)
   agent.move(FORWARD, 1)
   agent.move(DOWN, 1)
   agent.move(FORWARD, 1)
   agent.move(DOWN, 1)
   agent.move(FORWARD, 1)
   agent.move(DOWN, 1)



player.on_chat("come", teleport)
player.on_chat("mf", move_forward)
player.on_chat("tr", turn_right)
player.on_chat("mu", move_up)
player.on_chat("mb", move_back)
player.on_chat("tl", turn_left)
player.on_chat("md", move_down)
player.on_chat("obby",obby1)