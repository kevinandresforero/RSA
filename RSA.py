import tkinter as tk
from tkinter import Canvas

marco = tk.Tk()
marco.title("Encriptar con RSA")
marco.geometry("1000x500")

def primo(num):
    for i in range(2,num):
        if  num<23 or num%i == 0:
            return False
    return True
fi = 0
z = 0
s = 0
Desen = []

def Acc():
    Encript = []
    primP = False
    primQ = False
    primN = False
    p = int(entrada1.get())
    n = int(entrada3.get())
    q = int(entrada2.get())
    palabra = str(entrada4.get())
    if not primo(p):
        mostrar1.set("Este número no es primo a mayor a 23")
    else:
        mostrar1.set("")
        primP = True
    if not primo(q):
        mostrar2.set("Este número no es primo a mayor a 23")
    else:
        mostrar2.set("")
        primQ = True
    if not primo(n):
        mostrar3.set("Este número no es primo a mayor a 23")
    else:
        mostrar3.set("")
        primN = True
    if primP and primQ and primN:
        fi = (p-1)*(q-1)
        z = (p*q)
        s = n+1
        while True:
            if (n*s)%fi==1:
                break
            s = s+1
        mostrar6.set(s)
        mostrar7.set(z)
        for i in palabra:
            a = (int(ord(i))**n)%z
            Encript.append(a)
        mostrar4.set(Encript)
def Acc2():
    '''for i in range(len(Desen)):
        b = (int(Desen[i])**(int(mostrar6.get())))%(int(mostrar7.get()))
        Desen[i] = chr(b)
    mostrar5.set(Desen)
    del Desen[:]'''
    palabra = str(entrada4.get())
    for i in palabra:
        Desen.append(i)
    mostrar5.set(Desen)
    del Desen[:]

mostrar1 = tk.StringVar()
mostrar2 = tk.StringVar()
mostrar3 = tk.StringVar()
mostrar4 = tk.StringVar()
mostrar5 = tk.StringVar()
mostrar6 = tk.StringVar()
mostrar7 = tk.StringVar()

l1 = tk.Label(marco, text ="A continución digíte los 3 primos").grid(row=0)
l2 = tk.Label(marco, text ="p = ", fg="red").grid(row=1,sticky=tk.W)
entrada1 = tk.Entry(marco)
entrada1.grid(row=1,column=0)
l3= tk.Label(marco, text ="q = ").grid(row=2,sticky=tk.W)
entrada2= tk.Entry(marco)
entrada2.grid(row=2,column=0)
l4 = tk.Label(marco, text ="n = ").grid(row=3,sticky=tk.W)
entrada3 = tk.Entry(marco)
entrada3.grid(row=3,column=0)
l5 = tk.Label(marco, textvariable = mostrar1).grid(row=1,column=1)
l6 = tk.Label(marco, textvariable = mostrar2).grid(row=2,column=1)
l7 = tk.Label(marco, textvariable = mostrar3).grid(row=3,column=1)
l8 = tk.Label(marco, text ="Palabra a encriptar").grid(row=4,sticky=tk.W)
entrada4 = tk.Entry(marco)
entrada4.grid(row=5,column=0)
l9 = tk.Label(marco, text ="Palabra Encriptada").grid(row=6,sticky=tk.W)
l10 = tk.Label(marco, textvariable = mostrar4).grid(row=7,sticky=tk.W)

l11 = tk.Label(marco, text ="Palabra Desencriptada").grid(row=8,sticky=tk.W)
l12 = tk.Label(marco, textvariable = mostrar5).grid(row=9,sticky=tk.W)

l13 = tk.Label(marco, text ="s = ").grid(row=10,sticky=tk.W)
l14 = tk.Label(marco, textvariable = mostrar6).grid(row=10)

l15 = tk.Label(marco, text ="z = ").grid(row=11,sticky=tk.W)
l16 = tk.Label(marco, textvariable = mostrar7).grid(row=11)

tk.Button(marco, text="Encriptar",command=Acc).grid(row=13,sticky=tk.W)
tk.Button(marco, text="Desencriptar",command=Acc2).grid(row=13)

marco.mainloop()
