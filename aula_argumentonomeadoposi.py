def minha_func(a, b, c):
    print(a, b, c)

# invocando a função minha_func() passando valores de forma posicional
minha_func(1, 2, 3)
# invocando a função minha_func() passando valores de forma chave-valor(nomeado)
minha_func(a = 1, b = 2, c = 3)
# invocando a função minha_func() passando valores de forma chave-valor, porém fora de ordem(nomeado)
minha_func(a = 1, c = 3, b = 2)