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
blockType = 4 # 4 is Cobblestone, 39 Mushrooms, 45, Brick, 49 Obsidian
air = 0

# Create hollow building
mc.setBlocks(x,y,z, x + width, y + height, z + length, blockType)
mc.setBlocks(x + 1,y,z + 1, x + (width -1), y + (height-1), z + (length - 1), air)


