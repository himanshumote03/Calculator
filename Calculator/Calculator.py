from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=" :
        if scvalue.get().isdigit():
            value = int(opvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        opvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        opvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("300x485")
root.maxsize(300, 485)
root.minsize(300, 485)
root. title("Calculator")
root.wm_iconbitmap("calci2.ico")
root.configure(background="#1B2430")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 25 bold", justify="right")
screen.pack(fill=X, ipadx=8, pady=(10, 1), padx=10)

opvalue = StringVar()
opvalue.set("")
outputScreen = Label(root, textvariable=opvalue, font="lucida 25 bold", anchor="e")
outputScreen.pack(fill=X, ipadx=8, padx=10, pady=(1, 10))


# Frame 1
f = Frame(root, bg="#2C3639")
b = Button(f, text="C", padx=10, pady=5, font="lucida 20 bold", bg="#1B2430", fg="red", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="(", padx=14, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text=")", padx=14, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=8, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

f.pack()

# Frame 2
f = Frame(root, bg="#2C3639")
b = Button(f, text="1", padx=11, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=14.5, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5.4)
b.bind("<Button-1>", click)

f.pack()

# Frame 3
f = Frame(root, bg="#2C3639")
b = Button(f, text="4", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=13.4, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

f.pack()


# Frame 4
f = Frame(root, bg="#2C3639")
b = Button(f, text="7", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=14, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

f.pack()

# Frame 5
f = Frame(root, bg="#2C3639")
b = Button(f, text=".", padx=15, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=12, pady=5, font="lucida 20 bold", bg="#1B2430", fg="cyan", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=10, pady=5, font="lucida 20 bold", bg="blue", fg="white", relief=RAISED)
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
