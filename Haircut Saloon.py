#Haircut Saloon

tamanho_cabelo = 28

if tamanho_cabelo <= 20:
    print('o corte custa R$ 50,00') 
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('o corte custa R$ 70,00')
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print('o corte custa R$ 100,00')
else :
    print('consultar a recepção')