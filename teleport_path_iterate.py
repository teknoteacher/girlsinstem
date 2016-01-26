# Connect to Minecraft
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x,y and z variables to represent co-ordinates
x = 14.6
y = 2.0
z = 16.5

# Change the player's position
mc.player.setPos(x,y,z)
time.sleep(2) # Wait 2 sec

# Iterate the player's x position
for a in range(10): # Repeat 10 times
    x = x - 3
    mc.player.setPos(x,y,z)
    time.sleep(0.25) # Wait 1/4 sec
    
