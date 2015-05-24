from Tkinter import *
import random

# d(0_0)b

main = Tk()
main.title('Defend!')
main.minsize(1000,500)
menucanv = Canvas(main)
menucanv.config(width=1000,height=500)

bg = PhotoImage(file="bg.gif")
menucanv.create_image(500,250,image=bg)
buttonimg = PhotoImage(file="button.gif")




def start():
    root = Toplevel()
    root.title('Defend!')

    enemy = "woo"
    missile = "thingy!"
    global crossimg
    crossimg = "whoo!"
    



    root.minsize(1000,500)
    canvas = Canvas(root)
    canvas.config(width=1000,height=500)

    global thing
    global score
    global death
    global enemy
    global missile
    global player
    global cross



    cross = 0
    thing = True
    score = 0
    enemy = "foobar"


    class Missile(object):
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def move(self):
            self.x += 20
            canvas.coords(missile,self.x,self.y)
    class Enemy(object):
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def move(self):
            self.x -= speedcount
            canvas.coords(enemy,self.x,self.y)
    class Player(object):
        def __init__(self,y):
            self.y = y
        def up(self):
            self.y -= 30
            canvas.coords(player,100,self.y)
        def down(self):
            self.y += 30
            canvas.coords(player,100,self.y)
    class Boss(object):
        def  __init__(self,x):
            self.x = x
        def move(self):
            global bossimg
            self.x -= 1
            canvas.coords(bossimg,self.x,250)
        def create(self):
            global bossimg
            bossimg = canvas.create_image(self.x,250,image=boss_sprite)
    class Cross(object):
        def __init__(self,x):
            self.x = x
        def move(self):
            global crossimg
            global crossy
            self.x -= 10
            canvas.coords(crossimg,self.x,crossy)
                
        
    playersprite = PhotoImage(file="Cannon.gif")
    missilesprite = PhotoImage(file="Fetus.gif")
    enemysprite = PhotoImage(file="Freddy.gif")
    
    boss_sprite = PhotoImage(file="Boss.gif")
    cross_sprite = PhotoImage(file="Cross.gif")


    playercoords = Player(y=250)
    player = canvas.create_image(100,playercoords.y,image=playersprite)
    
    def loss():
        global score
        score = score
        canvas.delete(enemy)
        ensurance = True
    
        root.destroy()
    
        loss = Toplevel()
        loss.minsize(1000,500)
        loss.title("You Died with %s points!" % score)
        
        text = Text(loss)
    
        text.insert(INSERT,"You've Lost!")
        text.config(state=DISABLED)
        text.pack()
    
        loss.mainloop()

    def missilemovement():
        global missile_instance
        global missile
    
    
            

        
        if missile_instance.x < 1000:
           missile_instance.move()
        else:
            canvas.delete(missile)
            
            
            
    
        
        root.after(1,missilemovement)
    


    


    def fire(event):
        global thing
        global missile_instance
        global missile
    
        checker = canvas.find_all()
    
        if missile not in checker:    
            missile_instance = Missile(x=450,y=playercoords.y - 4)
            missile = canvas.create_image(missile_instance.x,missile_instance.y,image=missilesprite)
    
            if thing == True:
                missilemovement()
                thing = False
    




    def up(event):
        if playercoords.y > 95:
            playercoords.up()
   
        
    def down(event):
        if playercoords.y < 450:
            playercoords.down()
        
        
    



    




    def detect():
        global enemy
        global score
        enemybbox = canvas.bbox(enemy)
        ensurance = False
    
    
        if enemybbox is not None:
            overlap = canvas.find_overlapping(*enemybbox)
        if 'overlap' in locals() or 'overlap' in globals():
            try:
                if overlap[1] == missile:
                    score += 1
                    global speedcount
                    speedcount += 1
                    canvas.delete(enemy)
                    canvas.delete(missile)
                
            except IndexError:
                pass
    
    
    
        
        
        
        if enemycoords.x < 0 and ensurance == False:
           loss()

    
        root.after(5,detect)
    

    global speedcount
    speedcount = 0 
    
    
    def crossloop():
        global cross
        cross.move()
        
        if cross.x <= 0:
            canvas.delete(crossimg)
        
        root.after(2,crossloop)
    
    def crosses():
        global cross
        global crossimg
        global crossy
        
        crosschecker = canvas.find_all()
        
        if crossimg not in crosschecker:
            thingyy = boss.x - 200
            cross = Cross(x=thingyy)
            crossy = playercoords.y
            crossimg = canvas.create_image(cross.x,crossy,image=cross_sprite)
            
        root.after(10,crosses)
        
        
        
        
        
        
    
    global true
    true = True
    def bossloop():
        global true
        boss.move()
        if true == True:
            crosses()
            true = False
            
        root.after(40,bossloop)
    
    def bossfight():
        global boss
        boss.create()
        bossloop()
        crossloop()
        
        
    global num
    global counter
    num = True
    counter = 0


    def enemyloop():
        global enemy
        global enemycoords
        global ensurance
        global boss
        global num
        global cross
        global crossimg
        global missile
        global counter
    
        checker = canvas.find_all()
        if enemy not in checker:
            enemycoords = Enemy(x=900,y=random.randint(50,450))
            playerbbox = canvas.bbox(player)
            if enemycoords.y > playerbbox[1] and enemycoords.y < playerbbox[3]:
                pass
            else:
                if score <= 7:
                    enemy = canvas.create_image(enemycoords.x,enemycoords.y,image=enemysprite)
                else:
                    if num == True:
                        boss = Boss(x=1000)
                        bossfight()
                        num = False
        if enemy in checker:
            enemycoords.move()
            
        
        if cross != 0:
            crossbbox = canvas.bbox(crossimg)
            infront = boss.x - 200
            if crossbbox is not None:
                crosscollision = canvas.find_overlapping(*crossbbox)
                if len(crosscollision) > 1 and cross.x < 300 or boss.x < 50:
                    loss()
    
        
        if missile != "thingy!" and num == False:
            missile_bbox = canvas.bbox(missile)
            if missile_bbox is not None:
                missile_overlap = canvas.find_overlapping(*missile_bbox)
                
                if len(missile_overlap) > 1:
                    counter += 1
                    canvas.delete(missile)
                    
                    if counter == 30:
                        root.destroy()
                    
                        victory = Tk()
                        victory.title('You Win!')
                    
                        text = Text(victory)
                    
                        text.insert(INSERT,"You've Won!")
                        text.config(state=DISABLED)
                    
                    
                        text.pack()
                    
                    
                    
                        victory.mainloop()
        
        root.after(1,enemyloop)
    
    enemyloop()
    detect()



    root.bind("<Up>",up)
    root.bind("<Down>",down)
    root.bind("<z>",fire)














    canvas.pack()
    root.mainloop()

startbutton = Button(menucanv,image=buttonimg,command=start)
buttonwindow = menucanv.create_window(500,150,window=startbutton)





menucanv.pack()
main.mainloop()