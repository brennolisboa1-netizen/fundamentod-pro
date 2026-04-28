# crie um sistema aonde o valor inicial é de R$1000 e o usuário consiga realizar um saque e ao finalnseja exibido o valor do saldo

saldo = 1000
while saldo > 0:
    saque =float(input("Digite o valor do saque"))
    saldo-= saque # saldo = saldo - saque
    print(f"saldo restante: {saldo}")