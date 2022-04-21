from tkinter import messagebox

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
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return -1 #No existe el inverso porque no son coprimos a y m
	else:
		return x % m

a = int(input("Introduce alfa\n"))
b = int(input("Introduce beta\n"))
n = int(input("Introduce n\n"))

if(modinv(a, n) == -1):
    messagebox.showinfo("Error", "Alfa no es válido, introduce otro pls")

if(b > n):
    b = b%n
    messagebox.showinfo("Regreso del anillo", "El valor de beta dentro del anillo es: " + str(b))
    messagebox.showinfo("Resultado", "C = " + str(a) + " +" + str(b) + "mod" + str(n))
    messagebox.showinfo("Inverso", "El inverso multiplicativo de " + str(a) + " es " + str(modinv(a, n)))
    messagebox.showinfo("Inverso aditivo", "El inverso aditivo es: " + str(n - (b%n)))
else:
    messagebox.showinfo("Resultado", "C = " + str(a) + " +" + str(b) + "mod" + str(n))
    messagebox.showinfo("Inverso", "El inverso multiplicativo de " + str(a) + " es " + str(modinv(a, n)))
    messagebox.showinfo("Inverso aditivo", "El inverso aditivo es: " + str(n - (b%n)))