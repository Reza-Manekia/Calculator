from tkinter import * 

operator = ""

def btnClk(numbers):
    global operator 
    operator += str(numbers) 
    text_input.set(operator)

def btnEquals():
    global operator
    
    ans = str(eval(operator))
    text_input.set(ans)
    operator = ans 
   

def btnClear():
    global operator
    operator = ""
    text_input.set(operator)

calc = Tk()
calc.title("CALCULATOR")

text_input = StringVar()

display = Entry(calc, textvariable= text_input, insertwidth=5, bd=8, bg='light blue',font=("arial", 15, "bold"),justify='right').grid(columnspan=4)

btn0 = Button(calc, text="0", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(0)).grid(row=4,column=1)
btn1 = Button(calc, text="1", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(1)).grid(row=3,column=0)
btn2 = Button(calc, text="2", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(2)).grid(row=3,column=1)
btn3 = Button(calc, text="3", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(3)).grid(row=3,column=2)
btn4 = Button(calc, text="4", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(4)).grid(row=2,column=0)
btn5 = Button(calc, text="5", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(5)).grid(row=2,column=1)
btn6 = Button(calc, text="6", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(6)).grid(row=2,column=2)
btn7 = Button(calc, text="7", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(7)).grid(row=1,column=0)
btn8 = Button(calc, text="8", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(8)).grid(row=1,column=1)
btn9 = Button(calc, text="9", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command=lambda:btnClk(9)).grid(row=1,column=2)

add = Button(calc, text="+", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command= lambda:btnClk("+")).grid(row=1,column=4)
subtract = Button(calc, text="-", bd=8, padx=10, fg="black", font=("arial", 20, "bold"),command= lambda:btnClk("-") ).grid(row=2,column=4)
product = Button(calc, text="*", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command= lambda:btnClk("*")).grid(row=3,column=4)
division = Button(calc, text="/", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command= lambda:btnClk("/")).grid(row=4,column=4)


equal = Button(calc, text="=", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command= btnEquals).grid(row=4,column=2)
clear = Button(calc, text="C", bd=8, padx=10, fg="black", font=("arial", 20, "bold"), command = btnClear).grid(row=4,column=0)

calc.mainloop()



