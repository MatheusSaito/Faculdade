print("Digite um número de quatro dígitos: ")
n = int(input())
u = n % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = n // 1000
print("unidade", u)
print("dezena", d)
print("centena", c)
print("milhar", m)