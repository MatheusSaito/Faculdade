nome = 'Matheus'
sobrenome = 'Saito'
diaNasc = 22
mesNasc = 1
anoNasc = 2006
compra1 = 'Chocolate'
qtde1 = 3
preco1 = 5.50
compra2 = 'Refrigerante'
qtde2 = 4
preco2 = 6.40
compra3 = 'Salgadinho'
qtde3 = 5
preco3 = 2.30
total1 = preco1 * qtde1
total2 = preco2 * qtde2
total3 = preco3 * qtde3

print("{nome} {sobrenome} nascido em {diaNasc}/{mesNasc:02d}/{anoNasc} fez as seguintes compras: ".format(
    nome=nome, sobrenome=sobrenome, diaNasc=diaNasc, mesNasc=mesNasc, anoNasc=anoNasc))

print(f"{'Produto':10} {'Quantidade':20} {'Preço':10} {'Total':10}")
print("{0:10} {1:>10} {2:15.2f} {3:10.2f}".format(compra1, qtde1, preco1, total1))
print("{0:10} {1:>8} {2:15.2f} {3:10.2f}".format(compra2, qtde2, preco2, total2))
print("{0:10} {1:>10} {2:15.2f} {3:10.2f}".format(compra3, qtde3, preco3, total3))


