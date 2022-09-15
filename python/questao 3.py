#atividade da lista de exercícios 2

x = int(input('digite um número aleatorio: '))

if ((x > 0) and (x%2 == 0)) :
    print ('o número digitado é positivo e par')
    
elif (x < 0 and x%2 == 0) :
    print ('o número digitado é negativo e par')
    
elif (x > 0 and x%2 == 1) :
    print ('o número digitado é positivo e impar')
    
elif (x < 0 and x%2 == 1) :
    print ('o número digitado é negativo e impar')