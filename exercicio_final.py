"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input("Digite um CPF: ")
dotless_cpf_digito1 = []
soma_digito1 = 0
soma_digito2 = 0

if len(cpf) == 11:
    novo_cpf_digito1 = cpf[0:9]
    dotless_cpf_digito1 = novo_cpf_digito1
elif len(cpf) == 14:
    novo_cpf_digito1 = cpf.split("-")
    dotless_cpf_digito1 = novo_cpf_digito1[0].split(".")
    dotless_cpf_digito1 = dotless_cpf_digito1[0] + dotless_cpf_digito1[1] + dotless_cpf_digito1[2]
    
inicio_digito1 = 10
for item_digito1 in dotless_cpf_digito1:
    soma_digito1 += int(item_digito1) * inicio_digito1
    inicio_digito1 -= 1

mult_digito1 = soma_digito1 * 10
resto_digito1 = mult_digito1 % 11
if resto_digito1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_digito1

print(f"O primeiro digito do CPF: {cpf} é {primeiro_digito}")

cpf_primeiro_digito = str(dotless_cpf_digito1 + str(primeiro_digito))
inicio_digito2 = 11

for item_digito2 in cpf_primeiro_digito:
    soma_digito2 += int(item_digito2) * inicio_digito2
    inicio_digito2 -= 1

mult_digito2 = soma_digito2 * 10
resto_digito2 = mult_digito2 % 11
if resto_digito2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resto_digito2

print(f"O segundo digito do CPF: {cpf} é {segundo_digito}")
print("CPF FINAL: ", str(dotless_cpf_digito1) + "-" + str(primeiro_digito) + str(segundo_digito))
