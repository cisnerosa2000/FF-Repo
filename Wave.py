from Tkinter import *
import random


root = Tk()
root.title("""Adrian's Seismic Wave Simulator""")
canvas = Canvas(root)
canvas.config(width=1300,height=500)




        
        
sprite = PhotoImage(file="rockets.gif")





global true
true = True

def missileloop():
    canvas.move("missile",50,0)
    #replace 0 with random to move missiles with a random y deviation^
    
    # deletes missiles as soon as they exit the screen
    canvas.addtag_overlapping("out_of_bounds",1290,0,1300,500)
    canvas.delete("out_of_bounds")
    #^^^^^^^^^^^^
    
    root.after(5,missileloop)
    
    
def create():
    global true
    
    y = canvas.winfo_pointery()
    y = canvas.canvasy(y)
    #gets cursor coords
    
    missile = canvas.create_image(10,y-50,image=sprite,tags="missile")
    root.after(10,create)
    
    
    if true == True:
        missileloop()
        true = False
        
create()



















canvas.pack()
root.mainloop()

    