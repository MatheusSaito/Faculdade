print ("Informe um número: ")
num = int (input())
i = 1

print ("====OPÇÕES====")
print ("1. Adição")
print ("2. Subtração")
print ("3. Divisão")
opcao = int (input())

match opcao:
    case 1:
        while i <= 10:
            result = num + i
            print (num, "+", i, "=", result)
            i = i+1
    case 2:
         while i <= 10:
            result = num - i
            print (num, "-", i, "=", result)
            i = i+1
    case 3:
         while i <= 10:
            result = num / i
            print (num, "/", i, "=", result)
            i = i+1
    case _:
        print ("Opção inválida!")