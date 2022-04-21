# -*- coding: utf-8 -*-
#GUI PARA EL CIFRADOR RSA
import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sys
from playsound import playsound
from rsacipher import Cipher

def generate_new_keys(event):
	rsa.generate_keys()
	messagebox.showinfo("RSA Keys","Keys generated successfully!")

def select_public_key(event):
	global publicKey
	global statusPubKey
	filePublicKey = askopenfilename()
	statusPubKey["text"] = str(filePublicKey)
	publicKey = rsa.load_public_key(filePublicKey)

def select_private_key(event):
	global privateKey
	global statusPrvKey
	filePrivateKey = askopenfilename()
	statusPrvKey["text"] = str(filePrivateKey)
	privateKey = rsa.load_private_key(filePrivateKey)

def select_file(event):
	global file
	global filesatus
	file = askopenfilename()
	filesatus["text"] = str(file)
	file = open(file,"rb")

def sign_file(event):
	global file
	global privateKey
	rsa.generate_signature(file.read(),privateKey,file.name[:-4]+"_signed.rsa")
	messagebox.showinfo("Signed","File signed successfully!")
	file.close()

def verify_file(event):
	global file
	global publicKey
	op = rsa.verify_signature(file.read(),publicKey)
	if op == 1:
		messagebox.showinfo("Verifying...","Signature valid!")
	else:
		messagebox.showinfo("Verifying...","Signature invalid! :(")
	file.close()

#CREAMOS LA VENTANA Y ASIGNAMOS UN TAMAÑO
window = tk.Tk()
window.title("RSA Cipher")
frame = tk.Frame(master=window,width=500,height=460,bg="black")
#CREAMOS EL SALUDO
greeting = tk.Label(text="WELCOME TO RSA CIPHER!",foreground="crimson",background="black",width=35,height=4,font=("Courier",16))
greeting.place(x=10,y=0)

#CREAMOS EL BOTÓN KEYGEN Y LOADKEY
keygen = tk.Button(text="GENERATE NEW PAIR OF KEYS",width=30,height=1,fg="aqua",bg="black")
keygen.bind("<Button-1>",generate_new_keys)
keygen.place(x=140,y=80)

orlbl = tk.Label(text="---- OR ----",foreground="lime",background="black",height=2,font=("Courier",10),anchor="w")
orlbl.place(x=200,y=110)
#CREAMOS OTRO LABEL DE INSTRUCCIONES
instPubKey = tk.Label(text="LOAD PUBLIC KEY:\tSTATUS:",foreground="lime",background="black",height=2,font=("Courier",10),anchor="w")
instPubKey.place(x=10,y=150)

#CREAMOS EL BOTÓN PAR EL ARCHIVO DE LA LLAVE PÚBLICA
loadPublicKey = tk.Button(text="LOAD PUBLIC KEY",width=15,height=1,fg="aqua",bg="black")
loadPublicKey.bind("<Button-1>",select_public_key)
loadPublicKey.place(x=20,y=190)

#CREAMOS UN LABEL STATUS PARA EL ARCHIVO DE LA LLAVE PÚBLICA
statusPubKey = tk.Label(text="NO FILE SELECTED...",foreground="lime",background="black",width=40,height=1,font=("Courier",10),anchor="w")
statusPubKey.place(x=180,y=190)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
instPrvKey = tk.Label(text="LOAD PRIVATE KEY:\tSTATUS:",foreground="medium purple",background="black",height=2,font=("Courier",10),anchor="w")
instPrvKey.place(x=10,y=220)

loadPrivateKey = tk.Button(text="LOAD PRIVATE KEY",width=16,height=1,fg="aqua",bg="black")
loadPrivateKey.bind("<Button-1>",select_private_key)
loadPrivateKey.place(x=20,y=270)

#CREAMOS UN LABEL STATUS PARA EL ARCHIVO
statusPrvKey = tk.Label(text="NO FILE SELECTED...",foreground="lime",background="black",width=40,height=1,font=("Courier",10),anchor="w")
statusPrvKey.place(x=180,y=270)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
instFile = tk.Label(text="LOAD TEXT FILE:\t\tSTATUS:",foreground="medium purple",background="black",height=2,font=("Courier",10),anchor="w")
instFile.place(x=10,y=300)

loadFile = tk.Button(text="LOAD FILE",width=10,height=1,fg="aqua",bg="black")
loadFile.bind("<Button-1>",select_file)
loadFile.place(x=20,y=350)

#CREAMOS UN LABEL STATUS PARA EL ARCHIVO
filesatus = tk.Label(text="NO FILE SELECTED...",foreground="lime",background="black",width=40,height=1,font=("Courier",10),anchor="w")
filesatus.place(x=180,y=350)

#CREAMOS EL BOTÓN DE ENCRYPT Y DECRYPT
encbtn = tk.Button(text="SIGN FILE",width=10,height=1,fg="hot pink",bg="black")
encbtn.bind("<Button-1>",sign_file)
encbtn.place(x=20,y=400)

decbtn = tk.Button(text="VERIFY",width=10,height=1,fg="hot pink",bg="black")
decbtn.bind("<Button-1>",verify_file)
decbtn.place(x=110,y=400)


frame.pack()
file = None
publicKey = None
privateKey = None
try:
	rsa = Cipher()
	window.mainloop()
except KeyboardInterrupt:
	sys.exit()