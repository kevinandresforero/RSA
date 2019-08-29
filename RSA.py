
class rca:
    tex = ("Gonorrea Ome Gonorrea")
    _p = 23
    _q = 31
    _n = 29
    _fi = (_p-1)*(_q-1)
    _z = _p * _q
    _Cp = _n+1

    #Generando la clave publica

    while((_n*_Cp)%_fi != 1):
        _Cp = _Cp + 1
    print(_Cp)
    print(_z)
    _lTex = tex

    for i in range (len(_lTex)):
        ord(_lTex[i])


