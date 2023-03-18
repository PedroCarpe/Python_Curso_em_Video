#Referências de palavras
#https://www.normaculta.com.br/palavras-com-acento-grave/
#https://www.normaculta.com.br/palavras-com-acento-circunflexo/
#https://www.normaculta.com.br/palavras-com-acento-agudo/

print('___Procurando Letra em uma Frase___')


frase = input('Digite uma frase: ')

texto = 'a A ã â Â à À á Á'.split()

contador_letras = 0
for letras in texto:
    contador_letras += frase.count(letras)


primeira_letra_a = ''
boleana = False

for letras in frase:
    
    if boleana == True:
        break
    for letras_a in texto:
        
        #print(f'{letras} {letras_a}')
        if letras == letras_a:
            primeira_letra_a = frase.find(letras) + 1
            #print(f'Aqui {letras} {letras_a}')
            boleana = True
            break
        

###################
ultima_letra_a = ''
for letras in frase:
    
    for letras_a in texto:
        
        #print(f'{letras} {letras_a}')
        if letras == letras_a:
            ultima_letra_a = frase.rfind(letras) + 1
            #print(f'Aqui {letras} {letras_a}')


        
print(f'\nA letra -A- apareceu {contador_letras}x na frase.')
print(f'1ª letra -A- na posição: {primeira_letra_a}')
print(f'Enésima letra -A- na posição: {ultima_letra_a}')
