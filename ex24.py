print('___Sobre: Verificando as Primeiras Letras de um Texto___')

while True:
    
    cidade = input('\nEm que cidade você nasceu? ')
    alfabetico = False
    cidade = cidade.split()
    #'valorLogico', variavel criada pois, o valor da -var- 'alfabetico' nao é preciso, quero dizer, ele é atualizado, dentro do -for-
    
    for elementos in cidade:
        alfabetico = elementos.isalpha()
        if alfabetico == False:
            valorLogico = False
        else:
            valorLogico = True
    
    if valorLogico == True:
        
        if cidade[0].lower() == 'santo':
            print(True)
        else:
            print(False)
        break
    else:
        print('Dado incorreto, digite somente texto!')