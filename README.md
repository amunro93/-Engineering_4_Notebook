# -Engineering_4_Notebook
Engineering work junior/4 year

## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic_Solver](#Python_Quadratic_Solver)
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

** Don't forget to **COMMENT YOUR CODE** before you upload to Github!

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


### Evidence 
![Capture](https://user-images.githubusercontent.com/57007400/136056939-ba1a5599-f3b7-4911-8577-1bab9c9897ea.PNG)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))



def doMath(a,b,c): 
    if c == 1:  
        
        return str (a + b)
        
    if c == 2:
        
        return str (a - b)
    
    if c == 3: 
        
        return str (a * b)
    
    if c == 4: 
        
        return str (a / b)
        
    if c == 5:
        
        return str (a % b)
        
        
        
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))


### Wiring
N/A

### Reflection


## Python_Quadratic_Solver

### Assignment Description 

### Evidence 

### Wiring

### Reflection 




