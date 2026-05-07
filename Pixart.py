"""
This module allows for the creation of a pixel art drawing using a turtle object.
The functions below implement basic drawing capabilities, where each pixel can be colored based on a character input.
Each function is developed incrementally as part of the project.

Functions:
1. get_color(character)
2. draw_color_pixel(color_string, t)
3. draw_pixel(color_character, t)
4. draw_line_from_string(color_string, t)
5. draw_shape_from_string(t)
"""

import turtle as t



"""get_color function alligns or allocates each number to the requested color as mentioned in activity 1 doc"""
def get_color(character):
    if character == "0":
        return "black"
    elif character == "1":
        return "white"
    elif character == "2":
        return "red"
    elif character == "3":
        return "yellow"
    elif character == "4":
        return "orange"
    elif character == "5":
        return "green"
    elif character == "6":
        return "yellowgreen"
    elif character == "7":
        return "sienna"
    elif character == "8":
        return "tan"
    elif character == "9":
        return "grey"
    elif character == "A":
        return "darkgrey"
    else:
        return None                          #This will return none if theres no valid input for example X also 




"""draw_color_pixel function sets the color of the turtle and draws the pixel of size 30 and moves the turtle to the next position""" 
def draw_color_pixel(color_string, t):
    t.pendown()
    t.fillcolor(color_string)                    #Set the turtle color
    t.pencolor("black")
    t.begin_fill()
    for i in range(4):                       #Draw a square (pixel)
        t.forward(30)                        #Each side of the pixel is 30 units
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(30)                            #Move turtle to the next position



"""draw_pixel function draws a single pixel based on the character given using get_color function to convert the character to a color and the draw_color_pixel function to draw the actual pixel"""
def draw_pixel(color_character, t):
    color_string = get_color(color_character)
    if color_string:
        draw_color_pixel(color_string, t)
    else:
        print(f"Invalid color code: {color_character}")



"""draw_line_from_string function draws a row of pixels using the input given by user and each character has a preassignemed color so if its invalid and not pre-assigneed it shows up an error"""
def draw_line_from_string(color_string, t):
    for character in color_string:
        if get_color(character) is None:         #Stop if an invalid color is found
            print(f"Invalid character: {character}")
            return False
        draw_pixel(character, t)
    return True



"""draw_shape_from_string function keeps asking the user to continue and if they want to stop they can do enter or if invalid inout then also stop and this function also helps move turle move to the next line to start the next row"""
def draw_shape_from_string(t):
    while True:
        color_string = input("Enter a string of color codes (or press Enter to stop): ")
        if not color_string:                     #Stop if the string is empty
            break
        if not draw_line_from_string(color_string, t):
            print("Drawing stopped due to invalid input.")
            break
        t.penup()                                #Move the turtle to the next line
        t.setpos(t.xcor() - len(color_string) * 30, t.ycor() - 30)
        t.pendown()



"""draw_shape_from_string_file(color_string) to take input from files without asking for user input and function accordingly"""
def draw_shape_from_string_file(color_string):
    s_input = color_string.split('\n')            #Splits at the occurrence of the \n character
    for i in s_input:
        if draw_line_from_string(i, t):           #Calls function if value returned is 'True'
            pass
        else:                                     #Prints error incase of invalid or wrong input
            print("Error")
            break
        t.penup()  
        t.setpos(t.xcor() - len(i) * 30, t.ycor() - 30)         #Repositions itself to be at the beginning of the next line
        t.pendown()


"""Function to draw 20x20 grid"""
def draw_grid(t):

    for i in range(10):
    #Range is set to 10 and not 20 because for one loop, 2 rows are being drawn or theres 2 iterations taking place
        
        color_string = "02020202020202020202"                 #Pattern for first row
        draw_line_from_string(color_string, t)                #Calling draw_line_from_string() function
        t.penup()  #move the turtle to the next line
        t.setpos(t.xcor() - len(color_string) * 30, t.ycor() - 30)
        t.pendown()
        color_string = "20202020202020202020"               #Pattern for second row
        draw_line_from_string(color_string, t)
        t.penup()  #move the turtle to the next line
        t.setpos(t.xcor() - len(color_string) * 30, t.ycor() - 30)
        t.pendown()
            

"""draw_shape_from_file(filee) to take user input and draw according to the inputs present in the file"""
def draw_shape_from_file(filee):
    try:                                                 #Error handling block
        with open (filee,"r") as curfile:                #Opening with with-as
            for i in curfile:
                v1 = i.strip()                           #Removing all leading and trailing whitespaces including newlines
                draw_shape_from_string_file(v1)          #Calling Functiong
                
    except FileNotFoundError:                            #except block to handle error incase file is not found
        print ("This file does not exist, please input a proper file")


"""This function is used to clear the screen after every drawing and reposition the turtle"""
def clear_screen():
    t.clearscreen()
    t.speed(0)
    t.penup()                               
    t.goto(-300,300)
    t.pendown()