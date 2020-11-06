Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
nr=0
suma_p=0
while ((nr%3!=0) or (nr%2==0)):
    nr=eval(input("introdu numarul: "))
    if nr%2==0:
        suma_p+=nr
print("suma numerelor pare este egala cu ", suma_p)