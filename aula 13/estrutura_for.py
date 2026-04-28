# contar de 1 até 5 -
for numero in range(1,6):
 #   print(f"Eu sou o número {número}" )

# exemplos de tabuada -> 5
 resultado = 5 # variável no escopo global
for número in range (1,11):
    resultado = numero * número # variável no escopo local 
    print(f"5 x {número} = {resultado}")
                             