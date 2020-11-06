Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
suma_nr=0
produs_nr=1
nr=1
n=eval(input("n= "))
while nr<=n:
    suma_nr+=nr
    produs_nr*=nr
    nr+=1
print("suma numerelor este egala cu : ", suma_nr)
print("produsul numerelor este egal cu : ", produs_nr)
print("media aritmetica a numerelor este egala cu : ", suma_nr/n)