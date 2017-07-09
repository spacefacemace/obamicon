from PIL import Image
import time

#variable declaration
colorOne = ""
colorTwo = ""
colorThree = ""
colorFour = ""

# for recoloring
#obamacon
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

#sunspot
persimmon = (252, 89, 53)
sunburn = (235, 54, 51)
seduction = (164, 41, 87)
veronica = (42, 40, 86)

#freeray
twinkle = (254, 201, 126)
nipple = (238, 180, 151)
sugarplum = (133, 121, 176)
dusk = (82, 84, 149)

#sickness
spit = (170, 201, 128)
plumbob = (142, 176, 37)
ghastly = (130, 93, 130)
ooze = (101,58,108)

#frozenyogurt
bruised = (187, 149, 183)
tongue = (252, 193, 174)
wunderbar = (242, 238, 174)
powderedsugar = (111, 198, 202)

#Prompt user input for image
time.sleep(2)
print("Hi! I'm Copper! I'm here to recolor your images!")
time.sleep(2)
print("Please enter your image name (with extension!)")
time.sleep(2)
print("for example: image.jpg")
imageURLRaw = input("> ")
time.sleep(2)
print("Cool! Now choose a color scheme!")
time.sleep(2)
print("We have several options! Pick your favorite:")
time.sleep(2)
print("OBAMA or SUNSPOT or FREEZERAY or SICKNESS or FROZENYOGURT")
"""
answer = input("> ")
while answer != "OBAMA" or answer != "SUNSPOT" or answer != "FREEZERAY" or answer != "SICKNESS" or != "FROZENYOGURT":
    print("Clever! Inspiring! But not one of the choices :(")
"""
answer = input("> ")
if (answer == "OBAMA"):
    colorOne = darkBlue
    colorTwo = red
    colorThree = lightBlue
    colorFour = yellow

elif (answer == "SUNSPOT"):
    colorFour = persimmon
    colorThree = sunburn
    colorTwo = seduction
    colorOne = veronica

elif (answer == "FREEZERAY"):
    colorFour = twinkle
    colorThree = nipple
    colorTwo = sugarplum
    colorOne = dusk

elif (answer == "SICKNESS"):
    colorFour = spit
    colorThree = plumbob
    colorTwo = ghastly
    colorOne = ooze

elif (answer == "FROZENYOGURT"):
    colorFour = bruised
    colorThree = tongue
    colorTwo = wunderbar
    colorOne = powderedsugar

print("Brilliant! Loading your image now!")
time.sleep(2)

# Load the image and turn the image into a list of tuples.
my_image = Image.open(imageURLRaw)
image_list = my_image.getdata()
image_list = list(image_list)

# Check the intensity of each pixel, determine how to recolor it, and save it in a new list.
recolored = []
for pixel in image_list:

    intensity = pixel[0] + pixel[1] + pixel[2]

    if intensity < 182:
         recolored.append(colorOne)

    elif intensity >= 182 and intensity < 364:
        recolored.append(colorTwo)

    elif intensity >= 364 and intensity < 546:
        recolored.append(colorThree)

    elif intensity >=546:
        recolored.append(colorFour)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
