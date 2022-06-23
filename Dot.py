########################
## Team Members
## Name1:Phillipe Eligene         
## Name2:
#########################

from tkinter import *
import random


class Dot:
    ##### TO COMPLETE
    def __init__ (self, canvas, x_cord, y_cord, c_dot, is_displayed = False):
        self.canvas = canvas
        self.x = x_cord
        self.y = y_cord
        self.c = c_dot
        self.display = is_displayed
        
        if self.c == "rainbow":
            #making list of colors to randomize the color of each generated dot
            items = ["red", "green", "blue", "yellow", "white", "orange", "purple"]
            self.c = random.choice(items)
        
        if self.display == True:
            self.canvas.create_oval((self.x,self.y)*2, fill = self.c)










        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

