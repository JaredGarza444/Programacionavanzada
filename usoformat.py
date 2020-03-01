# El formato "format" es utilizado para crear 
#cadenas de texto en donde tenemos un diccionario
#con varios elementos y nos da la posibilidad de 
#de realizar la sustutucion de strings y combinar 
#los elementos en un solo mensaje 

def main():
 intLado1=15
 intLado2=10
#primero definimos las variables que vamoa a utilizar
 AreaCuadrado=(intLado1*intLado2)/2#Hacemos calculo
 texto="AreaCuadrado:{2:0.2f}({0} por {1} entre dos)"
#definimos el orden en que apareceran los elemntos del diccionario en nuestro mensaje 
 print(texto.format(intLado1,intLado2,AreaCuadrado))
#Impirmimos nuestro mensaje y le pasamos los argumentos a format 