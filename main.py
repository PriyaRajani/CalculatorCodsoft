# Here goes the code for calculator project which I named as Calc-U-Later🙂
from tkinter import *

val = " "


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_click_3():
    global val
    val = val + "3"
    data.set(val)


def btn_click_4():
    global val
    val = val + "4"
    data.set(val)


def btn_click_5():
    global val
    val = val + "5"
    data.set(val)


def btn_click_6():
    global val
    val = val + "6"
    data.set(val)


def btn_click_7():
    global val
    val = val + "7"
    data.set(val)


def btn_click_8():
    global val
    val = val + "8"
    data.set(val)


def btn_click_9():
    global val
    val = val + "9"
    data.set(val)


def btn_click_0():
    global val
    val = val + "0"
    data.set(val)


def btn_click_plus():
    global val
    val = val + "+"
    data.set(val)


def btn_click_minus():
    global val
    val = val + "-"
    data.set(val)


def btn_click_multiply():
    global val
    val = val + "*"
    data.set(val)


def btn_click_divide():
    global val
    val = val + "/"
    data.set(val)


def clear():
    global val
    val = ""
    data.set("")


def calculate():
    global val
    try:
        result = eval(val)
        result = round(result, 5)  # Round to 5 decimal places
        data.set(result)
        val = str(result)
    except ZeroDivisionError:
        data.set("Error:Division by zero")
        val = ""
    except SyntaxError:
        data.set("Error: Invalid expression")
        val = ""


root = Tk()
root.geometry("300x450+300+200")
root.resizable(False, False)
root.title("Calc-U-Later🙂")

data = StringVar()

lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    background="#ECF2FF",
    fg="#000000"
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_3
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_plus

)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_4
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_5
)
btn6.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_6
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_minus
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_7
)
btn9.pack(side=LEFT, expand=True, fill="both")

btn10 = Button(
    btnrow3,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_8
)
btn10.pack(side=LEFT, expand=True, fill="both")

btn11 = Button(
    btnrow3,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_9
)
btn11.pack(side=LEFT, expand=True, fill="both")

btn12 = Button(
    btnrow3,
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_multiply
)
btn12.pack(side=LEFT, expand=True, fill="both")

btn13 = Button(
    btnrow4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=clear
)
btn13.pack(side=LEFT, expand=True, fill="both")

btn14 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_0
)
btn14.pack(side=LEFT, expand=True, fill="both")

btn15 = Button(
    btnrow4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=calculate
)
btn15.pack(side=LEFT, expand=True, fill="both")

btn16 = Button(
    btnrow4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_click_divide
)
btn16.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
