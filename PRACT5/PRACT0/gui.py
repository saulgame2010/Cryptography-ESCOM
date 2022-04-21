# -*- coding: utf-8 -*-
#GUI PARA EL CIFRADOR AES
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from tkinter.filedialog import askopenfilename
import sys
from Crypto.Cipher import AES
import Crypto.Random  as rand
from playsound import playsound

def generateKey(event):
	fout = open("key.aes","wb")
	keyBytes = 	rand.get_random_bytes(16)
	fout.write(keyBytes)
	fout.close()

def selectKey(event):
	global key
	global statLoadKey
	key = askopenfilename()
	statLoadKey["text"] = str(key)
	key = open(key,"rb")

def selectFile(event):
	global file
	global filesatus
	file = askopenfilename()
	filesatus["text"] = str(file)
	file = open(file,"rb")

def encryptText(event):
	global file
	global key
	playsound('adarle.mp3')
	key = key.read()
	cipher = AES.new(key,AES.MODE_EAX)
	ciphertext, tag = cipher.encrypt_and_digest(file.read())
	file_out = open(file.name[:-4]+"_c.txt", "wb")
	[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
	file_out.close()

def decryptText(event):
	global file 
	global key
	try:
		key = key.read()
		nonce, tag, ciphertext = [ file.read(x) for x in (16, 16, -1) ]
		cipher = AES.new(key, AES.MODE_EAX, nonce)
		data = cipher.decrypt_and_verify(ciphertext, tag)
		file_out = open(file.name[:-6]+"_d.txt", "w")
		data = ''.join(data.decode('utf-8').split("\r"))
		file_out.write(data)
		file_out.close()
		playsound('viento.mp3')
	except Exception:
		messagebox.showinfo("Error","An error ocurred,, message has been modified")

#CREAMOS LA VENTANA Y ASIGNAMOS UN TAMAÑO
window = tk.Tk()
window.title("AES 128 bits")
frame = tk.Frame(master=window,width=500,height=330,bg="black")
#CREAMOS EL SALUDO
greeting = tk.Label(text="WELCOME TO AES CIPHER!",foreground="crimson",background="black",width=35,height=4,font=("Courier",16))
greeting.place(x=10,y=0)

#CREAMOS UN LABEL DE INSTRUCCIONES
keygen = tk.Button(text="GENERATE KEY",width=12,height=1,fg="aqua",bg="black")
keygen.place(x=20,y=80)
keygen.bind("<Button-1>",generateKey)

#CREAMOS EL BOTÓN loadkey Y LOADKEY
loadkey = tk.Button(text="LOAD KEY",width=10,height=1,fg="aqua",bg="black")
loadkey.place(x=20,y=120)
loadkey.bind("<Button-1>",selectKey	)

statLoadKey = tk.Label(text="STATUS:",foreground="lime",background="black",height=2,font=("Courier",10),anchor="w")
statLoadKey.place(x=110,y=110)
#CREAMOS OTRO LABEL DE INSTRUCCIONES
instB = tk.Label(text="SELECT FILE:\tSTATUS:",foreground="lime",background="black",height=2,font=("Courier",10),anchor="w")
instB.place(x=10,y=150)

#CREAMOS EL BOTÓN PAR EL ARCHIVO
loadfile = tk.Button(text="LOAD FILE",width=10,height=1,fg="aqua",bg="black")
loadfile.bind("<Button-1>",selectFile)
loadfile.place(x=20,y=190)

#CREAMOS UN LABEL STATUS PARA EL ARCHIVO
filesatus = tk.Label(text="NO FILE SELECTED...",foreground="lime",background="black",width=40,height=1,font=("Courier",10),anchor="w")
filesatus.place(x=130,y=190)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
instC = tk.Label(text="SELECT OPERATION:",foreground="medium purple",background="black",height=2,font=("Courier",10),anchor="w")
instC.place(x=10,y=220)

#CREAMOS EL BOTÓN DE ENCRYPT Y DECRYPT
encbtn = tk.Button(text="ENCRYPT",width=10,height=1,fg="hot pink",bg="black")
encbtn.bind("<Button-1>",encryptText)
encbtn.place(x=20,y=265)
decbtn = tk.Button(text="DECRYPT",width=10,height=1,fg="hot pink",bg="black")
decbtn.bind("<Button-1>",decryptText)
decbtn.place(x=110,y=265)

frame.pack()
file = None
key = None
try:
	window.mainloop()
except KeyboardInterrupt:
	sys.exit()