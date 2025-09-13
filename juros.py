print ("Qual o valor do depósito inicial? ")
dep_inicial = float (input())
print ("Agora, me informe a taxa de juros: ")
taxa_juros = float (input())
print ("Agora, me informe o prazo (em meses): ")
prazo = int (input())

saldo = dep_inicial
mes = 1

while mes <= prazo:
    print(f"Digite o valor de depósito do mes {mes}: ")
    deposito_mes = float(input())
    saldo+=deposito_mes
    saldo = saldo + (saldo * (taxa_juros / 100))
    mes = mes+1

saldo_mes = saldo - dep_inicial
print(f"Saldo mês {mes} é igual a: {saldo:.2f}")
print (f"O ganho obtido com os juros foi de R${saldo_mes:.2f}")