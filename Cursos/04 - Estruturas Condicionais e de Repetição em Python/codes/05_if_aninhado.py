conta_simples = False
conta_universitaria = False

saldo = 3000
saque = 3500
cheque_especial = 450


if conta_simples:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")   
    else:
        print("Não foi possível realizar a transação!")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print("O Sistema não reconheceu o tipo de sua conta! Tente novamente ou entre contato com o seu gerente!")