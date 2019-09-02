import  tkinter as tk
from tkinter import Canvas

def es_primo(numero_leido):

    verificar= False
    numero = int(numero_leido)
    contador = 0
    verificar= False
    for i in range(1,numero+1):
        if (numero% i)==0:
           contador = contador + 1
        if contador >= 3:
            verificar=True
            break

    if contador==2 or verificar==False:
        print ("El numero es primo")
        primo = True
        return primo

    else:
        print ("El numero no es primo")
        primo = False
        return primo

class rca:

    marco = tk.Tk()
    marco.title('Encriptación en SRA')
    marco.configure(background='#000000')
    marco.geometry('550x300')
    marco.resizable(False,False)


    lTitle = tk.Label(marco, text="Complete los Siguientes Campos", fg="yellow" ,bg ="black").grid(row=0,column=0)
    lText = tk.Label(marco, text="El Texto a Codificar", fg="yellow" ,bg ="black").grid(row=1,column=1)
    lp = tk.Label(marco, text="El Primer Número Primo", fg="yellow" ,bg ="black").grid(row=3,column=1)
    lq = tk.Label(marco, text="El Segundo Número Primo", fg="blue" ,bg ="black").grid(row=4,column=1)
    ln = tk.Label(marco, text="El Tercer Número Primo", fg="red" ,bg ="black").grid(row=5,column=1)

    cText = tk.Entry(marco).grid(row=1,column=2)
    cP = tk.Entry(marco).grid(row=3,column=2)
    cQ = tk.Entry(marco).grid(row=4,column=2)
    cN = tk.Entry(marco).grid(row=5,column=2)

    codificar = tk.Button(marco, text = "Codificar" , bg = "black" , fg = "blue").grid(row=4,column=0)

    marco.mainloop()

    print(str(cP)+" "+str(cQ)+" "+str(cN))

    primo = False

    while(primo == False):
        aux = 0
        _p = int(cP.get())
        print(cP)
        if(es_primo(_p) == True):
            aux = aux + 1
        _q = int(cQ.get())
        if(es_primo(_q) == True):
            aux = aux + 1
        _n = int(cN.get())
        if(es_primo(_p) == True):
            aux = aux +1
        if(aux >= 3):
            primo = True

    _fi = (_p-1)*(_q-1)
    _z = _p * _q
    _Cp = _n+1


    marco.mainloop()

    #Generando la clave publica


    while((_n*_Cp)%_fi != 1):
        _Cp = _Cp + 1

    _lTex = cText.get()
    encript = []
    dencript = []

    print(" Cp = "+str(_Cp))
    print(" z = "+str(_z))

    for i in range (len(_lTex)):
        encript.append(((ord(_lTex[i])) ** _n) % (_z))
        dencript.append((encript[i]**_Cp) % _z)
        print(str(ord(_lTex[i]))+"  :   "+str(encript[i])+" :   "+str((dencript[i])))
