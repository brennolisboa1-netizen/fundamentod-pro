print("sistema de emprestimo bancário")

# Entrada de dados
idade = int(input("Informe a idade: ")) 
salario = float(input("Informe o salário R$: "))
tempo_trabalho = int(input("Informe o seu tempo de trabalho em meses: "))

## estruturas condicionais 
if idade < 18:
    print ("Empréstimo negado, cliente menor de idade. ")
elif salario >= 5000:
    print ("Emprestimo aprovado automaticamente. ")
elif idade >= 18 and salario >= 2000 and tempo_trabalho >=2:
    print ("Empréstimo aprovado. ")
else: 
    print("Empréstimo negado. ")
    # verificar a idade, o salário e o tempo de trabalho
    