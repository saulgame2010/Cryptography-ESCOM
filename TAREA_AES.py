# -*- coding: utf-8 -*-
totalCombinaciones = pow(2,128)
print(f'El algoritmo AES tiene {totalCombinaciones} llaves posibles para una llave de longitud 128 bits\n')
sieteDias = 60*60*24*7 #7 días en segundos
valocidadProcesador = 0.000000001
combinacionesPorDia = double(totalCombinaciones/sieteDias)

print('Es decir, en un dia un solo procesador puede intentar {} combinaciones\n')
