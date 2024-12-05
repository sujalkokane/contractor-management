from tkinter import *
from tkinter import messagebox
Contractor={
    "id":[],
    'name':[],
    'spec':[]
}
Task={
    'cid':[],
    "task":[],
    'status':False
}
def handle():
    id_n=id.get()
    name=name_entry.get()
    spec=spec_entry .get()
    Contractor['id'].append(id.get())
    Contractor['name'].append(name_entry.get())
    Contractor['spec'].append(spec_entry.get())
    print(Contractor)
    messagebox.showinfo("Hi ",f"HI {name},{id_n},{spec}")
    
def assign():
    Task['cid'].append(cid_Entry.get())
    Task['task'].append(task_Entry.get())
    common=set(Task['cid']) & set(Contractor['id'])
    if(common):
        print(Task)
    else:
        messagebox.showinfo("Hi ","First Assign the Contractor")
root = Tk()
root.title("CONTRACTOR MANAGEMENT SYSTEM")
root.iconbitmap('icon.ico')
root.geometry('800x800')
root.resizable(height=False,width=False)
root.configure(background='#7393B3')
heading=Label(root,text='CONTRACTOR MANAGEMENT SYSTEM')
heading.config(font=('Helvetica',16,'bold'))
heading.grid(row=0,column=0,padx=250,pady=10)

# Contractor Add Fuctionality
contractor_add=Label(root,text="ADD CONTRACTOR",bg='blue')
contractor_add.grid(row=1,column=0,sticky='w',padx=60,pady=30)

#Entry ID
id=Label(root,text='ID:',fg='White',bg='#7393B3',anchor='e')
id.config(font=('verdana',22))
id.grid(row=2,column=0,sticky='w',padx=20)
# Entry
id=Entry(root)
id.grid(row=2,column=0,sticky='w',padx=100,pady=30)
#Entry Name
name_label=Label(root,text='Name:',fg='White',bg='#7393B3',anchor='e')
name_label.config(font=('verdana',22))
name_label.grid(row=3,column=0,sticky='w',padx=20)
# Entry
name_entry=Entry(root)
name_entry.grid(row=3,column=0,sticky='w',padx=100,pady=30)
#Entry Specialization
spec_label=Label(root,text='Specialization:',fg='White',bg='#7393B3',anchor='e')
spec_label.config(font=('verdana',22))
spec_label.grid(row=4,column=0,sticky='w',padx=20)
# Entry
spec_entry=Entry(root)
spec_entry.grid(row=4,column=0,sticky='w',padx=190,pady=30)

# Submir Button
submit_btn=Button(root,text='ADD',bg='white',width=10,height=1,command=handle )
submit_btn.grid(row=5,sticky='w',padx=180)
submit_btn.config(font=('verdana',20))

# Task Assignment
task_label=Label(root,text='TASK ASSIGNMENT',bg='blue')
task_label.grid(row=1,column=0,padx=(340,0))
# Contractor_id label
cid_label=Label(root,text='Contractor ID:',bg="#7393B3")
cid_label.config(font=('verdana',20))
cid_label.grid(row=2,column=0,padx=(140,0))

# Contractor_id Entry
cid_Entry=Entry(root)
cid_Entry.grid(row=2,column=0,padx=(500,0))

# Task label
task_label=Label(root,text='Task:',bg="#7393B3")
task_label.config(font=('verdana',20))
task_label.grid(row=3,column=0,padx=(140,0))

# Task Entry
task_Entry=Entry(root)
task_Entry.grid(row=3,column=0,padx=(500,0))

# Assign Button
assign_btn=Button(root,text='ASSIGN',bg='white',width=10,height=1,command=assign )
assign_btn.grid(row=4,sticky='w',padx=(540,0))
assign_btn.config(font=('verdana',20))



root.mainloop()