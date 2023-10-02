"""
Escopo significa o local onde o código pode atingir.
Existe o escopo global e local.
Local é o escopo onde apenas nomes do mesmo local podem alcançar.
"""
from re import X


x = 1

def escopo():
    global x
    y = 2
    print (x, y)
    
    def outra_funcao():
       global x
       y = 2
       print (x, y)

    outra_funcao()
    print (x)

    print(x)
    escopo()
    print(x)