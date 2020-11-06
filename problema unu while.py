Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse. Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
s=0
n=eval(input("introdu numarul : "))
while n!=0:
    s+=n
    n=eval(input("introdu numarul : "))
print("suma acestor numere este egala cu " ,s)