#Atividade numero 1
L = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista;
tamanho = len(L)

print("A lista possui", tamanho, "números")

# b) maior valor da lista;
maior = max(L)

print("O maior número é: ", maior)

# c) menor valor da lista;
menor = min(L)

print("O menor número é: ", menor)

# d) soma de todos os elementos da lista;
soma = sum(L)

print("A soma de todos os números é igual a:",soma)


# e) lista em ordem crescente;
L.sort()
print(L)

# f) lista em ordem decrescente.

L.sort(reverse=True)
print(L)

# 2) 
x = [1,2,-3,-4]

med = sum(x) / len(x)

print("A média é igual a:", med)

if med > 0:
    print("A média é um número positivo")

else:
    print("A média é um número negativo") 