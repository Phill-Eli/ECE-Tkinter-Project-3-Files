from tkinter import *
import time,random


class Missile:
    
       #### to complete
    def __init__ (self, canvas, c_height = 0, p_inc = 5, m_color = "orange", m_width = 8, m_height = 25):
        self.canvas = canvas
        self.c_height = c_height
        self.p_inc = p_inc
        self.m_color = m_color
        self.m_width = m_width
        self.m_height = m_height
        self.__active = False
            
    def activate(self, x, y):
        self.x = x
        self.y = y
        self.n_x = self.x + self.m_width
        self.n_y = 800 - self.m_height
        self.miss = self.canvas.create_rectangle(self.x, 800, self.n_x, self.n_y, fill = self.m_color)
        self.__active = True
            
            
    def deactivate(self):
        self.canvas.delete(self.miss)
        self.__active = False
        
    def is_active(self):
         return self.__active
        
    def next(self):
        self.m_height += self.p_inc
            
        if self.m_height >= self.c_height:
            self.deactivate()
            
        if self.is_active() == True:
            self.canvas.move(self.miss, 0, -self.p_inc)
            #self.miss.canvas.coords(self.miss, self.x, self.y + self.p_inc, self.x, self.n_y + self.p_inc)
    
        """for i in range(1000):
            n_y = self.y - self.p_inc
            self.activate(self.x, n_y)
            self.canvas.move(self, self.x, n_y)        
            i += 1
                
            if n_y <= self.c_height:
                self.deactivate()"""
        
    def add_missile(canvas, missiles, x, c_height = 0, p_inc = 5, m_color = "orange"):
        """for i in range(len(missiles)):
                
            if missiles[i].is_active() == False:
                 missiles.pop(missiles[i])

        n_missile = Missile(canvas, c_height, p_inc, m_color)
        n_missile.activate(x, c_height)
        missiles.append(n_missile)
        
        """
        for m in missiles:
            if m.is_active() == False:
                missiles.pop(missiles.index(m))
        n_missile = Missile(canvas, c_height, p_inc, m_color)
        n_missile.activate(x, c_height)

        missiles.append(n_missile)
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.m_height
        







###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock       
        while True:
           ##### To complete
            time.sleep(0.5)
            rand_x = random.randint(0, w)
            rand_cmax = random.randint(0, h)
            rand_pinc = random.randint(2,7)
            colors = ["blue", "yellow", "green", "purple", "red", "orange"]
            rand_clr = random.choice(colors)
            
            Missile.add_missile(canvas, missiles, rand_x, rand_cmax, rand_pinc, rand_clr )
            
            for m in missiles:
                m.next()

            




            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(),end=" ")
            print()
            
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

