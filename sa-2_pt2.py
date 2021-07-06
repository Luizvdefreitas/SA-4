# 3)

y = list(range(1,21))

med = sum(y) / len(y)

print(med)

print("maior número é: ", max(y))
print("menor número é: ", min(y))

print(y)

# 4)
def tamanho_linha(tam):

    linha = '_'
    print(tam * linha)
    
tamanho_linha(50)

# 5)

def tamanho_linha(l):

    for x in l:
        print(x)
    
lista = [2,4,6,10]

    
tamanho_linha(lista)

# 6)

pergunta = int(input("Digite a quantidade de horas que deseja converter em segundos:"))


horas_segundos = pergunta * (3600)

if pergunta < 2:

    print("R:", pergunta, "hora tem", horas_segundos, "segundos")

else:
    print("R:", pergunta, "horas tem", horas_segundos, "segundos")

# 7)
print(" *")
print(" * *\n" * 3) 
print("*** ***")
print("* *\n" * 2)
print(" *****")



 