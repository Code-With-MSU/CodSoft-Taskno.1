                                # todo list
import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Daily Goals (to-do) list")
root.geometry("400x600+300+10")
root.resizable(False,False)

listOfTheTasks=[]

def ADD_TASK():
   task=taskEntry.get()
   taskEntry.delete(0,END)

   if task:
      with open("List.txt","a") as taskfile:
         taskfile.write(f"\n"+task)
      listOfTheTasks.append(task)
      lisDisplayer.insert(END,task)

def DELETE_TASK():
    selected_task_index = lisDisplayer.curselection()
    
    if selected_task_index:
        task_index = selected_task_index[0]
        del listOfTheTasks[task_index]
        lisDisplayer.delete(task_index)
        
        with open("List.txt", "w") as taskfile:
            for task in listOfTheTasks:
                taskfile.write(task)

         

def openTaskFile():
    try:
        global listOfTheTasks
        with open("List.txt","r") as taskfile:
         tasks=taskfile.readlines()

        for task in tasks:
            if task!='\n':
               listOfTheTasks.append(task)
               lisDisplayer.insert(END,task)
    except:
       file=open("List.txt","w")
       file.close()        


logo=PhotoImage(file="logo.png")
root.iconphoto(False,logo)

taskBar=PhotoImage(file="sun rise.png")
Label(root,image=taskBar).pack()


# main
frame=Frame(root,width=400,height=50,bg="black")
frame.place(x=0,y=130)

task=StringVar
taskEntry=Entry(frame,width=35,font="times 12 bold",bd=0)
taskEntry.place(x=10,y=7)
taskEntry.focus()

AddButton = Button(frame, text="Add", font="Helvetica 20 bold", width=6, bg="orange red", fg="white", bd=0, command=ADD_TASK)
AddButton.place(x=300, y=0) 

frame1=Frame(root,bd=3,width=700,height=280,bg="orange")
frame1.pack(pady=(50,0))

lisDisplayer=Listbox(frame1,font="times 12",width=40,height=16,bg="lemon chiffon",fg="black",cursor="hand2",selectbackground="blue")
lisDisplayer.pack(side=LEFT,fill=BOTH,padx=2)

scroller=Scrollbar(frame1)
scroller.pack(side=RIGHT,fill=BOTH)

lisDisplayer.config(yscrollcommand=scroller.set)
scroller.config(command=lisDisplayer.yview)

openTaskFile()

deleteIcon=PhotoImage(file="bin.png")
deleteIcon=deleteIcon.subsample(3)
Button(root,image=deleteIcon,bd=0,command=DELETE_TASK).pack(side=BOTTOM,pady=10)

developer_label = Label(root, text="Developed by: Muhammad Samiullah", font=("Helvetica b", 10), bg="white")
developer_label.pack(side=BOTTOM, pady=(0, 0))
root.mainloop()
