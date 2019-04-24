# print ('Olá Aluno')

# nota1 = float (input ('Me informe sua primeira nota: '))
# nota2 = float(input ('Me informe sua segunda nota: '))
# nota3 = float(input ('Me informe sua terceira nota: '))

# media = (nota1 + nota2 + nota3) / 3.0

#print ('Sua média foi de {}'.format(round(media, 2)))
# if media == 10:
#     print ('aprovado, Parabéns')
# elif media >= 6:
#     print ('Passoui raspando')
# else:
#     print ('Pode chorar, pegou dp')


# tempoC = int(input ('Qual a temperatura em Celsus que deseja converter em  '))

# tempoF = float((tempoC *(9/5) + 32))

# print(f'{tempoC} em celsius equivalem a {tempoF} em f')

# import math

# exponencial = math.exp (3)

# print (exponencial)


# def calcular_pagamento (qtd_horas, valor_hora):
#     horas = float(qtd_horas)
#     dinheiro = float(valor_hora)
#     if horas >= 40: 
#         salario = horas *dinheiro
#     else
#         salario = 0
#         print('voce não recebe nada')
#     return salário
    

# salario = calcular_pagamento (40, 43.0)
# print (salario)




 #JOGO - DETETIVE
print ('detetive')
print ('responda as perguntas abaixo com S(sim) ou N(não): ')

perguntas=( 'Voce telefonou para a vitima?',  
            'Voce esqteve no local do crime?',
            'Voce era vizinha da vitima?',
            'Voce tinha crush na vitima?',
            'Voce é o mordomo?',
            'Voce devia dinheiro para vitima?')

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta).upper())


tipo = 0
for resposta in respostas:
    if resposta == 'S':
        tipo += 1

if tipo < 2:
        print('inocente')
elif tipo == 2:
        print ('acho que voce matou') 
elif tipo <= 4:
        print ('voce deve ter participado do assassinato')
else:
        print ('voce é o mordomo então vc matou')




# JOGO DO CANSAÇO MENTAL
# def soma (valor1, valor2):
#     return valor1 + valor2

# valor1= int(input('informe o valor: '))
# valor2= int(input('informe o valor: '))

# print(f'A soma dos valores e {soma(valor1,valor2)} ')






    




















