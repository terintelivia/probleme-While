n=1
nr=0
suma_n=0
suma_p=0
np=0
nn=0
while n<=12:
    nr=eval(input("Introdu temperatura: "))
    if nr>=0:
        suma_p+=nr
        np+=1
    else:
        suma_n+=nr
        nn+=1
    n+=1
print("Media anuala a temperaturilor pozitive este  ",suma_p/np)
print("Media anuala a temperaturilor negative este  ",suma_n/nn)