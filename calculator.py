from tkinter import *
top=Tk()
top.title("calculeter")
top.minsize(600,300)

numbers1=Label(text="FIRST_NUMBER")
numbers1.pack()
numbers1entry=Entry()
numbers1entry.pack()

numbers2=Label(text="second_NUMBER")
numbers2.pack()
numbers2ntry=Entry()
numbers2ntry.pack()

def add():
    num1=int(numbers1entry.get())
    num2=int(numbers2ntry.get())
    ret= num1+num2
    resultlabel=Label(text="the ruselt"+str(ret))
    resultlabel.pack()
But=Button(text="add",command=add)
But.pack()




top.mainloop()




