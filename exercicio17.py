#compra de tinta otimizada pela tinta

import math
area_a_ser_pintada = int(input('Entre com a área a ser pintada: '))
area_com_folga = area_a_ser_pintada * 1.1
litros_a_serem_usados = area_com_folga/6

litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados/litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80

litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados/litros_por_galao)
valor_com_apenas_galoes = numero_de_galoes*25

#compra de tinta otimizada pelo valor
numero_de_latas = math.floor(litros_a_serem_usados/litros_por_lata)
valor_de_latas = numero_de_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_de_galoes = math.ceil(litros_faltantes/litros_por_galao)
valor_com_galoes = numero_de_galoes * 25

valor_total = valor_de_latas + valor_com_galoes

print(f'''Você poderá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas} ou
você poderá usar {numero_de_galoes} de galões de 3,6 litros, no valor de R$ {valor_com_apenas_galoes} ou
você poderá  usar {numero_de_latas} latas de 18 litros mais {numero_de_galoes} galões de 3,6 litros, no valor de R$ {valor_total}.''')