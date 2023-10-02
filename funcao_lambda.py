#Função lambda em Python
#A função lambda é uma função.
#como qualquer outra em Python. Porém são funções anônimas, que contém apenas uma linha.
#Ou seja, tudo deve ficar dentro de uma única expressão.
#lista = [
#{'nome': 'André', 'sobrenome': 'Estevam'},
#{'nome': 'Maria', 'sobrenome': 'Ari'},
#{'nome': 'Cuca', 'sobrenome': 'Beludo'},
#{'nome': 'Paula', 'sobrenome': 'Texando'},
#{'nome': 'Thomas', 'sobrenome': 'Turbando'},
#{'nome': 'Mico', 'sobrenome': 'Meu'},
#{'nome': 'Sal', 'sobrenome': 'Sicha'},


#]

#lista = [4, 32, 1, 34, 5, 6, 6, 21]
#lista.sort(reverse = True)
#sorted(lista)
#print(lista)

lista = [
    {'nome': 'André', 'sobrenome': 'Estevam'},
    {'nome': 'Maria', 'sobrenome': 'Ari'},
    {'nome': 'Cuca', 'sobrenome': 'Beludo'},
    {'nome': 'Paula', 'sobrenome': 'Texando'},
    {'nome': 'Thomas', 'sobrenome': 'Turbando'},
    {'nome': 'Mico', 'sobrenome': 'Meu'},
    {'nome': 'Sal', 'sobrenome': 'Sicha'},

]
def orderna(item):
    print(item)
    return item

lista.sort(key=orderna)
print(lista)

