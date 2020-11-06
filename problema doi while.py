Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
n=1
nr=0
suma_n=0
suma_p=0
np=0
nn=0
while n<=12:
    nr=eval(input("introdu temperatura: "))
    if nr>=0:
        suma_p+=nr
        np+=1
    else:
        suma_n+=nr
        nn+=1
    n+=1
print("media anuala a temperaturilor pozitive este  ", suma_p/np)
print("media anuala a temperaturilor negative este  ", suma_n/nn)