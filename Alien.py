from tkinter import *
import math
import time, random

class Alien:
    ### to complete
    def __init__ (self, canvas, p_inc = 4, a_clr = "yellow", a_w = 50, a_h = 50, ip_val = 1):
        self.p_val = 0
        self.canvas = canvas
        self.p_inc = p_inc
        self.a_clr = a_clr
        self.a_w = a_w
        self.a_h = a_h
        self._active = False
        self.ip_val= ip_val
         
    def activate(self, x, y):
        self.x = x
        self.y = y
        
        self.x = random.randint(0, self.canvas.winfo_width())
        self.y = 0
        
        self.alien = self.canvas.create_rectangle(self.x, self.y, self.x + self.a_w, self.y + self.a_h, fill = self.a_clr)
        self._active = True
        
    def is_active(self):
        return self._active
    
    def deactivate(self):
        self.canvas.delete()
    
    def next(self):
            
        if self.a_h >= self.canvas.winfo_height():
            self.deactivate()
            
        if self.is_active() == True:
            self.a_h += self.p_inc
            self.canvas.move(self.alien, 0, self.p_inc)
            
    def add_alien(canvas, aliens):
        alien0=Alien(canvas)
        alien1=Alien_red(canvas)
        alien2=Alien_green(canvas)
        alien3=Alien_blue(canvas)
        
        for alien in aliens:
            if alien.is_active() == False:
                aliens.pop(aliens.index(alien))
        
        alien_list = [alien0, alien1, alien2, alien3]
        c_alien = random.choice(alien_list)
        time.sleep(0.5)
        c_alien.activate(1, 1)
        aliens.append(c_alien)
        
        
        
    def is_shot(self, x_h, y_h):
        self.x_h = x_h
        self.y_h = y_h
        val = False
        
        if (self.x == self.x_h) and (self.y == self.y_h):
            val = True
        
            return val

################################################################
################################################################

class Alien_red(Alien):
    
    def __init__(self,c):
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        self.c = c
        # contstructor to complete
        super().__init__(c, 4, "red" , 50, 50, 2)
    # to complete
    
    def activate(self, x, y):
        self.x = x
        self.y = y
        
        self.x = random.randint(0, self.c.winfo_width())
        self.y = 0
        
        self.alien = self.c.create_image(self.x, self.y,anchor=CENTER,image=self.image)
        self._active = True

###############################################################
###############################################################

class Alien_green(Alien_red):

    # to complete
    def __init__(self, c):
        self.c = c
        Alien.__init__(self.c, 4, "green", 50, 50, 4)
        super().__init__(self.c)
        self.image = PhotoImage(file="alien_green.png")
        
    
    def next(self):
        
        if self.is_active() == True:
            self.y += self.p_inc
            w_x = random.randint(-5,5)
            self.c.move(self.alien, w_x, self.p_inc)
        
        if self.y >= self.canvas.winfo_height():
            self.deactivate()    

###############################################################
###############################################################
                


class Alien_blue(Alien_red):


    # to complete
    def __init__(self, c):
        self.c = c
        Alien.__init__(self, self.c, 4, "blue", 50, 50, 3)
        super().__init__(self.c)
        self.image = PhotoImage(file="alien_blue.png")
    
    def next(self):
        
        if self.is_active() == True:
            
            ang = random.randint(-160, -20)
            x_val = self.p_inc * math.cos((math.pi/180) * ang)
            y_val = self.p_inc * math.sin((math.pi/180) * ang)
            x_fin = int(math.sqrt(x_val**2))
            y_fin = int(math.sqrt(y_val**2))
            
            self.x += x_fin
            self.y += y_fin
            
            if (self.x >= self.c.winfo_width()):
                x_fin = x_fin * -1
            
            self.c.move(self.alien, x_fin, y_fin)

        if self.y >= self.canvas.winfo_height():
            self.deactivate()
        
###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
    print(x,y,result)


    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        alien=Alien_blue(canvas)

        alien.activate(w, h)
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate(w, h)
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

