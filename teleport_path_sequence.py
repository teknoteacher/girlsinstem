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
    
# Set x,y and z variables to represent co-ordinates
x = 12.6
y = 2.0
z = 16.5

# Change the player's position
mc.player.setPos(x,y,z)
time.sleep(2) # Wait 2 sec

# Set x,y and z variables to represent co-ordinates
x = 10.6
y = 2.0
z = 16.5

# Change the player's position
mc.player.setPos(x,y,z)
time.sleep(2) # Wait 2 sec

