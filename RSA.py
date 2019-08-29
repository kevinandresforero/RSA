import  tkinter as tk

'''
marco = tk.Tk()
marco.title('Encriptación SRA')
marco.configure(background='#000000')
marco.geometry('400x400')
marco.mainloop()
'''''

class rca:

    _tex = (" tu y yo <3 ")
    _p = int(input(" digite un Primo"))
    _q = 2
    _n = 3
    primo = False
    a =[_p, _q , _n]
    aprimo = [False,False,False]
    for j in range (len(aprimo)):
        while(aprimo[j] == False):
            for i in range (len(a)):
                a[i] = int(input(" digite un Primo"))
                if(a[i] < 2):
                    print("no Valido")
                else:
                    if (_p == 2 ):
                        aprimo[j] = True
                        print(" Es Primo ")
                    else:
                        x = 2
                        while(x < _p):
                            if(_p % x == 0):
                                print(" No es Primo ")
                                break
                            else:
                                if(x==_p-1):
                                        aprimo[j] = True
                                        print(" Es Primo ")
                                x = x+1

    _fi = (_p-1)*(_q-1)
    _z = _p * _q
    _Cp = _n+1

    #Generando la clave publica

    while((_n*_Cp)%_fi != 1):
        _Cp = _Cp + 1
    print(" Cp = "+str(_Cp))
    print(" z = "+str(_z))
    _lTex = _tex

    for i in range (len(_lTex)):
        print("   "+str(_lTex[i])+"   =   "+str((ord(_lTex[i]) ** _n) % _z))
