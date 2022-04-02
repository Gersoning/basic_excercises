def permutador(array,num):
    i = 0
    arraylist=[]
    lista=[]
    while i < num :
        lista=[]
        for n in range(len(array)) :
            if n == 0 :
                if array[n+1] == 0 :
                    z = 0
                    lista.append(z)
                else :
                    z = 1
                    lista.append(z)
            elif n == (len(array)-1) :
                if array[n-1] == 0 :
                    z = 0
                    lista.append(z)
                else :
                    z = 1
                    lista.append(z)
            else :
                if array[n-1] == array[n+1] :
                    z = 0
                    lista.append(z)
                else :
                    z = 1
                    lista.append(z)
        array = lista
        arraylist.append(lista)
        i+=1
    return print(arraylist[num-1])

def mayor(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        x=n1
    elif  n2 >=n1 and n2 >= n3:
        x=n2
    else :
        x=n3
    return print(x)

def par_o_impar(v):
    par=[]
    impar=[]
    for i in v:
        if i % 2 ==0 :
            par.append(i)
        else:
            impar.append(i)
    par.sort()
    impar.sort()
    for i in impar:
        par.append(i)
    lista= str(par)[1:-1]
    print(lista)

def extractor(nombre_empresa):
    objetivos = {"s","o","h"}
    letras=[]
    for i in nombre_empresa:
        if i in objetivos:
            letras.append(i)
    resultados=set(letras) 
    return print(objetivos==resultados)


entrada1 = input("Escriba su array separado por espacios y sin corchetes: ")
entrada2 = int(input("Escriba el número de permutaciones: "))
entrada1=entrada1.split()
entrada1=[int(i) for i in entrada1]
permutador(entrada1,entrada2) 