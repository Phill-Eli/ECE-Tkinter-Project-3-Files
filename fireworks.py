from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################

        ### To complete
        t = 0
        while True:
                rand_x = random.randint(0,w)
                rand_r = random.randint(100, 300)
                op = [h//4, 3*h//4]
                rand_cmax = random.choice(op)
                rand_pinc = random.randint(2,7)
                colors = ["blue", "yellow", "green", "purple", "red", "orange"]
                rand_clr = random.choice(colors)
            
                Missile.add_missile(canvas, missiles, rand_x, rand_cmax, rand_pinc, rand_clr )
            
                for m in missiles:
                        m.next()
                        if m.is_active() == False:
                                Explosion.add_explosion(canvas, booms, rand_x, m.y, rand_r, rand_clr)   
                                for b in booms:
                                        b.next()
                """for m in missiles:
                        print(m.is_active(),end=" ")
                        print()
                """
                root.update()   # update the graphic (redraw)
                time.sleep(0.01)  # wait 0.01 second  
                t=t+1
        
        root.mainloop()   

if __name__=="__main__":
    main()

