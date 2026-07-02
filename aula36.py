# function round() - arredonda o número para o inteiro mais próximo
# para calculos complexos utilizase a precisão decimal com decimal.Decimal
import decimal
number_1 = decimal.Decimal(1.47)
number_2 = decimal.Decimal(3.34)
number_correct = number_1 + number_2
# ao invés de usar - aqui retorna string (texto)
print(f'{number_correct:.15f}')
print(round(number_correct, 2)) # aqui retorna float (numero) (number)