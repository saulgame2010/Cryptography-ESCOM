from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
ventana = Tk()

def archivos():
	global filename
	Tk().withdraw()
	filename = askopenfilename()
	rutaL = Label(frame, text = filename, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 200)

def mostrarV():
	global pasL
	global pasE
	global cifrarB
	global desB
	pasL.place(x = 30, y  = 240)
	pasE.place(x = 200, y  = 240)
	cifrarB.place(x = 150, y = 290)
	desB.place(x = 300, y = 290)

def mostrarA():
	global aL
	global aE
	global bL
	global bE
	global cifrarBA
	global desBA
	aL.place(x = 30, y  = 240)
	aE.place(x = 110, y  = 240)
	bL.place(x = 180, y  = 240)
	bE.place(x = 280, y  = 240)
	nL.place(x = 330, y = 240)
	nE.place(x = 420, y = 240)
	cifrarBA.place(x = 150, y = 290)
	desBA.place(x = 300, y = 290)

def cifrarV():
	global pasE
	global filename
	textoC = ""
	i = 0
	archivo = open(filename, "rb")
	texto = archivo.read().decode("utf-8")
	llave = pasE.get()
	for n in texto:
		if(i == len(llave)):
			i = 0
		c = (ord(n) + ord(llave[i])) % 256
		textoC = textoC + chr(c)
		i = i + 1
	print(textoC)
	archivoC = open("ElvisC.vig", "wb")
	archivoC.write(bytes(textoC, 'utf-8'))
	archivo.close()
	archivoC.close()
	messagebox.showinfo("Cifrado", "Su archivo ha sido cifrado")

def desV():
	global pasE
	global filename
	textoD = ""
	i = 0
	archivo = open(filename, "rb")
	texto = archivo.read().decode("utf-8")
	llave = pasE.get()
	for n in texto:
		if (i == len(llave)):
			i = 0
		k = 256 - ord(llave[i])
		c = (ord(n) + k) % 256
		textoD = textoD + chr(c)
		i = i + 1
	archivoD = open("ElvisD.txt", "wb")
	archivoD.write(bytes(textoD, 'utf-8'))
	archivo.close()
	archivoD.close()
	messagebox.showinfo("Cifrado", "Su archivo ha sido descifrado")

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		#q es la division ENTERA entre a y b
		#r es el residuo de la division (por eso está como un módulo)
		q, r = b//a, b%a
		#Aqui se aplican las fórmulas del despeje
		m, n = x-u*q, y-v*q
		#b ahora será igual a "a", a ahora será r
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	messagebox.showinfo("Hola", "GCD = " + str(gcd) + " x = " + str(x) + " y = " + str(y))
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return -1 #No existe el inverso porque no son coprimos a y m
	else:
		messagebox.showinfo("Hola 2", "x % m = " + str(x % m))
		return x % m

def cifrarA():
	global aE
	global bE
	global nE
	a = int(aE.get())
	b = int(bE.get())
	n = int(nE.get())
	textoC = ""
	key = [a, b]
	global filename
	archivo = open(filename, "rb")
	texto = archivo.read().decode("utf-8")
	if(modinv(a, n) != -1):
		textoC = ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % n) + ord('A')) for t in texto.upper().replace(' ', '') ])
		print(textoC)
		archivoC = open("SimonC.aff", "wb")
		archivoC.write(bytes(textoC, 'utf-8'))
		archivo.close()
		archivoC.close()
		messagebox.showinfo("Cifrado", "Su archivo ha sido cifrado")
	else:
		messagebox.showinfo("Error", "Numeros no validos")

def desA():
	global aE
	global bE
	global nE
	a = int(aE.get())
	b = int(bE.get())
	n = int(nE.get())
	textoD = ""
	key = [a, b]
	global filename
	archivo = open(filename, "rb")
	texto = archivo.read().decode("utf-8")
	if(modinv(a, n) != -1):
		textoD = ''.join([ chr((( modinv(key[0], n)*(ord(c) - ord('A') - key[1])) % n) + ord('A')) for c in texto ])
		print(textoD)
		archivoD = open("SimonD.txt", "wb")
		archivoD.write(bytes(textoD, 'utf-8'))
		archivo.close()
		archivoD.close()
		messagebox.showinfo("Cifrado", "Su archivo ha sido descifrado")
	else:
		messagebox.showinfo("Error", "Numeros no validos")

ventana.resizable(False, False)
seleccion = IntVar()
frame = Frame()
frame.pack()
frame.config(bg="#f0c0fa")
frame.config(width = "650", height = "450")
frame.config(bd = "20")
frame.config(relief = "ridge")
frame.config(cursor = "heart")
bienL = Label(frame, text = "Cifrador Vigenere y Affine", fg = "purple", font = ("Comic Sans MS", 14), bg = "#f0c0fa").place(x = 150, y  = 20)
vaL = Label(frame, text = "Seleccione el cifrado con el que quiere trabajar", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 70)
vin = Radiobutton(frame, text = "Vigenere", variable = seleccion, value = 1, command = mostrarV, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 90, y = 100)
aff = vin = Radiobutton(frame, text = "Affine", variable = seleccion, value = 2, command = mostrarA, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 240, y = 100)
archL = Label(frame, text = "Seleccionar archivo", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 160)
botonA = Button(frame, text = "Cargar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = archivos).place(x = 200, y = 160)
filename = "No se ha seleccionado ningún archivo"
rutaL = Label(frame, text = filename, fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa").place(x = 30, y  = 200)
pasL = Label(frame, text = "Ingrese su clave:", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa")
pasE = Entry(frame, fg = "#a8588d", font = ("Comic Sans MS", 12))
cifrarB = Button(frame, text = "Cifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = cifrarV)
desB = Button(frame, text = "Descifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = desV)
aL = Label(frame, text = "Ingrese a:", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa")
aE = Entry(frame, fg = "#a8588d", font = ("Comic Sans MS", 12), width = 5)
bL = Label(frame, text = "Ingrese b:", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa")
bE = Entry(frame, fg = "#a8588d", font = ("Comic Sans MS", 12), width = 5)
nL = Label(frame, text = "Ingrese n:", fg = "purple", font = ("Comic Sans MS", 12), bg = "#f0c0fa")
nE = Entry(frame, fg = "#a8588d", font = ("Comic Sans MS", 12), width = 7)
cifrarBA = Button(frame, text = "Cifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = cifrarA)
desBA = Button(frame, text = "Descifrar archivo", fg = "white", font = ("Comic Sans MS", 10), bg = "#ad0dce", command = desA)
ventana.mainloop()
