senha_correta = "python123"
tentativa_senha = 0
while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
            print("Senha correta! Acesso concedido.")
            break

    tentativa_senha+=1
    if (tentativa_senha < 3):
        print("Senha incorreta. Tente novamente.")
    else:
        print("Acesso bloqueado!")
        break