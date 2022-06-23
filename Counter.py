from tkinter import *
from turtle import left, right

class Counter:
    # to complete
    def __init__(self, canvas, i_val = 0):
        self.canvas = canvas
        self.i_val = i_val
        self.count = self.canvas.create_text(self.canvas.winfo_width() - 70, 20, text= str(self.i_val), fill="orange", font=('Courier 25 bold'))
#########################
    def increment(self, i_v):
            self.i_v = i_v

            if self.i_v < 0:
                self.i_val -= 1
                self.canvas.itemconfig(self.count, text = str(self.i_val))
            
            if self.i_v > 0:
                self.i_val += 1
                self.canvas.itemconfig(self.count, text = str(self.i_val))
                  

def main(): 
    
        ##### create a window, canvas 
    root = Tk() # instantiate a tkinter window
    my_image=PhotoImage(file="space2.png")

    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

    canvas.create_image(0,0,anchor=NW,image=my_image)
    canvas.pack()
    root.update() 

    count = Counter(canvas, 0)
    
    
    def left(event):
        count.increment(-1)
        
    def right(event):
        count.increment(1)
    
    root.bind("<Left>", left)
    root.bind("<Right>", right)
    
    
    
    root.update()   # update the graphic (redraw)
    root.mainloop()

if __name__=="__main__":

    main()



        
