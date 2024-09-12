MINUTOS= float(input('Ingrese el total de minutos trabajados en un dia'))
VALOR= float(input('Ingrese el valor del costo de una hora'))
DIAS= float (input('Ingrese la cantidad de dias trabajados'))
OPERACION1= MINUTOS/60
OPERACION2= OPERACION1*VALOR
OPERACION3= OPERACION2*DIAS
print ('El sueldo mensual es: ')
print (OPERACION3)
