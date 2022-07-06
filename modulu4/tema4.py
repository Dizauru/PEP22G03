#problema 1
def calcul(x):
     y=3*x
     return  3*x**2-4*y+4
n=0
x=range(10,21)
z=[]
for i in x:
    rezultat= calcul(i)
    z.append(rezultat)
for x in range(10,21):
    if n <= 10:
       n += 1
       print (f"""==== x = {x}'=== /n Solutia ecuatiei este:""" ,z[n])





# nr=input("Cate carti doriti sa adaugati in biblioteca: ")
# lista_nume= []
# lista_autor=[]
# lista_an= []
# carte={}
# for i in range(int(nr)):
#     nume_carte= input("numele cartii este :")
#     an_publicatie= input("anul publicarii este :")
#     nume_autor=input("numele autorului este ")
#     lista_nume.append(nume_carte)
#     lista_autor.append(nume_autor)
#     lista_an.append(an_publicatie)
#
# for i in range(int(nr)):
#
#     print(f"cartea{i+1} ")
#     print(f"numele cartii {i+1}: {lista_nume[i]}")
#     print(f"numele autorului {i+1}: {lista_autor[i]}")
#     print(f"anul publicatiei {i+1}: {lista_an[i]}")
#
# for i in range(len(lista_nume)):
#     carte['nume'] = lista_nume[i]
#     carte['autor'] = lista_autor[i]
#     carte['an'] = lista_an[i]
#     print(carte)
