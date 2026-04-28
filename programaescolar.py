print("sistema escolar ")

# entrada de dados 
idade = int(input("Informe a idade: ")) 
print("sistema de emprestimo bancário")

nota = float(input("Informe a nota: "))
frequencia = int(input("Informe a sua sequencia em meses: "))

## estruturas condicionais 
if idade < 18:
    print ("matricula negada, estudante menor de idade. ")
elif nota >= 9:
    print ("matricula aprovado automaticamente. ")
elif idade >= 18 and nota >= 9:
    print ("matricula aprovada. ")

    # verificar a idade, e a nota
    