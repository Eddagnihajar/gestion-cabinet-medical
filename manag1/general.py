# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:59:50 2021

@author: Manal
"""
from tkinter import *
from tkinter import PhotoImage
from tkinter import Canvas
from PIL import ImageTk, Image
import tkinter

window = Tk()

window.geometry('600x450')
window.title('Gesion de cabinet médical')
   
   
   #window['bg']='#B5C9E2'
f = ("MV Boli", 16)

def RDVpage():

    window.destroy()
    import mini_pro
    
    
    
        
def patientPage():
    window.destroy()
    import mini_pro2
   
def traitementpage():
    
    window.destroy()
    import traitement
def comentpage():
    window.destroy()
    import commentaire
    
img = PhotoImage(file= "hahena.png" ) 
label = Label(window, image=img)
label.place(x = 0,y = 0)   
 
#2label2 = Label(
    #window,
    #text="la page générale",
    #font = f,
    #padx=5,
    #pady=5,
   #bg='black'
#).pack(expand=FALSE, fill=BOTH)

 
Button(
    window, 
    text="Gestion Commentaire",
    font = f,
    width = 25,
    bg='#B5C9E2',
    command=comentpage
    ).pack(side=BOTTOM,padx=5,pady=30)
Button(
    window, 
    text="Gestion Traitement",
    font = f,
    width = 25,
     bg='#B5C9E2',
    command=traitementpage
    ).pack(side=BOTTOM ,padx=5,pady=30)

Button(
    window, 
    text="Gestion Rendez-vous",
    font = f,
    width = 25,
    bg='#B5C9E2',
    command=RDVpage
    ).pack(side=BOTTOM,padx=5,pady=30)
Button(
    window, 
    text="Gestion Patient", 
    font=f,
    width = 25,
    relief=RAISED,
    bg='#B5C9E2',
    command=patientPage
    ).pack(side=BOTTOM,padx=5,pady=30)


window.iconbitmap(r'logo.ico')
window.mainloop()

