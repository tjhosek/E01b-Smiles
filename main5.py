#!/usr/bin/env python3

import utils, open_color, arcade    # importing the libraries necessary to run the program

utils.check_version((3,7))

SCREEN_WIDTH = 800  #sets the width of the screen to 800 pixels
SCREEN_HEIGHT = 600 #sets the height of the screen to 600 pixels
SCREEN_TITLE = "Smiley Face Example"    #sets the title of the screen to be "Smiley Face Example"

class Faces(arcade.Window): #establishes a new class Faces, which requires a parameter of the type arcade.Window
    """ Our custom Window Class"""  # describing the class to be "Our Custom Window Class"

    def __init__(self): #runs the following code when an instance of the Faces class is initialized
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2   #sets the variable x of the Faces instance to the width of the screen /2
        self.y = SCREEN_HEIGHT / 2  #sets the variable y of the Faces instance to the height of the screen /2

        arcade.set_background_color(open_color.white)   #sets the background color of the screen to white

    def on_draw(self):  #runs the following code whenever the screen is drawn
        """ Draw the face """
        arcade.start_render()   #tells the program to start rendering images
        face_x,face_y = (self.x,self.y) #sets the x and y values of the face to the x and y values of the cursor
        smile_x,smile_y = (face_x + 0,face_y - 10)  #sets the x and y values of the smile to slightly below the center of the circle
        eye1_x,eye1_y = (face_x - 30,face_y + 20)   #sets the position of the left eye relative to the face
        eye2_x,eye2_y = (face_x + 30,face_y + 20)   #sets the position of the right eye relative to the face
        catch1_x,catch1_y = (face_x - 25,face_y + 25) #sets the position of the left light catch relative to the face
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #sets the position of the right light catch relative to the face

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #draws the yellow circle
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #draws the outline of the face
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)    #draws the left eye
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)    #draws the right eye
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)    #draws the left light catch
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)    #draws the right light catch
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)   #draws the smile


    def on_mouse_motion(self, x, y, dx, dy):    #when the mouse moves, execute the following code
        """ Handle Mouse Motion """
        self.x = x  #sets the x of the instance to the x of the mouse
        self.y = y  #sets the y of the instance to the y of the mouse



window = Faces()    #sets the window as an instance of the faces class
arcade.run()        #tells the code to start playing the game