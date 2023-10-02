"""
Escopo de função 
Escopo significa o local onde o código pode atingir.
Existe o escopo global e local.
Global é o escopo onde todo o código é alcançável 
local é o escopo onde apenas nomes do mesmo local podem alcançar
"""
x = 1

def escopo():
    def outra_funcao():
        y = 2
        print(x, y)
    outra_funcao()
    print(x)


escopo()


