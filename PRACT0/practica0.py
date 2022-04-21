from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

ventana = Tk()

def archivos():	
	global filename
	Tk().withdraw() 
	filename = askopenfilename() 
	rutaL = Label(frame, text = filename, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 150)

def cifrar():	
	global pasE
	global filename
	llave = str.encode(pasE.get())
	datos = open(filename, "rb").read()
	cipher = AES.new(llave, AES.MODE_EAX)
	textoC, tag = cipher.encrypt_and_digest(datos)
	archivoS = open("Marley_C.txt", "wb")
	[ archivoS.write(t) for t in (cipher.nonce, tag, textoC) ]
	archivoS.close()
	messagebox.showinfo("Cifrado", "Su archivo ha sido cifrado")

def des():
	global pasE
	global filename
	archivoE = open(filename, "rb")
	nonce, tag, textoC = [ archivoE.read(t) for t in (16, 16, -1) ]
	llave = str.encode(pasE.get())
	cipher = AES.new(llave, AES.MODE_EAX, nonce)
	datos = cipher.decrypt_and_verify(textoC, tag)
	archivoD = open("Marley_D.txt", "wb")
	archivoD.write(datos)
	archivoD.close()
	messagebox.showinfo("Descifrado", "Su archivo ha sido descifrado")

ventana.resizable(False, False)
frame = Frame()
frame.pack()
frame.config(bg="#f0c0fa")
frame.config(width = "650", height = "450")
frame.config(bd = "20")
frame.config(relief = "ridge")
frame.config(cursor = "heart")
bienL = Label(frame, text = "Bienvenidos a la práctica 0 AES", fg = "purple", font = ("Comic Sans MS", 14), bg = "#f0c0fa").place(x = 150, y  = 20)
pasL = Label(frame, text = "Ingrese su contraseña (16 caracteres):", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 70)
pasE = Entry(frame, fg = "#a8588d", font = ("Comic Sans MS", 12))
pasE.place(x = 320, y  = 70)
archL = Label(frame, text = "Seleccionar archivo", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 110)
botonA = Button(frame, text = "Cargar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = archivos).place(x = 200, y = 110)
filename = "No se ha seleccionado ningún archivo"
rutaL = Label(frame, text = filename, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 150)		
cifrarB = Button(frame, text = "Cifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = cifrar).place(x = 150, y = 190)
desB = Button(frame, text = "Descifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = des).place(x = 300, y = 190)


ventana.mainloop()