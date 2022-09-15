a = int(input('Escreva um número inteiro: '))
b = int(input('Escreva um número inteiro: '))
c = int(input('Escreva outro número inteiro: '))

if (a>b and a>c):
    print ('Os valores digitados foram {}, {} e {}. {} é o maior deles'. format(a, b, c, a))
    
elif (b>a and b>c) :
    print ('Os valores digitados foram {}, {} e {}. {} é o maior deles'. format(a, b, c, b))
           
else :
    print ('Os valores digitados foram {}, {} e {}. {} é o maior deles'. format(a, b, c, c))