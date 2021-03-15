# Console-Drawing
A simple console version of a drawing scheme.

## Design
This program is written in python and been subdivided in four different scripts.

## main.py
This file is meant to take input from the user and cast the output via the console mode. 

The user can input one of the following commands.
  
  1. ` C w h ` creates a new canvas on console with width w and height h.
  2.  `L x1 y1 x2 y2` creates a new line from (x1, y1) to (x2, y2). Horizontal and vertical lines are drawn using the 'x' character.
  3.  `R x1 y1 x2 y2` creates a new rectangle, whose upper left corner is (x1, y1) and lower right corner is (x2, y2). Horizontal and vertical lines are drawn using the 'x' character.
  4.  `B x y c` fills the entire area connected to (x, y) with color 'c'.
  5.  `Q` quits the program.

## canvas.py

The Canvas.py file contains the Canvas class and all the functionalities have been implemeneted in this class which is responsible for the commands stated above.

## constant.py

All exceptions have been stated in this script and further used in the testing script.

## test_proxorassignment.py

Unit Testing is a type of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software code performs as expected.
For implememting the testing, python's unittest library has been used.

For testing, different number of test cases have been considered. Exceptions were raised using constant.py in accordance with different situations.

# Instructions to run the program

1.  Clone the repository locally.
    `git clone https://github.com/bansal-shubham/Console-Drawing.git`  
    `cd Console-Drawing`
2.  To run the program
    `python main.py`
3.  To run the unit test
    `python test_proxorassignment.py`
