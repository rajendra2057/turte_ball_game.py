import turtle
import math
import random
import winsound 

#set up screen
wn= turtle.Screen()
wn.bgcolor("lightgreen")



#Draw border:
mypen=turtle.Turtle()
mypen.up()
mypen.setposition(-300,-300)
# mypen.color("white")
mypen.pendown()
for sides in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


#Create player turtle
player= turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)


#create score:
score=0


#create goal
goal=turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.speed(0 )
goal.setposition(random.randint(-300,300),random.randint(-300,300))


#set speed variable:
speed=1


#define Funcitons:
def turnleft():
    player.left(45)
    
def turnright():
    player.right(45)
    
def increasespeed():
    global speed
    speed+=0.55
     
def iscollision(t1,t2 ):
    distance= math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<18:
        return True
    else:
        return False


#set keyboard bindings
turtle.listen()  # to wait for keyboard commands
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")   #right gives error
turtle.onkey(increasespeed,"Up")  # wants to increase speed on up arrow click
   #the onkey function listen the user to press the key and
   #calls the given function


while True:
    player.fd(speed)
    
    #Boundary Checking for turtle
    if player.xcor()>290 or player.xcor()<-290:
        player.right(180)
    if player.ycor()>290 or player.ycor()<-290:
        player.right(180)
        
        
    #collision checking:
    if iscollision(player,goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.right(random.randint(0,360))
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        score+=1
        
        #Draw score on the screen:
        mypen.undo()  # so that the new score do not overlap the previous score
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-290,305)
        scorestring="score: %s"%score
        mypen.write(scorestring, move=False, align='left', font=('Arial', 10, 'normal'))
        
      
    #move goal:
    goal.fd(1 )
    
    #boundary checking for goal:
    if goal.xcor()>290 or goal.xcor()<-290:
        goal.right(180)
    if goal.ycor()>290 or goal.ycor()<-290:
        goal.right(180)
    



wn.mainloop()
