from tkinter import *
from tkinter import _tkinter
import sys,turtle,numpy

class turtleDraw:
    def __init__(self,root):
        self.root = root

    def buttonClear(self): #Clears button after choice has been made
        for i in self.root.winfo_children():
            i.destroy()  
        self.buttonLoop()

    def endProgram(self): #Ends the program
        self.initVar()
        turtle.Screen().bye()
        sys.exit(0)
        
        
            
        
    def buttonLoop(self):
        try:
            if choices["shape"] == None: #Buttons to choose shape
                Label(self.root, text="What shape would you like to draw?",font="Helvetica 16 bold").grid(row=0,column=0,columnspan=2,sticky="W")
                Button(self.root, text="Star",width=15,height=3, command=lambda:self.setVariable("shape",108)).grid(row=1,column=0 )
                Button(self.root,text="Circular Spiral",width=15,height=3,command=lambda:self.setVariable("shape",121)).grid(row=1,column=1)
                Button(self.root,text="Spiral",width=15,height=3,command=lambda:self.setVariable("shape",90.11)).grid(row=1,column=2)
                Button(self.root,text="Spiral 2",width=15,height=3,command=lambda:self.setVariable("shape",139)).grid(row=1,column=3)
                Button(self.root,text="Sun",width=15,height=3,command=lambda:self.setVariable("shape",170)).grid(row=1,column=4)
                Button(self.root,text="Open Spiral",width=15,height=3,command=lambda:self.setVariable("shape",284)).grid(row=1,column=5)
                Button(self.root,text="Open Spiral 2",width=15,height=3,command=lambda:self.setVariable("shape",304)).grid(row=1,column=6)

            elif choices["shape"] != None and choices["colorNum"] == None: #Buttons to choose # of colors
                Label(self.root, text="How many colors would you like?",font="Helvetica 16 bold").grid(row=0,column=0,columnspan=2,sticky="W")
                Button(self.root,text="1 Color",width=15,height=3,command=lambda:self.setVariable("colorNum",0)).grid(row=1,column=0) 
                Button(self.root,text="2 Colors",width=15,height=3,command=lambda:self.setVariable("colorNum",1)).grid(row=1,column=1)    
                Button(self.root,text="Random Colors",width=15,height=3,command=lambda:self.setVariable("colorNum",2)).grid(row=1,column=2)  

            elif choices["shape"] != None and choices["colorNum"] == 0 and choices["colorChoice"] == None: #Button to choose singular colors
                Label(self.root, text="What color would you like?",font="Helvetica 16 bold").grid(row=0,column=0,columnspan=2,sticky="W")
                Button(self.root,text="Red",width=15,height=3,command=lambda:self.setVariable("colorChoice","red")).grid(row=1,column=0)
                Button(self.root,text="Orange",width=15,height=3,command=lambda:self.setVariable("colorChoice","orange")).grid(row=1,column=1) 
                Button(self.root,text="Yellow",width=15,height=3,command=lambda:self.setVariable("colorChoice","yellow")).grid(row=1,column=2)
                Button(self.root,text="Green",width=15,height=3,command=lambda:self.setVariable("colorChoice","green")).grid(row=1,column=3) 
                Button(self.root,text="Blue",width=15,height=3,command=lambda:self.setVariable("colorChoice","blue")).grid(row=1,column=4)
                Button(self.root,text="Indigo",width=15,height=3,command=lambda:self.setVariable("colorChoice","indigo")).grid(row=1,column=5) 
                Button(self.root,text="Violet",width=15,height=3,command=lambda:self.setVariable("colorChoice","violet")).grid(row=1,column=6) 

            elif choices["shape"] != None and choices["colorNum"] == 2 and choices["colorChoice"] == None: #Sets variable for random color choice
                self.setVariable("colorChoice","rand")

            elif choices["shape"] != None and choices["colorNum"] == 1 and choices["colorChoice"] == None and choices["2colorChoice0"] == None: #Sets first of 2 colors
                Label(self.root, text="Pick your first color",font="Helvetica 16 bold").grid(row=0,column=0,columnspan=2,sticky="W")
                Button(self.root,text="Red",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","red")).grid(row=1,column=0)
                Button(self.root,text="Orange",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","orange")).grid(row=1,column=1)                 
                Button(self.root,text="Yellow",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","yellow")).grid(row=1,column=2)
                Button(self.root,text="Green",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","green")).grid(row=1,column=3) 
                Button(self.root,text="Blue",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","blue")).grid(row=1,column=4)
                Button(self.root,text="Indigo",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","indigo")).grid(row=1,column=5) 
                Button(self.root,text="Violet",width=15,height=3,command=lambda:self.setVariable("2colorChoice0","violet")).grid(row=1,column=6) 
                
            elif choices["shape"] != None and choices["colorNum"] == 1 and choices["colorChoice"] == None and choices["2colorChoice0"] != None and choices["2colorChoice1"] == None: #Sets second of 2 colors
                Label(self.root, text="Pick your second color",font="Helvetica 16 bold").grid(row=0,column=0,columnspan=2,sticky="W")
                Button(self.root,text="Red",width=15,height=3,command=lambda:[self.setVariable("2colorChoice1","red"),self.setVariable("colorChoice","2c")]).grid(row=1,column=0)
                Button(self.root,text="Orange",width=15,height=3,command=lambda:[self.setVariable("2colorChoice1","orange"),self.setVariable("colorChoice","2c")]).grid(row=1,column=1)                 
                Button(self.root,text="Yellow",width=15,height=3,command=lambda:[self.setVariable("2colorChoice1","yellow"),self.setVariable("colorChoice","2c")]).grid(row=1,column=2)
                Button(self.root,text="Green",width=15,height=3,command=lambda:lambda:[self.setVariable("2colorChoice1","green"),self.setVariable("colorChoice","2c")]).grid(row=1,column=3) 
                Button(self.root,text="Blue",width=15,height=3,command=lambda:lambda:[self.setVariable("2colorChoice1","blue"),self.setVariable("colorChoice","2c")]).grid(row=1,column=4)
                Button(self.root,text="Indigo",width=15,height=3,command=lambda:lambda:[self.setVariable("2colorChoice1","indigo"),self.setVariable("colorChoice","2c")]).grid(row=1,column=5) 
                Button(self.root,text="Violet",width=15,height=3,command=lambda:lambda:[self.setVariable("2colorChoice1","violet"),self.setVariable("colorChoice","2c")]).grid(row=1,column=6) 
                
            elif choices["shape"] != None and choices["colorNum"] != None and choices["colorChoice"] != None: #Buttons to either reset the drawing choices, or stop the program entirely
                Button(self.root,text="Stop Drawing",width=15,height=3,command=lambda:[self.initVar(),self.setVariable("shape", None)]).grid(row=0,column=0)
                Button(self.root,text="Stop Program",width=15,height=3,command=lambda:self.endProgram()).grid(row=0,column=1)
                self.turtleDraw()
        except TypeError:
            pass

    def setVariable(self,name,value): #Sets variable based on name and value
        choices[name] = value
        self.buttonClear()

    def initVar(self): #Resets variables to original values
        global choices
        turtle.Screen().clear()
        choices = {"shape":None,"colorNum":None,"colorChoice":None,"2colorChoice0":None,"2colorChoice1":None}
        self.buttonLoop()
    

    def turtleDraw(self): #Draws the shape depending on choices
        painter = turtle.Turtle()
        painter.screen.colormode(255)
        if choices["colorChoice"] != "rand" and choices["colorChoice"] != "2c":
            painter.color(choices["colorChoice"])
        painter.speed(0)
        for i in range(1200):
            if choices["colorChoice"] == "rand":
                painter.pencolor(tuple(numpy.random.choice(range(256), size=3)))
            if choices["colorChoice"] == "2c":
                painter.color(choices[str("2colorChoice" + str(i%2))])
            painter.forward(i)
            painter.right(choices["shape"])

    def run(self):
        self.initVar()        
        self.root.mainloop()

if __name__ == "__main__":
    root= Tk()
    turtleDraw(root).run()