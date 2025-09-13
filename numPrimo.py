print ("Entre com um número: ")
num = int(input())
flag = True
dvd = 2

while dvd<=num / 2:
    if num % dvd == 0:
        flag = False
        break
    dvd +=1

if flag:
    print (f"{num} é primo")
else:
    print (f"{num} não é primo")