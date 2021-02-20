#!/usr/bin/env python3 
#Autor: LorenaMtz
print("Ingrese sus calificaciones")
calif1 = int(input("Primer Examen: "))
calif2 = int(input("Segundo Examen: "))
calif3 = int(input("Tercer Examen: "))

sum = ((calif1+calif2+calif3)//3)
print("Promedio: ",sum)
if (sum >= 70):
	print("Aprobado")
else:
	print("Reprobado")