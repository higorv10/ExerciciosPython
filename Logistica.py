def dimensoesObjeto():
    while True:
     try:
        dms1 = int(input('Digite o comprimento do objeto (em cm):'))
        dms2 = int(input('Digite a largura do objeto (em cm):'))
        dms3 = int(input('Digite a altura do objeto (em cm):'))
        mult = float(dms1 * dms2 * dms3)
        x = mult
        print ('Volume do objeto é (em cm³): {}'.format(x))
        if(x <= 1000):
          return 10.00
        elif(x >= 1001) and (x < 10000):
          return 20.00
        elif(x >= 10001) and (x < 30000):
          return 30.00
        elif(x >= 30001) and (x < 100000):
          return 50.00
        else:
            print('Não aceitamos objetos tão grandes \nentre com as dimensões desejadas novamente')
            continue
     except ValueError:
        print('Você digitou alguma dimansão do objeto com valor não numérico \nPor favor entre com as dimensões desejadas novamente')
        continue


def pesoObjeto():
    while True:
     try:
        peso =float(input('Digite o peso do objeto (em kg):'))
        y = peso
        if(y <= 0.1):
         return 1
        elif(y <= 1) and (y >= 0.11):
         return 1.5
        elif(y <= 10) and (y >= 1.10):
         return 2
        elif(y <= 30) and (y >= 10.1):
         return 3
        else:
            print('Não aceitamos objetos tão pesados')
            continue
     except ValueError:
       print('Você digitou peso do objeto com valor não numérico \nPor favor entre com o peso desejado novamente')
       continue

def rotaObjeto():
    while True:
     try:
        rota = (input('Selecione a rota: \nBR - De Brasília para Rio de Janeiro\nBS - De Brasília para São Paulo\nRB - De Rio de Janeiro para Brasília\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\nSB - De São Paulo para Brasília\n>>'))
        r = rota
        if(r == 'RS'):
         return 1
        elif(r == 'SR'):
         return 1
        elif(r == 'BS'):
         return 1.2
        elif(r == 'SB'):
         return 1.2
        elif (r == 'BR'):
            return 1.5
        elif (r == 'RB'):
            return 1.5
        else:
            print('Você digitou uma rota que não existe')
            continue
     except ValueError:
       print('Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente')
       continue

print('Bem vindo a companhia de logistica Higor Vilela') #RU4114211
dim = dimensoesObjeto()
peso = pesoObjeto()
rot = rotaObjeto()
print('Total a pagar(R$): {:.2f} (Dimensões: {} * Peso: {} * Rota: {})'.format(dim*peso*rot,dim,peso,rot))