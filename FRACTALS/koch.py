from turtle import *
  
#function to create koch vonkoch curve
def vonkoch(lengthSide, levels): 
    if levels == 0: 
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    vonkoch(lengthSide, levels-1) 
    left(60) 
    vonkoch(lengthSide, levels-1) 
    right(120) 
    vonkoch(lengthSide, levels-1) 
    left(60) 
    vonkoch(lengthSide, levels-1) 
  
# main function 
if __name__ == "__main__": 
  
    # defining the speed of the turtle 
    speed(0)                    
    length = 300.0              
  
    # Pull the pen up – no drawing when moving. 
    penup()                      
      
    # Move the turtle backward by distance,  
    # opposite to the direction the turtle  
    # is headed. 
    # Do not change the turtle’s heading. 
    backward(length/2.0)         
  
    # Pull the pen down – drawing when moving. 
    pendown()          
  
    vonkoch(length, 3)
  