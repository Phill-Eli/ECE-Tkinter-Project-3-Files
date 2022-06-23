from tkinter import *
import math,time,random
from Dot import Dot
#import matplotlib.pyplot as plt


class Explosion:

    #### to complete
    def __init__ (self, canvas, c_explosion, max_r = 80):
        #constructor
        self.canvas = canvas
        self.radius = max_r
        self.color = c_explosion
        self.dot_num = 15
        self.dot_list = []
        self.__active_set = False
        
    def activate(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
        self.r = 0
        self.__active_set = True
        
    def is_active(self):
        
        return self.__active_set
    
    def next(self):
        
        if self.__active_set == True:
            self.r += 1
            #Variable ang for angle is randomly selected based on 360 degrees of freedom
            ang = random.randint(0,359)
            
            for i in range(self.dot_num):
                #The generated angle is then converted into radians and plugged into sine and cosine functions
                #and multipled by the r variable in the active method, to find the coordinates of each generated dot
                x_val = self.r * math.cos((math.pi/180) * ang)
                y_val = self.r * math.sin((math.pi/180) * ang)
                
                z = Dot(self.canvas, x_val + self.x, y_val + self.y, self.color, True)
                self.dot_list.append(z)
            
            if self.r >= self.radius:
                self.deactivate()  
            
    def deactivate(self):
        
        for i in range(len(self.dot_list)):
            #As the for loop iterates, the individual dots in the dot_list are deleted
            self.canvas.delete(self.dot_list[i])
        
        self.__active_set = False
    
    def add_explosion(canvas, exp_d, x, y, max_s = 80, clr = "rainbow"):
        
        for i in range(len(exp_d)):
            #As the for loop goes through the explosion data, if the explostion at index i is determined to no longer be active
            #it is deleted to free up memory 
            if exp_d[i].is_active() == False:
                exp_d.pop(exp_d[i])
        
        exp = Explosion(canvas, clr, max_s)
        exp.activate(x,y)
        exp_d.append(exp)
    
    
        
        
            

        
        
        
        
        












        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

