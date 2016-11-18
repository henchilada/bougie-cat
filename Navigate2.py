
##create an object named car and give the car a few attributes, including position and speed
##the user is driving a car and navigating a city grid of 10 x 10
##position [0,0] indicates that the car is in the bottom left corner, with coordinates [x,y]
##initialize the position of the car at coordinates [0,0]
##initialize the time of the simulation to 13:00
##initialize the speed of the car at 1.0, representing 1 block per minute of time
##to start, the car will drive by itself until it hits a red or green light
"""
define the directions (north, south, east, and west)
north means the position of the car has the same x value and a y value that is 1 greater than the last position
south means the position of the car has the same x value and a y value that is 1 less than the last position
east means the position of the car has the same y value and an x value that is 1 greater than the last position
west means the position of the car has the same y value and a x value that is 1 less than the last position
if the car hits a green light, it will move in the same direction as it already was
if the car hits a red light, it will turn either left or right, based on a random function
the car can move exactly one block in 1 minute and will sit for 1 minute each time it hits a red light
if the car hits the edge of the map and attempts to turn off the map, it will instead turn back toward...
the inside of the grid and move 1 block
write a function that chooses a random coordinate anywhere in the range of [5,5] and [10,10]
assign this value to the variable 'destination'
each time the loop completes, print the time, the location of the car, the direction of the car, which...
direction the car just moved, and the distance to the destination.
calculate the distance from the car's current position and the destination point. Start by calculating...
this as the driving distance, finding the difference between the destination x and y points and current
location. As a more advanced step, you can calculate the distance as the crow flies, which will use the
pythagorean theorem to calculate the two sides of the triangle and the hypotenuse.
Bonus- calculate the time it will take to get to the destination, using the shortest path, and print this
estimate during each cycle.
Super bonus- change from a text game into something that draws the car on a grid and shows you where it is
Super super bonus- create a choice for the user at each interval where they can either go straight or turn...
but the lights are still random. 
"""

carOn = False
print("Welcome to the Gotham City Driving Adventure")
while carOn == False:
    ignition = input("Type START to begin the course:")
    if ignition != "START":
        print ("Hmm...It won't turn on. Let's try again.")
    else:
        carOn = True
print ("vroom vroom!", " Here we go!")

#some initialized attributes of the car. Make the car into a class later!
carCoordinates = [0,0]
lastCoordinates = [0,0]
currentTime = 1300
carSpeed = 1.0
gridSize = [10,10]
interval = 0
direction = "north"
import random

print ("The time is ", currentTime, ".","Your location is ",carCoordinates,".", "You are traveling ", direction, " on the street.")
#we will use streetlight = False to represent red and streetlight = True to represent green
streetLight = True
while streetLight == True:
    print("You reach the intersection.")
    interval += 1
    streetLight = random.choice([True, False])
    if streetLight == True:
        print ("The light is green!", " You drive through the intersection traveling", direction,".")
        lastCoordinates = carCoordinates
        carCoordinates [1] += 1
    else:
        print("The light is red. :(", "You'll have to wait a minute.")
        turnChoice = input("Would you like to turn 'left', 'right', or stay 'straight'?")
        if turnChoice = "straight"
            interval += 1
            print("Guess we'll have to wait here at the light for a minute...")
            
        
def IsNorth ():
    if carCoordinates [0] == lastCoordinates [0]
        if carCoordinates [1] - lastCoordinates [1] == 1
            return True
        return False
    return False





    
    





