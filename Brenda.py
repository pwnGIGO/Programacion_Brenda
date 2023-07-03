'''
 MATERIA: Programación
 PROGRAMADOR: Brenda Miranda Cázares 
 CONTACTO: brenda_mirand@hotmail.com
 FECHA: 3 de Julio 2023
'''

print("Yo soy Brenda de la licenciatura en física y este es mi primer HOLA MUNDO!")
#print("Yo soy Brenda de la licenciatura en física y este es mi primer HOLA MUNDO!2")
print("Yo soy Brenda de la licenciatura en física y este es mi primer HOLA MUNDO!3")

# Esta linea imprime un hola con el numero 4
print("Yo soy Brenda de la licenciatura en física y este es mi primer HOLA MUNDO!4") 

print("&&\t Primer caratula\t&&")
print( "&&&\tAprendiendo a programar\t&&&")
print("\t°°Brenda Miranda Cázares°°\t\n&&\tLicenciatura en Física\t&&")
print("\t Fecha: Junio 2023") 

titulo = "&\t Primer caratula        \t&"
clase = "&\tAprendiendo a programar \t&"
nombre_y_licenciatura = "&\t Brenda Miranda Cázares  \t&\n&\tLicencicatura en físca    \t&"
fecha = "&\t Julio 2023             \t&"



print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(titulo)
print(clase)
print(nombre_y_licenciatura)
print(fecha)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

"""
ALGORITMO
    1. Imprimir el margen superior de la hoja
    2. Imprimir margen lateral con titulo
    3. Imprimir margen lateral con nombre 
    4. Imprimir margen lateral y licenciatura
    5. Imprimir margen lateral y fecha
    6. Imprimir el margen inferior de la hoja

"""
nombre= "&\tBrenda Miranda Cázares   \t&"
licenciatura= "&\tLicenciatura en física  \t&"

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(titulo)
print(clase)
print(nombre)
print(licenciatura)
print(fecha)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Definicón de función que calcula la velocidad de un objeto
def velocidad (distancia, tiempo):
  #print("Calculo de a velocidad.")
  velocidad = distancia / tiempo
  return str(velocidad) + " m/s" # Regresa cadena de texto

# Definicón de método que muestra una carátula con contenido estático
def caratulaEstatica ():
  print("&&\t Primer caratula\t&&")
  print( "&&&\tAprendiendo a programar\t&&&")
  print("\t°°Brenda Miranda Cázares°°\t\n&&\tLicenciatura en Física\t&&")
  print("\t Fecha: Junio 2023") 

# Definicón de método que muestra una carátula con contenido dinámico
def caratulaDinamica (titulo, clase, nombre, licenciatura, fecha):
  print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
  print("&\t",titulo, "\t&")
  print("&",clase, "\t&")
  print("&",nombre, "\t&")
  print("&",licenciatura, "\t&")
  print("&",fecha, "          \t\t&")
  print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

  # Llamado a la función velocidad

print("El resultado de 15 m / 5 s es:", velocidad(15,5))

print("El resultado es:", velocidad(11000,11))

print("El resultado es:", velocidad(300000000, 100))

#caratulaEstatica()

caratulaDinamica("Primer caratula","Aprendiendo a programar","Brenda Miranda Cázares","licenciatura en física","Julio 2023")

caratulaDinamica("Probando probando 123","CLASE 1","Rodrigo","Compu","3, Julio 2023")


#Algoritmo:
"""
  Step 1: Tener el valor f
  Step 2: Mostrar un mensaje descriptivo de la función.
  step 3: Sustituir f en la fórmula 
  step 4: Guardar el cálculo en una variable
  step 5: Regresar el resultado en forma de cadena de texto
"""

#Definición de la fincion Grados Fahrenheit a Celcius
def Fahr_a_Celcius (f):
  print("Calculo de grados Fahrenheit a Celcius")
  celcius=(5*(f-32))/9
  return "La conversión de " + str(f) + " grados Fahrenheit a Celcius es: " + str(celcius) + "."
  #return celcius

print(Fahr_a_Celcius(407))
