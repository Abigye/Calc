#Calculator using Python GUI Tkinter

from tkinter import *
from tkinter import ttk

#globally declaring our expression variable
expression = ""

# update our expresssion in the text entry box

def press(num):
    global expression
    expression += str(num)
    # update our expressions by using the set method
    equation.set(expression)

# evaluate final expression
def equalpress(): 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable  by empty string 
        expression = "" 
  
    # if error is generate then handle by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  

# clears the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# creating our GUI window 
if __name__ == "__main__":
    # create a GUI window 
    gui = Tk() 
    gui.configure(background="white") 
    gui.title("Simple Calculator") 
    gui.geometry("270x150") 
  
    # StringVar() is the variable class, 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for showing the expression . 
    expression_field = ttk.Entry(gui, textvariable=equation) 

    expression_field.grid(columnspan=4, ipadx=65) 
  
    equation.set('enter your expression') 

    style = ttk.Style()
    style.configure("TButton", foreground="black", background="blue",height =1,width=4)
  
    # creating the buttons
    button1 = ttk.Button(gui, text=' 1 ', style ="TButton",
                     command=lambda: press(1)).grid(row=2, column=0) 
  
    button2 = ttk.Button(gui, text=' 2 ', style ="TButton",
                     command=lambda: press(2)).grid(row=2, column=1) 
  
    button3 = ttk.Button(gui, text=' 3 ', style ="TButton",
                     command=lambda: press(3)).grid(row=2, column=2) 
  
    button4 = ttk.Button(gui, text=' 4 ', style ="TButton",
                     command=lambda: press(4)).grid(row=3, column=0) 
  
    button5 = ttk.Button(gui, text=' 5 ', style ="TButton",
                     command=lambda: press(5)).grid(row=3, column=1) 
  
    button6 = ttk.Button(gui, text=' 6 ', style ="TButton",
                     command=lambda: press(6)).grid(row=3, column=2) 
  
    button7 = ttk.Button(gui, text=' 7 ', style ="TButton",
                     command=lambda: press(7)).grid(row=4, column=0) 
  
    button8 = ttk.Button(gui, text=' 8 ', style ="TButton",
                     command=lambda: press(8)).grid(row=4, column=1) 
  
    button9 = ttk.Button(gui, text=' 9 ', style ="TButton",
                     command=lambda: press(9)).grid(row=4, column=2) 
  
    button0 = ttk.Button(gui, text=' 0 ', style ="TButton",
                     command=lambda: press(0)).grid(row=5, column=0) 
  
    plus = ttk.Button(gui, text=' + ', style ="TButton",
                  command=lambda: press("+")).grid(row=2, column=3) 
  
    minus = ttk.Button(gui, text=' - ', style ="TButton",
                   command=lambda: press("-")).grid(row=3, column=3) 
  
    multiply = ttk.Button(gui, text=' * ', style ="TButton",
                      command=lambda: press("*")).grid(row=4, column=3) 
  
    divide = ttk.Button(gui, text=' / ', style ="TButton",
                    command=lambda: press("/")).grid(row=5, column=3) 
  
    equal = ttk.Button(gui, text=' = ', style ="TButton",
                   command=equalpress).grid(row=5, column=2)  

    clear = ttk.Button(gui, text='Clear', style ="TButton",
                   command=clear).grid(row=6, column=0) 
  
    Decimal= ttk.Button(gui, text='.', style ="TButton",
                    command=lambda: press('.')).grid(row=5, column=1) 

    # start the GUI 
    gui.mainloop() 