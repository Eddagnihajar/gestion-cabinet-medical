# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:28:17 2021

@author: Manal
"""

from tkinter import *
import sqlite3
import tkinter
from tkinter.ttk import Separator
from tkinter import messagebox
conn = sqlite3.connect('mydb.db')
c = conn.cursor()
ids = []
ids_p = []
number = []
patients = []

class Application2:

    def __init__(self, window):

        self.window = window
        self.v = IntVar()
        c.execute("SELECT * FROM commentaire")
        self.alldata=c.fetchall()
# creating the frames in the window
        self.main = Frame(window, width=450, height=400, bg="#B5C9E2")

        self.showdetailsframe = Frame(self.window)
        self.updateframe = Frame(self.window)
        self.deleteframe = Frame(self.window)
    def startpage(self):
       
        # labels for the window
        self.heading = Label(self.main, text="MHZ Commentaires",font=('Forte',25) ,fg='black',bg="#B5C9E2")
        self.heading.place(x=90, y=20)

        # name

        self.name = Label(self.main, text="Nom de Patient", font=('arial 12 bold'),bg="#B5C9E2")
        self.name.place(x=0, y=110)

        # age

        self.age = Label(self.main, text="Age", font=('arial 12 bold'),bg="#B5C9E2")
        self.age.place(x=0, y=155)
        
         # CIN

        self.CIN = Label(self.main, text="CIN", font=('arial 12 bold'),bg="#B5C9E2")
        self.CIN.place(x=0, y=200)

        # traitement

        self.coment = Label(self.main, text="Commentaire", font=('arial 12 bold'),bg="#B5C9E2")
        self.coment.place(x=0, y=250)
        
        


       

# text box for lables

        self.name_ent = Entry(self.main, width=30)
        self.name_ent.place(x=140, y=115)

        self.age_ent = Entry(self.main, width=30)
        self.age_ent.place(x=140, y=160)
       
        self.CIN_ent = Entry(self.main, width=30)
        self.CIN_ent.place(x=140, y=200)
        
        self.coment_ent = Entry(self.main, width=30)
        self.coment_ent.place(x=140, y=250)
        
       
# button to perform a command

        self.submit = Button(self.main, text="Ajouter commentaire", font="aried 12 bold",width=16, height=1, bg='#B09390',command=self.add_appointment)
        self.submit.place(x=145, y=310)

#show log

        sql2 = "SELECT id_c FROM commentaire "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids

        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

       #  display the logs in our frame

        self.logs = Label(self.main, text="TOTAL\n des comentaires", font=('arial 10 bold'), fg='black',bg="#B5C9E2")
        self.logs.place(x=330, y=320)
        self.logs = Label(self.main, text=" " + str(self.final_id), width=8, height=1,relief=SUNKEN).place(x=360, y=360)


        self.main.pack()

# funtion to call submit button

    def add_appointment(self):

        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.CIN_ent.get()
        self.val4 = self.coment_ent.get()
        
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
          tkinter.messagebox.showinfo("Attention!!!", "STP remplir tous les champs ")
        else:

            sql = "INSERT INTO 'commentaire' ( nom, age, cin, commantaire) VALUES(?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4))
            conn.commit()
            tkinter.messagebox.showinfo("Succ??s", "\n ajout pour " + str(self.val1) + " bien cr??er ")
        self.main.destroy()
        self.__init__(self.window)
        self.startpage()

    def homee(self):
        self.main.destroy()
        self.showdetailsframe.destroy()
        self.updateframe.destroy()
        self.deleteframe.destroy()
        self.__init__(self.window)
        self.startpage()
        self.main.pack()

    def showdetails(self):
        self.main.destroy()
        self.showdetailsframe.destroy()
        self.updateframe.destroy()
        self.deleteframe.destroy()
        self.__init__(self.window)
        count1=0
        count2=0
        clmnname=['Id_Patient','Nom','Age','Cin','Commentaire']
        for i in range(len(clmnname)):
            Label(self.showdetailsframe,text=clmnname[i],font="ariel 12 bold").grid(row=0,column=i*2)
            Separator(self.showdetailsframe,orient=VERTICAL).grid(row=0,column=i*2,sticky='ns')
        clmnname=['Id_Patient','Nom','Age','Cin','Commentaire']
        for i in range(len(clmnname)):
            Label(self.showdetailsframe,text=clmnname[i],font="ariel 12 bold").grid(row=0,column=i*2)
            Separator(self.showdetailsframe,orient=VERTICAL).grid(row=0,column=i*2+1,sticky='ns')
        for i in range(len(self.alldata)):
            for j in range(5):
                Label(self.showdetailsframe, text = self.alldata[i] [j],font="ariel 10").grid(row=count1+2, column=count2*2)
                Separator(self.showdetailsframe, orient=VERTICAL).grid(row=count1+2, column=count2 * 2 +1 ,sticky='ns')
                count2+=1
            count2=0
            count1+=1
        self.showdetailsframe.pack()


    def updatee(self):
        self.main.destroy()
        self.showdetailsframe.destroy()
        self.updateframe.destroy()
        self.deleteframe.destroy()
        self.__init__(self.window)

        self.id = Label(self.updateframe, text="Donnez le num??ro de commentaire a modifier ", font=('arial 12 bold'),fg="red")
        self.id.place(x=0, y=12)
        self.idnet = Entry(self.updateframe, width=10)
        self.idnet.place(x=360, y=18)
        self.search = Button(self.updateframe, text="Chercher", font="aried 12 bold", width=10, height=1,bg='#B09390',command=self.update1)
        self.search.place(x=160, y=50)
        self.updateframe.pack(fill='both', expand=True)

    def update1(self):
        self.input = self.idnet.get()
        # execute sql
        sql = "SELECT * FROM commentaire WHERE id_c LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.cin = self.row[3]
            self.coment = self.row[4]
            
        # creating the update form
        self.uname = Label(self.updateframe, text="Nom de Patient", font=('arial 14 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.updateframe, text="Age", font=('arial 14 bold'))
        self.uage.place(x=0, y=180)

        self.ucin = Label(self.updateframe, text="cin", font=('arial 14 bold'))
        self.ucin.place(x=0, y=220)

        self.ucoment = Label(self.updateframe, text="commentaire", font=('arial 14 bold'))
        self.ucoment.place(x=0, y=260)
#entrys
        self.ent1 = Entry(self.updateframe, width=30)
        self.ent1.place(x=180, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.updateframe, width=30)
        self.ent2.place(x=180, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.updateframe, width=30)
        self.ent3.place(x=180, y=220)
        self.ent3.insert(END, str(self.cin))

        self.ent4 = Entry(self.updateframe, width=30)
        self.ent4.place(x=180, y=260)
        self.ent4.insert(END, str(self.coment))

#buttons for update and delete
        self.update = Button(self.updateframe, text="modifier", font="aried 12 bold", width=10, height=1, bg='#B09390',command=self.update2)
        self.update.place(x=210, y=340)
        self.updateframe.pack()

    def update2(self):

            # declaring the variables to update
            self.var1 = self.ent1.get()
            self.var2 = self.ent2.get()
            self.var3 = self.ent3.get()
            self.var4 = self.ent4.get()
  

            query = "UPDATE commentaire SET nom=?, age=?, cin=?, commantaire=? WHERE id_c LIKE ?"
            c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.idnet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Succ??s", "Modification r??ussite")
            self.updateframe.destroy()
            self.__init__(self.window)
            self.updatee()
            self.updateframe.pack()

    def deletee(self):

            self.main.destroy()
            self.showdetailsframe.destroy()
            self.updateframe.destroy()
            self.deleteframe.destroy()
            self.__init__(self.window)

            self.id = Label(self.deleteframe, text="Donnez le num??ro du commentaire a supprimer ", font=('arial 12 bold'), fg="red")
            self.id.place(x=0, y=12)
            self.idnet = Entry(self.deleteframe, width=10)
            self.idnet.place(x=375, y=18)
            self.search = Button(self.deleteframe, text="Chercher ", font="aried 12 bold", width=10, height=1,
                                 bg='#B09390', command=self.delete1)
            self.search.place(x=160, y=50)
            self.deleteframe.pack(fill='both', expand=True)

    def delete1(self):
        self.input = self.idnet.get()
        # execute sql
        sql = "SELECT * FROM commentaire WHERE id_c LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.cin = self.row[3]
            self.coment = self.row[4]
         
        # creating the update form
        self.uname = Label(self.deleteframe, text="Nom de Patient", font=('arial 14 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.deleteframe, text="Age", font=('arial 14 bold'))
        self.uage.place(x=0, y=180)

        self.ucin = Label(self.deleteframe, text="cin", font=('arial 14 bold'))
        self.ucin.place(x=0, y=220)

        self.ucoment = Label(self.deleteframe, text="commentaire", font=('arial 14 bold'))
        self.ucoment.place(x=0, y=260)

        # entrys
        self.ent1 = Entry(self.deleteframe, width=30)
        self.ent1.place(x=180, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.deleteframe, width=30)
        self.ent2.place(x=180, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.deleteframe, width=30)
        self.ent3.place(x=180, y=220)
        self.ent3.insert(END, str(self.cin))

        self.ent4 = Entry(self.deleteframe, width=30)
        self.ent4.place(x=180, y=260)
        self.ent4.insert(END, str(self.coment))

        # buttons for update and delete
        self.update = Button(self.deleteframe, text="Supprimer", font="aried 12 bold", width=10, height=1, bg='#B09390',
                             command=self.delete2)
        self.update.place(x=210, y=340)
        self.deleteframe.pack()

    def delete2(self):
        sql2 = "DELETE FROM commentaire WHERE id_c LIKE ?"
        c.execute(sql2, (self.idnet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Succ??s", "Suppression r??ussite")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.deleteframe.destroy()
        self.__init__(self.window)
        self.deletee()
        self.deleteframe.pack()
        
def accpage():
       window.destroy()
       import general
def patientPage():
    window.destroy()
    import mini_pro2
   
def traitementpage():
    
    window.destroy()
    import traitement
def RDVpage():
    window.destroy()
    import mini_pro 
def homepage():
    window.destroy()
    import general 
def menubar():
     main_menu = Menu()
     window.config(menu=main_menu)
     message_menu = Menu(main_menu, tearoff=False)
     main_menu.add_cascade(label="Commentaire", menu=message_menu)
     message_menu.add_command(label="Accueil", command=b.homee)
     message_menu.add_command(label="consulter commentaire", command = b.showdetails)
     message_menu.add_command(label="modifier commentaire", command = b.updatee)
     message_menu.add_command(label="supprimer commentaire", command=b.deletee)
     message_menu.add_separator()
     message_menu.add_command(label="Quitter", command=homepage)
     
  
     
     trait_menu = Menu(main_menu, tearoff=False)
     main_menu.add_command(label="Traitement", command=traitementpage)
     patient_menu = Menu(main_menu, tearoff=False)
     main_menu.add_command(label="Patient", command=patientPage)
     coment_menu = Menu(main_menu, tearoff=False)
     main_menu.add_command(label="RDV", command=RDVpage)
    
window = Tk()
b = Application2(window)
b.startpage()
window.config(menu=menubar())
window.title("gestion de cabinet m??dical  ")
window.iconbitmap(r'logo.ico')
window.geometry("450x400")
window.resizable(False, False)
window.mainloop()
    