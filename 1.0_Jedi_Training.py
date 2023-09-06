'''
1.0 Jedi Training (17pts)  Name: Tommy Ngo


1. Define Forking (1pt): Forking is copying the files from the upstream remote repository to your remote repository.
It is making a copy of the files.

2. Define Cloning (1pt): Cloning is pulling the files from your remote repository to your local repository (computer)
to edit.

3. Define Branching (1pt): Branching is creating a separate strand to code on. This helps with testing code or
debugging code. You can merge the branches back into the master branch.

4. Define Committing (1pt): Committing is making a hard save of your code. You can go back to the commit like a
checkpoint.

5. Define Merging (1pt): Merging is combining either branches or forks back into the master branch/file.

6. Define Pushing (1pt): Pushing is placing/syncing the files from your local repository back to your remote
repository.

7. Define Pull Request (1pt): Someone can make a pull request to the file owner if they wish to merge their forked
files back into the master file in the upstream remote repository. The owner can choose to either accept or deny the
request.


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('purple')
tommy.color('black')

tina.shape('turtle')
tommy.shape('turtle')

def gas_flames():
  tina.begin_fill()
  tina.right(50)
  tina.forward(80)
  tina.left(100)
  tina.forward(80)
  tina.end_fill()
def gas_body(x,y):
  tina.goto(x,y)
  tina.pendown()
  gas_flames()
  gas_flames()
  gas_flames()
  gas_flames()
  gas_flames()
  gas_flames()
  gas_flames()
def eyes():
  tommy.begin_fill()
  tommy.pendown()
  tommy.right(40)
  tommy.forward(90)
  tommy.right(90)
  tommy.circle(-50, 180)
  tommy.end_fill()

tina.penup()
gas_body(-40,-80)
tina.begin_fill()
tina.left(5)
tina.forward(100)
tina.left(30)
tina.forward(100)
tina.left(50)
tina.forward(80)
tina.left(45)
tina.forward(70)
tina.left(3)
tina.forward(70)
tina.left(60)
tina.forward(55)
tina.left(5)
tina.forward(90)
tina.left(40)
tina.forward(30)
tina.left(20)
tina.forward(100)
tina.end_fill()
tina.penup()


tommy.begin_fill()
tommy.penup()
tommy.goto(0,-100)
tommy.pendown()
tommy.circle(110)
tommy.end_fill()
tommy.penup()
tommy.goto(-120, 80)
tommy.color('white')
eyes()
tommy.penup()
tommy.goto(10, 30)
tommy.left(20)
eyes()

tommy.penup()
tommy.goto(-80, 20)
tommy.color('black')
tommy.begin_fill()
tommy.pendown()
tommy.circle(5)
tommy.end_fill()
tommy.penup()
tommy.goto(30, 20)
tommy.begin_fill()
tommy.pendown()
tommy.circle(5)
tommy.end_fill()

tommy.penup()
tommy.goto(-60, -30)
tommy.color('pink')
tommy.left(152)
tommy.begin_fill()
tommy.pendown()
tommy.circle(65, 180)
tommy.end_fill()

tommy.penup()
tommy.left(90)
tommy.forward(20)
tommy.left(60)
tommy.color('white')
tommy.begin_fill()
tommy.pendown()
tommy.forward(40)
tommy.right(130)
tommy.forward(35)
tommy.end_fill()
tommy.penup()
tommy.left(65)
tommy.forward(20)
tommy.left(80)
tommy.begin_fill()
tommy.pendown()
tommy.forward(40)
tommy.right(130)
tommy.forward(45)
tommy.end_fill()
tommy.penup()
tommy.color('black'')

tommy.goto(-150, -150)
tommy.pendown()
tina.goto(-100, -150)


tommy.write('Tommy Ngo',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
