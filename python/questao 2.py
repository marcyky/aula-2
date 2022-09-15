#atividade da lista de exercícios 2

idade = int(input('Informe sua idade: '))

if (5 <= idade <= 7) :
    print ('infantil A')
    
elif (8 <= idade <= 10) :
    print ('infantil B')
    
elif (11 <= idade <= 13) :
    print ('juvenil A')
    
elif (14 <= idade <= 17) :
    print ('juvenil B')
    
elif (idade >= 18) :
    print ('adulto')
    
elif (idade < 5) :
    print ('não pode competir')