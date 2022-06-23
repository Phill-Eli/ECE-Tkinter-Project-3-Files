from tkinter import *

class SpaceShip:
    def __init__(self, canvas):
        self.canvas = canvas
        self._active = False
    
    def activate(self, x, y):
        self.x = x
        self.y = y
        self.spaceship = self.canvas.create_rectangle(self.x, self.y, self.x + 25, self.y + 25, fill = "black")
        self.spaceship = self.canvas.create_image(self.x, self.y,anchor=CENTER,image=PhotoImage(file="ship.png")) 
        self._active = True
    
    def shift_left(self):
        self.canvas.move(self.spaceship, 15, 0)
    
    def shift_right(self):
        self.canvas.move(self.spaceship, -15, 0)
 

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate((w/2), (h-17))
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

