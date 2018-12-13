from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

#---------------------------------------------------------------------------------------
# Canvas Size : 240 x 60 ,Font Size = 60 x 60, Default Color = #000000
imageSize = (240, 60)
fontSize = (60, 60)
defaultColor = (0, 0, 0)

#---------------------------------------------------------------------------------------
# Random char, rotate, background color, font color, posation
def rndChar():
    return chr(random.randint(65, 90))

def rndRotate():
    return random.randint(-90, 90)

def rndBgColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndFontColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def rndPosation(i):
    return (60 * i + random.randint(0,20), random.randint(0,20))

#---------------------------------------------------------------------------------------
# clear
def fillImg(width, height, img):
    for x in range(width):
        for y in range(height):
            img.point((x, y), fill=rndBgColor())


#---------------------------------------------------------------------------------------
def addNewChar(image):
    # Init
    char = Image.new('RGB', fontSize, defaultColor)
    drawChar = ImageDraw.Draw(char)

    # Random
    rChar =  rndChar()
    rotate = rndRotate()
    posation = rndPosation(i)

    # Draw and rotate
    drawChar.text((10, 10), rChar,  fill = rndFontColor(), font = font)
    char = char.rotate(rotate)

    # Split
    r, g ,b = char.split()
    # print(r,g,b)
    # Paste
    image.paste(char, posation, r)
    image.paste(char, posation, g)
    image.paste(char, posation, b)

#---------------------------------------------------------------------------------------
# New Image
image = Image.new('RGB', imageSize, defaultColor)
font = ImageFont.truetype('arial.ttf', 36)
drawImage = ImageDraw.Draw(image)
fillImg(imageSize[0], imageSize[1], drawImage)

#---------------------------------------------------------------------------------------
# Blur background
image = image.filter(ImageFilter.BLUR)

# Add Char
for i in range(4):
    addNewChar(image)

# Blur all
# image = image.filter(ImageFilter.BLUR)

#---------------------------------------------------------------------------------------
# Save
image.save('code3.jpg', 'jpeg')