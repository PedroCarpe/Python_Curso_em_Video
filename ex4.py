#Esses métodos, parecem ser úteis para validação de 'entradas'
entrada = input('Digite algo: ')

print(f'\nTipo primitivo: {type(entrada)}')
print(f'É um número: {entrada.isnumeric()}\nCaracteres Alfanuméricos: {entrada.isalnum()}\nOs caracteres são imprimíveis: {entrada.isprintable()}\nÉ um dígito: {entrada.isdigit()}\nNúmero decimal(sitema numérico): {entrada.isdecimal()}\nÉ um identificador: {entrada.isidentifier()}\nOs caracteres minúsculos: {entrada.islower()}\nEspaço em branco: {entrada.isspace()}')
