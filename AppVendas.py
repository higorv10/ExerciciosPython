print("Bem Vindo a Lanchonete do Higor Vilela") #RU4114211
print("***************Cardápio***************")
print("| Código |     Descrição             | Valor |")
print("|   100  |   Cachorro Quente         |  9,00 |")
print("|   101  | Cachorro Quente Duplo     | 11,00 |")
print("|   102  |         X_Egg             | 12,00 |")
print("|   103  |        X-Salada           | 13,00 |")
print("|   104  |         X-Bacon           | 14,00 |")
print("|   105  |         X-Tudo            | 17,00 |")
print("|   200  |   Refrigerante Lata       |  5,00 |")
print("|   201  |      Chá Gelado           |  4,00 |")
pedindo = True
codigo = 0
resposta = ""
total = 0.
vefCodigo = True
while pedindo == True:
   while vefCodigo == True:
       codigo = input("Entre com o código desejado: ")
       if codigo == '100':
           print("Você pediu Cachorro Quente no valor de R$9,00")
           total = total + 9.00
           vefCodigo = False
       elif codigo == '101':
           print("Você pediu um Cachorro Quente Duplo no valor de R$11,00")
           total = total + 11
           vefCodigo = False
       elif codigo == '102':
           print("Você pediu um X-Egg no valor R$12,00")
           total = total + 12
           vefCodigo = False
       elif codigo == '103':
           print("Você pediu um X-Salada no valor de R$13,00")
           total = total + 13
           vefCodigo = False
       elif codigo == '104':
           print("Você pediu um X-Bacon no valor de R$14,00")
           total = total + 14
           vefCodigo = False
       elif codigo == '105':
           print("Você pediu um X-Tudo no valor de R$17,00")
           total = total + 17
           vefCodigo = False
       elif codigo == '200':
           print("você pediu um Refrigerante Lata no valor de R$5,00")
           total = total + 5
           vefCodigo = False
       elif codigo == '201':
           print("você pediu um Chá Gelado no valor de R$4,00")
           total = total + 4
       else:
           print("Opção Inválida!")
           continue
   resposta = input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n>>')
   if resposta == "1":
       vefCodigo = True
   else:
       print("O total a ser pago é:",total)
       break