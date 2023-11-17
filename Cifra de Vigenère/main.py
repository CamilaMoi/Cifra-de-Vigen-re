def ordenacao_lista(lista):
    if len(lista)<=1:
        return lista
    
    primeira_letra_aux=lista[0]

    for i in range(1, len(lista)):
        lista[i-1]=lista[i]
    
    lista[-1]=primeira_letra_aux

    return lista

def substituir_letras(frase, palavra_substituta):
    resultado = []
    indice_palavra = 0

    for caractere in frase:
        if caractere.isalpha():
            resultado.append(palavra_substituta[indice_palavra % len(palavra_substituta)])
            indice_palavra += 1
        else:
            resultado.append(caractere)

    return ''.join(resultado)


alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g','h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y', 'z']
matriz_vigenere= []
palavra_encriptada=[]
lista_coord=[]
tupla_indexacao=[]
result=alfabeto

for i in range(1, 26):
    linha = []
    for j in range(0, 26):
        linha.append(result[j])
    result=ordenacao_lista(result)
    matriz_vigenere.append(linha)

'''for i in range(1, 26):
    for j in range(0, 26):
        print(matriz_vigenere[i-1][j], end = " ", sep = " ")
    print()'''


frase=str(input('digite a frase que deseja encriptar: '))
lista_frase=list(frase)
palavra_chave=str(input('digite a palavra chave para : '))
lista_palavra_chave=list(palavra_chave)

palavra_lista_teste=list(substituir_letras(frase, palavra_chave))

tupla_subst=list(zip(lista_frase, palavra_lista_teste))
#print(tupla_subst)

for i in range(0, len(palavra_lista_teste)):
    for j in range(0, 2):
        for k in range(0, 26):
            if tupla_subst[i][j]==alfabeto[k]:
                lista_coord.append(k)

#print(lista_coord)

for i in range(0, len(lista_coord), 2):
    posicaoi=lista_coord[i]
    posicaoj=lista_coord[i+1]
    palavra_encriptada.append(matriz_vigenere[posicaoi-1][posicaoj-1])

palavra_final=str(palavra_encriptada)

print("A palavra encriptada é ", palavra_final)



