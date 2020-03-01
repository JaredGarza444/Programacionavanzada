#En este programa se estableceran funciones que 
#Permitiran preguntas datos sin ninguna validacion 

import datetime 
#Los datos otorgados pueden ser de diferente tipo
def main():
 Datostring=input ("Dame un dato tipo string:")
 #Los datos string no es necesario procesarlos 
 #Ya que todos los datos otrogados por el usuario 
 #Son del tipo string 
 Datosint=input ("Dame un dato de tipo entero:")
 Datosint=int(Datosint)
 #Los datos tipo int son dats enteros de tipo numerico
 Datosfloat = input("Dame un dato float: ")
 Datosfloat =float(Datosfloat)
 #Los datos del tipo float son datos numericos pero a 
 #Diferencia de los enteros poessen decimales 
 Datosdate=input ("Dame una fecha yyy/mm/dd:")
 #Este tipo de datos se refieren a  fechas 

 año=Datosdate[0:4]
 mes=Datosdate[5:7]
 dia=Datosdate[-2:]
 #En este paso se realizan el acomodo de los numeros 
 #De esta manera el formato adquirido al imrpimir el resultado 
 #Es de una forma de fecha 

 print(año)
 print(mes)
 print(dia)
#Se imprimen los resultados del paso anterior para que el usuario 
#´Pueda corroborar 
 

 Datosdate =datetime.datetime(int(año),int(mes),int(dia))

 print("Resultados...")
 print(Datostring)
 print(type(Datostring))
 print(Datosint)
 print(type(Datosint))
 print(Datosfloat)
 print(type(Datosfloat))
 print(Datosdate)
 print(type(Datosdate))
 #Los datos resultantes de nuestro programa se imprimen
 #Para el usuario 




