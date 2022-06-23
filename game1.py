from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True
    
def shoot(canvas, aliens, booms, ammunition, x, y): 
    ####### to complete
    for alien in aliens:
        if alien.is_active() == True and alien.is_shot(x,y) == True:
            alien.deactivate()
            result="hit!"
            ammunition.increment(alien.ip_val)
            boom = Explosion.add_explosion(canvas, booms, x, y, 300, "white")

        else:
            result="Miss!"
            ammunition.increment(alien.ip_val)
        print(x,y,result)




################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################



        #To complete (time sleep is 0.01s)
        t = 0
        while True:
            time.sleep(0.5)
            Alien.add_alien(canvas, aliens)
            
            rand_x = random.randint(0,w)
            rand_r = random.randint(100, 300)
            colors = ["blue", "yellow", "green", "purple", "red", "orange"]
            rand_clr = random.choice(colors)
            
            for alien in aliens:
                alien.next()
                if alien.is_shot(alien.x, alien.y) == False:
                    Explosion.add_explosion(canvas, booms, alien.x, alien.y, 30, "white")   
                    for b in booms:
                        b.next()
                
                root.update()   # update the graphic (redraw)
                time.sleep(0.01)  # wait 0.01 second  
                t=t+1   



          
        root.update()   
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

