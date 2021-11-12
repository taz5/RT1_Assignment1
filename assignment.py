from __future__ import print_function

import time
from sr.robot import *

"""
	Assignment 1

	The robot is the same as the one given in the exercises to practice. 
	The only difference is that now the sensors can detect boxes around all directions.
	
	Tasks with respect to the robot's behaviour:
	
	1. Constantly drive the robot around the circuit in the counter-clockwise direction
	2. Avoid touching the golden boxes.
	3. when the robot is close to a silver box, it should grab it, and move it behind itself

"""

# float: Threshold for the control of the orientation
a_th = 2.0

# float: Threshold for the control of the linear distance
d_th = 0.4

# Boolean: It is a variable for letting the robot know if it has to look for a silver or a golden marker
silver = True

# Robot class
R = Robot()

gold_th = 1.1
silver_th = 1


# Forward Motion of the robot
def drive(speed, seconds):

	'''
	Function for setting a linear velocity

	Args: speed (int): the speed of the wheels
	      seconds (int): the time interval
	'''

	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0

# Rotation of the robot
def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

# Finding the Silver Token
def find_silver_token():
    """
    Function to find the closest silver token
    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist=2
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and -70<token.rot_y<70:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==2:
	return -1, -1
    else:
   	return dist, rot_y

# Finding the Golden Token 
def find_golden_token():
    """
    Function to find the closest golden token
    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -40<token.rot_y<40:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

# Finding the Golden Token 
def find_golden_token_left():
    """
    Function to find the closest golden token
    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -105<token.rot_y<-75:
            dist=token.dist
    if dist==100:
	return -1, -1
    else:
   	return dist

# Finding the Golden Token 
def find_golden_token_right():
    """
    Function to find the closest golden token
    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and 75<token.rot_y<105:
            dist=token.dist
    if dist==100:
	return -1, -1
    else:
   	return dist

# Creating a grab function for the robot to grab and release the silver token behind it
def grab_silver_token():
    # if we grab the token, we move the robot forward and on the right, we release the token, 
    # and we go back to the initial position
    if R.grab(): 
        print("Gotcha!")
	turn(20, 3)
	drive(20,1)
	R.release()
	drive(-20,2)
	turn(-20,3)
"""
# Creating a scanning function in order to avoid hitting a golden token
def obstacle():
    if dist_for_gold_token < d_th:
"""
	   
# This section of the code will perform all the necessary tasks by utilising the functions previously defined
while 1:
    
    dist_silver, rot_silver = find_silver_token()
    dist_gold, rot_gold = find_golden_token()
    left_dist = find_golden_token_left()
    right_dist = find_golden_token_right()


    if(dist_gold>gold_th and dist_silver>silver_th) or (dist_gold>gold_th and dist_silver):
	drive(130,0.1)
   
    ########### Silver Token Related ################ 
    # if no token is detected, we make the robot turn
    if dist_silver<silver_th and dist_silver!=-1:  
	print("Silver is very close")
	if dist_silver < d_th:
		print("Found it!!!")
    		grab_silver_token()
      
    elif -a_th<= rot_silver <= a_th: # if the robot is well aligned with the token, we go forward
        drive(40, 0.1)
	print("Ah, that'll do.")
    	
    elif rot_silver < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        print("Left a bit...")
        turn(-10, 0.1)

    elif rot_silver > a_th:
        print("Right a bit...")
        turn(+10, 0.1)

    ########### Gold Token Related ##################
    if dist_gold < gold_th and dist_gold!=-1:
	
	print("Wait a minute.... Where is the wall?")

	if left_dist>right_dist:
		turn(-35,0.1)
		print("Wall on the right"+ str(right_dist)+ ", the distance on the left is: "+str(left_dist))
	elif right_dist>left_dist:
		turn(35,0.1)
		print("Wall on the left"+ str(left_dist)+ ", the distance on the right is: "+str(right_dist))
	else:
		print("Distances are equal")
