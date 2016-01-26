# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

# Set x,y, and z variables to player co-ordinates
x = pos.x + 5
y = pos.y
z = pos.z

# Set dimensions of building
width = 10
height = 5
length = 6

# Set blocktypes
blockType = 39 # 4 is cobblestone, 
air = 0

# Create building
mc.setBlocks(x,y,z, x + width, y + height, z + length, blockType)


