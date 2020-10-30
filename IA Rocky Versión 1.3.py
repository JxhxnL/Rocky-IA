import time
from colorama import init, Fore
import os
import random

#funciones
def Arduino_Definición():
  arduino=input(f"¿{nombre}, sabes que es Arduino? \n")
  if arduino == "Si" or arduino == "SI" or arduino == "si":
    rtaarduino=input("Y, ¿qué es? \n")
    print(Fore.GREEN + f"¡Ok!")
    rtaarduino1=input(f"{nombre}, y ¿te gustaria saber algo más? \n")
    if rtaarduino1 == "Si" or rtaarduino1 == "SI" or rtaarduino1 == "si":
      print(f"{nombre} según Torrente (2013) en su libro de Arduino curso practico de formación, Arduino es una placa de hardware libre que lleva consigo un microcontrolador y una serie de pines.")
      hardwarelibre=input("Sabes que es hardware libre? \n")
      if hardwarelibre == "si" or hardwarelibre == "SI" or hardwarelibre == "Si":
        print("Ok")
        time.sleep(1)
      elif hardwarelibre == "No" or hardwarelibre == "NO" or hardwarelibre == "no":
        print(f"Ok no hay problema {nombre}")
        print("Hardware libre es un dispositivo basicamente de codigo abierto, que puedes adquirir de manera pública ya sea con una forma de pago o de manera gratuita, que ademas te permite intervenir de manera libre con el mismo dispositivo.")
        time.sleep(3)
        input(f"Presiona una tecla para continuar {nombre}...")
        os.system('cls')
        print(f"{nombre} ademas Torrente (2013), tambien afirma que Arduino proporciona la facilidad de insertar cables dentro de estos pines y permitir en el, el flujo de corriente proporcionando de tal forma el uso de sensores y actuadores.")
  if arduino == "No" or arduino == "NO" or arduino == "no":
    print(f"{nombre} según Torrente (2013) en su libro de Arduino curso practico de formación, Arduino es una placa de hardware libre que lleva consigo un microcontrolador y una serie de pines.")
    hardwarelibre=input("Sabes que es hardware libre? \n")
    if hardwarelibre == "si" or hardwarelibre == "SI" or hardwarelibre == "Si":
      print("Ok")
    elif hardwarelibre == "No" or hardwarelibre == "NO" or hardwarelibre == "no":
      print(f"Ok no hay problema {nombre}")
      print("Hardware libre es un dispositivo basicamente de codigo abierto, que puedes adquirir de manera pública ya sea con una forma de pago o de manera gratuita, que ademas te permite intervenir de manera libre con el mismo dispositivo.")
      time.sleep(3)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      print(f"{nombre} ademas Torrente (2013), tambien afirma que Arduino proporciona la facilidad de insertar cables dentro de estos pines y permitir en el, el flujo de corriente proporcionando de tal forma el uso de sensores y actuadores.")

def año_Arduino():
  print(f"{nombre}, Arduino fue inventado en el año 2005 por el entonces estudiante del instituto IVRAE Massimo Banzi, quien, en un principio, pensaba en hacer Arduino por una necesidad de aprendizaje para los estudiantes de computación y electrónica del mismo instituto donde se encontraba estudiando")
  time.sleep(2)
  print("Ya que en ese entonces, adquirir una placa de micro controladores era muy complicado.")
  time.sleep(1)
  print(Fore.YELLOW + "En conclusion Arduino surgio por una necesidad.")

def captcha1(data):
  capcha=int(input("¿Qué año es?\n"))
  if capcha == 2020:
    print(Fore.GREEN + "Correcto")
    capcha2=input("Ahora responde: ¿Un carro es un medio de transporte?. Responde Si / No\n")
    if capcha2 == "Si" or capcha2 == "SI" or capcha2 == "si":
      print(Fore.GREEN + "Correcto")
      print(Fore.RED + "Verificación completada")
      time.sleep(2)
    else:
      print("Error de digitación, ejecuta nuevamente el programa.")
      time.sleep(2)
      os.system('cls')
      exit()
  else:
    print("Error de digitación, ejecuta nuevamente el programa.")
    time.sleep(2)
    os.system('cls')
    exit()

def captcha2(data):
  capcha=int(input("¿Qué número es menor entre 4 y 7?\n"))
  if capcha == 4:
    print(Fore.GREEN + "Correcto")
    capcha2=input("¿Pesa más un kilo de algodon que un kilo de hierro solido?. Responde Si / No \n")
    if capcha2 == "NO" or capcha2 == "No" or capcha2 == "no":
      print(Fore.GREEN + "Correcto")
      print(Fore.RED + "Verificación completada")
      time.sleep(2)
    else:
      print("Error de digitación, ejecuta nuevamente el programa.")
      time.sleep(2)
      os.system('cls')
      exit()
  else:
    print("Error de digitación, ejecuta nuevamente el programa.")
    time.sleep(2)
    os.system('cls')
    exit()
    
def captcha3(data):
  capcha=int(input("¿Cuánto es 56 + 24? \n"))
  if capcha == 80:
    print(Fore.GREEN + "Correcto")
    capcha2=input("Ahora responde, ¿De que color es el cielo? \n")
    if capcha2 == "azul" or capcha2 == "AZUL" or capcha2 == "Azul":
      print(Fore.GREEN + "Correcto")
      print(Fore.RED + "Verificación completada")
      time.sleep(2)
    else:
      print("Error de digitación, ejecuta nuevamente el programa.")
      time.sleep(2)
      os.system('cls')
      exit()
  else:
    print("Error de digitación, ejecuta nuevamente el programa.")
    time.sleep(2)
    os.system('cls')
    exit()

def captcha4(data):
  print(Fore.MAGENTA + "Hay meses que tienen 30 días y otros 31 días ¿cuántos meses tienen 28 días?.")
  time.sleep(0.5)
  print("A. Solo 1 mes")
  time.sleep(0.5)
  print("B. Ninguno tiene 28 días")
  time.sleep(0.5)
  print("C. 1 cada 5 años")
  time.sleep(0.5)
  print("D. Todos los meses tienen 28 días")
  time.sleep(0.5)
  capcha=input("Responde el item de respuesta correcto:\n")
  print
  if capcha == "D" or capcha == "d":
    print(Fore.GREEN + "Correcto")
    print(Fore.YELLOW + "¿La sangre de un humano es roja?")
    capcha2=input("Ahora responde con Si o No\n")
    if capcha2 == "si" or capcha2 == "SI" or capcha2 == "Si":
      print(Fore.GREEN + "Correcto")
      print(Fore.RED + "Verificación completada")
      time.sleep(2)
    else:
      print("Error de digitación, ejecuta nuevamente el programa.")
      time.sleep(2)
      os.system('cls')
      exit()
  else:
    print("Error de digitación, ejecuta nuevamente el programa.")
    time.sleep(2)
    os.system('cls')
    exit()

def run(data):
  captchaselect = random.choice([captcha1,captcha2,captcha3,captcha4])
  print(captchaselect('data'))


#variables
a=1
b=1

init(autoreset=True)
print(Fore.GREEN +"¡Hola!")
time.sleep(0.5)
print("¡Bienvenido a este tu nuevo amigo online!")
time.sleep(1)
print("Para empezar Rocky verificara que no eres un robot")
time.sleep(1.5)
print(Fore.LIGHTYELLOW_EX +"Responde lo siguiente:")
time.sleep(1)
run('data')
os.system('cls')
time.sleep(2)
print(Fore.BLUE + "--- Rocky ---")
print(Fore.CYAN + "Version 1.2")
print("¿Quieres saber sobre quien es Rocky?")
Rocky=input()
if Rocky == "si" or Rocky == "Si" or Rocky == "SI":
  print("¡Oh ok!")
  print("Para empezar por favor regalame tu nombre")
  nombre=input()
  time.sleep(0.5)
  os.system('cls')
  print(f"{nombre}, Rocky es un Software IA desarrollado por los estudiantes del grado 9B del Liceo Nuevos Horizontes en el año 2020")
  time.sleep(5.5)
  input(f"Presiona una tecla para continuar {nombre}...")
  os.system('cls')
  print(f"{nombre}, no se si de pronto quisieras saber alguna de las siguientes cosas, si es asi solo digita el numero de el item que deseas saber.")
  print(Fore.YELLOW + "1. Año de creación")
  print(Fore.MAGENTA + "2. Lenguaje de programación del software")
  print(Fore.GREEN + "3. Objetivo del Software")
  print(Fore.RED + "4. Población a la cual va dirigido Rocky")
  print(Fore.BLUE + "5. Datos interesantes de Rocky")
  print("¿Qué deseas saber?")
  while a == 1:
    rta1=int(input())
    os.system('cls')
    if rta1 == 1:
      print(Fore.YELLOW + "Rocky es un software diseñado desde el año 2020 como te mencione anteriormente, esperamos generar proximas actualizaciones para que el software siga evoluacionando.")
      time.sleep(7.5)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      rta2=input("¿Deseas saber otro dato más? \n")
      if rta2 == "si" or rta2 == "SI" or rta2 == "Si":
        print("Digita el número nuevamente del item.")
        a=1
      elif rta2 == "no" or rta2 == "No" or rta2 == "NO":
        print("¡OK!")
        time.sleep(2)
        break
      else:
        print("Empezemos de nuevo, no te entiendo :(")
        time.sleep(2)
        os.system('cls')
        a=1 
    elif rta1 == 2:
      print(Fore.MAGENTA +"Rocky fue diseñado con unos de los mejores lenguajes de programación que han surgido en la historia,el cual es Python")
      time.sleep(7.5)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      rta2=input("¿Deseas saber otro dato más? \n")
      if rta2 == "si" or rta2 == "SI" or rta2 == "Si":
        print("Digita el número nuevamente del item.")
        a=1
      elif rta2 == "no" or rta2 == "No" or rta2 == "NO":
        print("¡OK!")
        time.sleep(2)
        break
      else:
        print("Empezemos de nuevo, no te entiendo :(")
        time.sleep(2)
        os.system('cls')
        a=1 
    elif rta1 == 3:
      print(Fore.GREEN + "El objetivo de Rocky ademas de enseñar aspectos frente el Hardware de Arduino, tambien es poder demostrar como la programación desde tempranas de edad es ¡Increible!") 
      time.sleep(7.5)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      rta2=input("¿Deseas saber otro dato más? \n")
      if rta2 == "si" or rta2 == "SI" or rta2 == "Si":
        print("Digita el número nuevamente del item.")
        a=1
      elif rta2 == "no" or rta2 == "No" or rta2 == "NO":
        print("¡OK!")
        time.sleep(2)
        break
      else:
        print("Empezemos de nuevo, no te entiendo :(")
        time.sleep(2)
        os.system('cls')
        a=1 
    elif rta1 == 4:
      print(Fore.RED + "Gracias a etapas de desarrollo es posible afirmar que este software esta pensado y asi mismo diseñado para que cualquier persona superior a 10 años mas o menos, pueda interactuar con Rocky")
      time.sleep(7.5)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      rta2=input("¿Deseas saber otro dato más? \n")
      if rta2 == "si" or rta2 == "SI" or rta2 == "Si":
        print("Digita el número nuevamente del item.")
        time.sleep(2)
        a=1
      elif rta2 == "no" or rta2 == "No" or rta2 == "NO":
        print("¡OK!")
        break
      else:
        print("Empezemos de nuevo, no te entiendo :(")
        time.sleep(2)
        os.system('cls')
        a=1 
    elif rta1 == 5:
      print(Fore.BLUE + "Rocky fue diseñado por los estudiantes del grado 9B de la institución Liceo Nuevos Horizontes ubicado en Bogota - Colombia en el año 2020, ademas hasta el momento cuenta con mas de 400 lineas de codigo. ")
      time.sleep(7.5)
      input(f"Presiona una tecla para continuar {nombre}...")
      os.system('cls')
      rta2=input("¿Deseas saber otro dato más? \n")
      if rta2 == "si" or rta2 == "SI" or rta2 == "Si":
        print("Digita el número nuevamente del item.")
        a=1
      elif rta2 == "no" or rta2 == "No" or rta2 == "NO":
        print("¡OK!")
        time.sleep(2)
        break
      else:
        print("Empezemos de nuevo, no te entiendo :(")
        time.sleep(2)
        os.system('cls')
        a=1 
    else:
      print("No entendi tu respuesta :( Digita nuevamente el número")
      time.sleep(3)
      os.system('cls')
      a=1
elif Rocky == "no" or Rocky == "No" or Rocky == "NO":
  print("Vale no hay problema")
  time.sleep(0.5)
  print("Para iniciar es necesario que por favor me regales tu nombre y asi nos vamos conociendo.")
  nombre=input()
  print(f"{nombre} es un nombre muy bonito. :3")
  time.sleep(2)
  os.system('cls')
else: 
  print("No entendi tu respuesta :(")
  time.sleep(2)
  os.system('cls')
  print(Fore.RED +"[Error 100 Rocky]")
  time.sleep(1)
  print(Fore.YELLOW + "No respondiste si o no, por favor ejecuta nuevamente el programa.")
  time.sleep(4)
  exit()
os.system('cls')
print(f"{nombre} cuantos años tienes?")
edad=int(input())
if edad <= 10:
  print(f"{nombre} eres aun muy joven")
elif edad >= 10 and edad < 18:
  print(f"{nombre} ah vale, eres aun un poco joven, ademas es bueno que aprendas programación desde esta edad.")
  time.sleep(2)
  print("Nose si sabias", nombre,"que personas como Elon Musk, dueño de tesla y spaceX hoy dia empresa que piensa llegar a marte con la programación y personas como bill gates, fundador de apple, a esta edad maso menos ya sabian programar y hoy en día son las personas mas exitosas del mundo, ese mismo mundo al cual han cambiado con su tecnologia.")
  time.sleep(7)
  input(f"Presiona una tecla para continuar {nombre}...")
  print("Interesante no?, pero bueno sigamos.")
  time.sleep(1)
elif edad >= 18:
  print("Increible que a pesar de tu edad y quizas labores que te ocupen intentes aprender sobre programación.")
  time.sleep(2)
  print("Me parece muy bien", nombre,"!" )
  time.sleep(3)
time.sleep(2)
os.system('cls')
print("Rocky necesita saber unos datos tuyos, empecemos.")
while b == 1:
  pais=input(f"{nombre} eres de Colombia? \n")
  if pais == "Si" or pais == "si" or pais == "SI" or pais == "sI":
    print("Vale")
    time.sleep(2)
    os.system('cls')
    break
  elif pais == "No" or pais == "no" or pais == "NO" or pais == "nO":
    print("Oh vale, increible.")
    time.sleep(0.5)
    print("Y entonces, ¿de que país eres?")
    país=input("")
    os.system('cls')
    break
  else:
    print(f"{nombre}, no entendi tu respuesta responde nuevamente si eres del país colombiano o no.")
    time.sleep(3)
    os.system('cls')
    b=1
os.system('cls')
estudio=input(f"{nombre}, ¿estudias? \n")
if estudio == "si" or estudio == "Si" or estudio == "SI":
  print("¿Qué estudias?")
  carrera=input()
  print("Oh vale, me parece increible.")
  input(f"Presiona una tecla para continuar {nombre}...")
  os.system('cls')
elif estudio == "No" or estudio == "NO" or estudio == "no":
  print("Bueno pero si te gusta algo y crees que es bueno, te recomiendo", nombre,"que salgas adelante en ello.")
  time.sleep(2)
  input(f"Presiona una tecla para continuar {nombre}...")
  os.system('cls')
print(Fore.GREEN + f"Bueno {nombre} ya tengo tus datos mas importantes.")
time.sleep(1)
print(Fore.YELLOW + f"Sigamos {nombre}")
input(f"Presiona una tecla para continuar {nombre}...")
os.system('cls')
arduinodefinicion=input(f"¿{nombre} estas listo para aprender sobre Arduino? \n")
if arduinodefinicion == "Si" or arduinodefinicion == "SI" or arduinodefinicion == "si":
  Arduino_Definición()
elif arduinodefinicion == "No" or arduinodefinicion == "NO" or arduinodefinicion == "no":
  print(f"Vale {nombre}, sigamos aprendiendo.")
  time.sleep(1.5)
os.system('cls')
ar_año=input("¿Te gustaría ahora saber el año en el que fue creado Arduino? \n")
if ar_año == "Si" or ar_año == "si" or ar_año == "SI":
  año_Arduino()
elif ar_año == "No" or ar_año == "no" or ar_año == "NO":
  rockybravo=input(f"¿Estas bravo {nombre}?, no quieres aprender conmigo :( \n")
  if rockybravo == "No" or rockybravo == "no" or rockybravo == "NO":
    print("Ok entonces sigamos aprendiendo :(")
  elif rockybravo == "Si" or rockybravo == "si" or rockybravo == "SI":
    print(f"Si no quieres seguir aprendiendo por ello, no hay problema", nombre,", es más te voy a enseñar mucho la proxima vez que me ejecutes")
    apagar=input(f"Si me deseas apagar solo escribe si o no {nombre} \n")
    if apagar == "Si" or apagar == "SI" or apagar == "si":
      exit()
    elif apagar == "No" or apagar == "NO" or apagar == "no":
      print(f"Bueno mi {nombre}, sigamos entonces.")

#1.4 Se realizara jueves 29 de octubre con estudiantes del grado 9B - LNH
