#Esta funcion pregunta un dato al usuario 
#Y reliza validaciones hasta que el dato otorgado 
#Por el usuario sea correcto 

import re 
#Esta expresion sera utilizada para importar 
#El modulo requerido

def main():
  #Preguntara un dato y lo estara validando
  #Con expresiones 


 while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
  #Con la estructura del while solicitamos el RFC  a nuestro 
  #Usuario y verificamos que la extencion sea la adecuada
    if (coincide):
      print("El RFC ingredado es correcto, gracias")
      break
    else:
      print("El RFC ingresado es incorrecto, por favor intente de nuevo, gracias.")
    #Con la estructura del if despues de evaluar los 
    #Datos y ver si estan correctos establecemos esta 
    #Estrucutura para que mande un mensaje de confirmacion al usuario dependiendo del resultado
    #Obtenido con anterioridad



  
 
