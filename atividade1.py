print("Digite seu nome: ")
nome = str(input())
print("Digite sua idade: ")
idade = int(input())
print("Digite sua altura (em cm): ")
altura_cm = float(input())
print("Digite sua cidade: ")
cidade = str(input())
print("Digite sua profissão: ")
profissao = str(input())

altura_m = altura_cm / 100

print("Olá, meu nome é %s, tenho %d anos, minha altura é %.2f m, moro em %s, e trabalho com %s." % (nome, idade, altura_m, cidade, profissao))