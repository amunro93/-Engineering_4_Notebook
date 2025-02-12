# -Engineering_4_Notebook
Engineering work junior/4 year

## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#Python_Dice_Roller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic_Solver](#Python_Quadratic_Solver)
* [Strings_and_Loops](#Python_Strings_and_Loops)
* [MSP](#MSP)
* [Swing_Arm](#Swing_Arm)
* [Skateboard](#Skateboard)
* [GPIO_Pin_Introduction](#Pin_Introduction)
* [RPI_Safe_Shutdown](#Safe_Shutdown)
* [GPIO Pins](#GPIO_Pins)
* [Headless Accelerometer](#Headless_Accelerometer)
* [Pi Camera](#Pi_Camera)
* [Copypasta](#Copypasta)
---

## Basics
Hello world was for us to warm backup to coding and PI.

### Assignment Description
For Hello World we were assigned to set up

### Evidence 

Pictures / Gifs of your work should go here.  You need to communicate what your thing does. For code only assignments like the Python calculator, include a screenshot of the output of the code.

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here.

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!


## Python_Dice_Roller

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!                                                                                                 

## Python_Calculator

### Assignment Description
For this assingment we were assinged to write a python calculator.py program that gives you the sum, diffrence, quotient, and the modulo of the two numbers. If done correctly the program will ask the user for two and then runs them through one function. 

### Evidence
![Capture](https://user-images.githubusercontent.com/57007400/136062077-4979838f-0d71-4b17-9260-23bafadee8fa.PNG)

### Code

    if c == 1:  #Defines Sum
        
        return str (a + b)
        
    if c == 2:  #Defines Difference
        
        return str (a - b)
    
    if c == 3:  #Defines Product
        
        return str (a * b)
    
    if c == 4:  #Defines Quotient 
        
        return str (a / b)
        
    if c == 5:  #Defines Modulo
        
        return str (a % b)
        
        

### Wiring
N/A

### Reflection
This code was quite simple but it will help me on the next assingment.

## Python_Quadratic_Solver

### Assignment Description 
In this module, we had to make a quadratic solver, meaning the user would give their a,b, & c values for standard form of a quadratic, and then the program would produce the roots, and if there were no roots, then the program would produce that there were no roots.

### Evidence 
![QudraticSolver](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/QudraticSolver.PNG)

### Reflection 
At first the code I had written would only multiply the three inputed numbers after trouble shooting it would do the quadratic however even if it was not a quadratic it would say that it was.


## Python_Strings_and_Loops


### Assingment Description 
For this assingment we were assinged to write a program that asks the user to type a simple sentence. 

### Evidence 
![PythonProgram03](https://user-images.githubusercontent.com/57007400/136064918-ae3677ba-aab5-41ba-a04c-31b650539eff.PNG)

### Reflection


## MSP

### Assingment Description 
This assingment was to make a game like stick man. You had to be able to have the code acknowledge when the person would guess the correct or wrong answer and have a stick man be created when you got it wrong. 
### Evidence
![MSP](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/MSP.PNG)

### Reflection 
I struggled with this assigment as my code did not draw the man corectly and it took me a long time to ajust the code to write it correctly I used google quite a bit. I also had trouble with the computer knowing if the letter typed was in the word however after a while I fixed it.


## Swing_Arm

### Assingment Description 
For this assingment we had to make a swing arm with a couple pictures and use variables. 

### Evidence 
![SwingArm](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/SwingArm.PNG)
![SwingArm2](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/SwingArm2.PNG)

### Reflection 
This was quite simple the only I stuggled with was the variables. I forgot to add them at the beginning so unfortunately I had to reset but other than that it was a breeze. 

## Skateboard 

### Assingment Description 
We were assingend to make a skateboard.
### Evidence 
![SkateboardFinal](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/SkateboardFinal.png)
![SkateboardBarrings](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/SkateboardBarrings.png)
![SkateboardDeck](https://raw.githubusercontent.com/amunro93/Engineering_4_Notebook/main/Images/SkateboardDeck.png)
### Reflection 
This assingment taught me to have patience while following directions in onshape. But the assinment wasn't very difficult it just took a little longer than I expected. I learned in this assingment how to 

## Pin_Introduction

### Assingment Description 
Using the pi GPIO (general purpose input/output) pins for this assignment. In this case, you will be using them as outputs, to drive LEDs. 

### Reflection 
This was a fairly easy assingment and will help me later in more difficult code. I didn't struggle with any of it. 
## Safe_Shutdown

### Assingment Description 
For this assingment we had to code a button when pressed would restart the pi and when held down for a longer period of time then five seconds it would shutdown the pi. 

### Reflection 
This assingment took a little longer then I expected. I got tripped up on making it restart for a while I could only shut it down but I got it to work. 

## GPIO_Pins

### Assingment Description 
For this assinment I had to wire up two sweet little devices (one input and one output) to our Pi using our trusty GPIO pins.
    
### Reflection 
This was defintly the hardest assingment yet this quarter for me. It took quite a while but with help from classmates I was able to complete it. 

## Headless_Accelerometer

### Assingment Description 
For this assinment I used a good bit of my knowledege from the last assingment and had to use a dot to show where the pi was leaning. 

### Reflection 
This assingment was quite easy I learned that the Accelerometer could read which way it was being tilted. 

## Pi_Camera 

### Assingment Description 
For this assingment I had to be able to capture a picture with a tiny little camera. 

## Copypasta

### Assingment Description
For this assingment I had to make my own stop motion animation video using a Raspberry Pi, Python and a camera module to take pictures, controlled by a push button connected to the Pi’s GPIO pins.
