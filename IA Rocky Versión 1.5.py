# -*- coding: utf-8 -*-

#modulos/bibliotecas

import time
from colorama import init, Fore
import os
import random

#Funciones

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

def sensores_definición():
  t=1
  print(f"{nombre}, un sensor es un dispositivo que capta magnitudes físicas (variaciones de luz, temperatura, sonido, etc.) u otras alteraciones de su entorno.")
  time.sleep(2)
  print("¿Quieres ver algunos ejemplos?")
  sensor_aprobacion=input()
  if sensor_aprobacion == "Si" or sensor_aprobacion == "si" or sensor_aprobacion == "SI":
    print("A continuación veras una lista y escogeras la magnitud fisica que quieras ver ligada a algún sensor.")
    print("")
    print(Fore.YELLOW + """   
    1. Temperatura
    2. Luz
    3. Sonido
    4. Movimiento
    """) 
    print("")
    while t == 1:
      respuesta_sensores=int(input("Digita el número del item que deseas saber. \n"))
      if respuesta_sensores == 1:
        print(f"{nombre}, un sensor de temperatura es un componente electrónico que devuelve una señal eléctrica que depende de la temperatura del sensor. A partir de la señal eléctrica se puede conocer la temperatura real a la que se encuentra el sensor.")
        respuestasensort=input(f"¿Ahora quieres saber sobre algunos sensores de temperatura {nombre}? \n")
        if respuestasensort == "Si" or respuestasensort == "si" or respuestasensort == "SI":
          print("Vale, a continuación algunos ejemplos de sensores de temperatura.")
          print("- Sensor de temperatura NTC.")
          print("- Sensor de temperatura basado en circuito integrado LM35.")
          time.sleep(3)
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
        elif respuestasensort == "No" or respuestasensort == "no" or respuestasensort == "NO":
          print("Vale no hay lio, sigamos.")
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
      elif respuesta_sensores == 2:
        print(f"{nombre}, un sensor de luz es el que nos va a permitir medir luz en el entorno donde tengamos realizado nuestro montaje, de tal forma que podamos decidir qué acciones a realizar en función de los umbrales de luz u oscuridad que estimemos oportuno.")
        time.sleep(4)
        print("Un umbral corresponde en este caso teniendo en cuenta la luz, a la mínima cantidad de luz que puede detectar el ojo humano en la oscuridad")
        time.sleep(3)
        respuestasensort=input(f"¿Quieres saber sobre algunos sensores de luz {nombre}? \n")
        if respuestasensort == "Si" or respuestasensort == "si" or respuestasensort == "SI":
          print("""Un ejemplo de este tipo de sensores es el LDR o fotoresistor, que es un componente cuya resistencia interna va a cambiar en función de la luz percibida. Su comportamiento es el siguiente:
              
          Mas luz = menor resistencia eléctrica
          Menos luz = mayor resistencia eléctrica

          """)
          time.sleep(3)
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
        elif respuestasensort == "No" or respuestasensort == "no" or respuestasensort == "NO":
          print("Vale no hay problema, sigamos aprendiendo.")
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
      elif respuesta_sensores == 3:
        print(f"{nombre}, el sensor de sonido es una tarjeta de pequeñas dimensiones para aplicaciones donde se necesite sensar la intensidad del sonido o ejecutar alguna instrucción posterior a detectar un ruido. ")
        time.sleep(4)
        print("")
        print("Ademas...")
        print("")
        time.sleep(2)
        print("El módulo cuenta con ganancia ajustable para el micrófono para así tener una mejor lectura además cuenta con tres pines para conectarlo con tu Arduino, microcontrolador o cualquier tarjeta de desarrollo.")
        time.sleep(3)
        respuestasensort=input(f"¿Quieres saber sobre algún ejemplo de sensores de sonido {nombre}? \n")
        if respuestasensort == "Si" or respuestasensort == "si" or respuestasensort == "SI":
          print("Un ejemplo seria: LM393 Módulo sensor de sonido. Cuyas espeficicaciones son: ")
          print("")
          time.sleep(2)
          print("""
          - Voltaje de operacion: 3.3v-5v
          - Tamaño: 44mm/16mm/9mm
          """)
          print("")
          time.sleep(3)
          voltaje=input("¿Deseas saber sobre que es el voltaje? \n")
          if voltaje == "Si" or voltaje == "SI" or voltaje == "si":
            print("")
            print(f"{nombre}, el voltaje es en pocas palabras la cantidad de voltios que actúan en un aparato o en un sistema eléctrico.")
            time.sleep(3)
            print("El voltaje, también es conocido como tensión o diferencia de potencia permite establecer el flujo de una corriente eléctrica.")
            time.sleep(3)
            print("Por ejemplo una pila de un control consta con alrededor de 1.5 voltios.")
            print("")
            time.sleep(2)
            tamañosensorsonido=input(f"¿Quieres ahora, de pronto saber a cuanto equivale el tamaño del sensor de sonido LM393 con algún objeto? \n")
            if tamañosensorsonido == "Si" or tamañosensorsonido == "si" or tamañosensorsonido == "SI":
              print("El tamaño de 44mm es equivalente a 4.4 cm es decir que el modulo tiene un tamaño parecido a un borrador.")
            else:
              print(f"Vale sigamos entonces, {nombre}")
          elif voltaje == "No" or voltaje == "NO" or voltaje == "no":
            print("¡Ok! pero...")
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
        elif respuestasensort == "No" or respuestasensort == "no" or respuestasensort == "NO":
          print("Vale no hay problema, sigamos aprendiendo.")
          repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
          if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
            print("Ok")
            print(Fore.YELLOW + """
            1. Temperatura
            2. Luz
            3. Sonido
            4. Movimiento
            """)
            t=1
          elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
      elif respuesta_sensores == 4:
        print(f"{nombre}, es un sensor que reacciona sólo ante determinadas fuentes de energía tales como el calor del cuerpo humano o animales. ")
        print("")
        time.sleep(3)
        print("Estos basicamente...")
        print("Reciben la variación de las radiaciones infrarrojas del medio ambiente que cubre. Es llamado pasivo debido a que no emite radiaciones, sino que las recibe. Estos captan la presencia detectando la diferencia entre el calor emitido por el cuerpo humano y el espacio alrededor.")
        print("")
        time.sleep(4)
        print("Estos sensores tambien son conocidos como: ")
        time.sleep(1)
        print(Fore.GREEN + "Detectores PIR (Passive Infrared) o Pasivo Infrarrojo")
        time.sleep(2)
        repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
        if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
          print("Ok")
          print(Fore.YELLOW + """
          1. Temperatura
          2. Luz
          3. Sonido
          4. Movimiento
          """)
          t=1
        elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
            t=2
      elif respuestasensort == "No":
        print("Vale no hay problema, sigamos aprendiendo.")
        repetir_sen=input(f"{nombre}, quieres saber sobre otro sensor? \n")
        if repetir_sen == "Si" or repetir_sen == "SI" or repetir_sen == "si":
          print("Ok")
          print(Fore.YELLOW + """
          1. Temperatura
          2. Luz
          3. Sonido
          4. Movimiento
          """)
          t=1
        elif repetir_sen == "No" or repetir_sen == "NO" or repetir_sen == "no":
          t=2
  else:
    print("Ok no hay problema")

def despedida():
  print("")
  print(Fore.YELLOW + f"Bueno {nombre}, fue un placer charlar contigo...")
  time.sleep(1)
  print(Fore.CYAN + f"Espero hayas aprendido muchisimo, y que hayas podido tomar nota de absolutamente todo lo que te haya parecido de interes.")
  time.sleep(1)
  print("")
  print(Fore.YELLOW + f"A continuación me encantaria recopilar unos datos tuyos. Regalame un segundo. ")
  print("")
  print(Fore.GREEN + "Cargando")
  time.sleep(1)
  print(Fore.GREEN + ".")
  time.sleep(0.90)
  print(Fore.GREEN + ".")
  time.sleep(0.80)
  print(Fore.GREEN + ".")
  time.sleep(0.70)
  print(Fore.GREEN + ".")
  time.sleep(0.60)
  print(Fore.GREEN + ".")
  time.sleep(0.50)
  print(Fore.GREEN + ".")
  print("")
  print(Fore.YELLOW + f"Recopilación datos : {nombre}")
  lista_datos = ["Nombre: ", nombre, "Genero: ", genero, "País: ", pais_final, "Edad: ", edad, "Estudio", estudio, "Gusto por la tecnología: ", tecnologia, "Conocimiento programación: ", programacionrta, "Vocación a futuro: ", vocacion]
  print(lista_datos)
  time.sleep(5)
  print(Fore.GREEN + "Cargando")
  time.sleep(1)
  print(Fore.GREEN + ".")
  time.sleep(0.90)
  print(Fore.GREEN + ".")
  time.sleep(0.80)
  print(Fore.GREEN + ".")
  time.sleep(0.70)
  print(Fore.GREEN + ".")
  time.sleep(0.60)
  print(Fore.GREEN + ".")
  time.sleep(0.50)
  print(Fore.GREEN + ".")
  print("")
  input(Fore.GREEN + "Presiona la tecla Enter para cerrar el programa y dirigite a la carpeta donde tienes guardado Rocky y revisa el archivo de texto datos.txt")

  file = open("datos.txt", "w")
  file.write("| --- --- DATOS DE INTERVENCIÓN - Rocky 1.5 --- --- |" + os.linesep)
  file.write(f"Nombre: {nombre}" + os.linesep)
  file.write(f"Genero: {genero}" + os.linesep)
  file.write(f"País: {pais_final}" + os.linesep)
  file.write(f"Edad: {edad}" + os.linesep)
  file.write(f"Estudio: {estudio}" + os.linesep)
  file.write(f"Gusto por la tecnología: {tecnologia}" + os.linesep)
  file.write(f"Conocimiento programación: {programacionrta}" + os.linesep)
  file.write(f"Vocación a futuro: {vocacion}")
  file.close()

def motor_definición():
  print(f"Vale mira {nombre}, un motor es: ")
  print("")
  print(Fore.BLUE + "Una maquina que, haciendo uso de una fuente de energía, puede generar movimiento.")
  time.sleep(2)
  print("En arduino encontramos diferentes tipos de motores, pero entre los mas conocidos esta los siguientes: ")
  time.sleep(1)
  print(Fore.BLUE + """
  1. Motores DC
  2. Servomotores
  3. Motores paso a paso
  """)
  print("")
  rta_motor=input("¿Sobre cuál deseas saber?, digita el número de la lista.")
  if rta_motor == 1:
    print(f"{nombre}, un motor DC es según torrente (2013) en su libro Arduino para todos.")
    time.sleep(0.5)
    print("Uno de los motores más simples.  Estos poseen dos terminales, los cuales cuando uno se conecta a una fuente de alimentación continua como una batería y el otro se conecta a tierra el motor gira en una dirección contraria a las manecillas del reloj es decir de derecha a izquierda. ")
    print("")
    print("Este tipo de motores se caracteriza por que, entre más intensidad de corriente, más velocidad tendrá a la hora de realizar las revoluciones es decir los giros.")
  elif rta_motor == 2:
    print(f"{nombre}, un servomotor es según torrente (2013) en su libro Arduino para todos.")
    time.sleep(0.5)
    print("Un motor que permite limitar la velocidad de giro es decir las revoluciones por segundo de su eje.")
    print("")
    print("En pocas palabras su eje no tiene la característica propia de girar cómo le sea necesario libremente, sino que, rota un determinado ángulo, indicado a través de la instrucción dada en el lenguaje del Software de Arduino.  ")
    print("")
  elif rta_motor == 3:
    print(f"{nombre}, un motor paso a paso es según torrente (2013) en su libro Arduino para todos.")
    time.sleep(0.5)
    print("Aquel motor que no gira continuamente, sino que lo hace con un número determinado de pasos que deben ser estipulados previamente en las líneas de código del Arduino de esta manera teniendo un control total del giro mínimo del eje.")
    print("")

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
c=1

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
print(Fore.CYAN + "Version 1.5")
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
      print(Fore.YELLOW + "Rocky es un software diseñado desde el año 2020 como te mencione anteriormente, esperamos generar proximas actualizaciones para que el software siga evolucionando.")
      print("")
      time.sleep(2)
      print(Fore.YELLOW + "La versión actual de Rocky es = update 1.5")
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
      print(Fore.MAGENTA +"Rocky fue desarrolado con unos de los mejores lenguajes de programación que han surgido en la historia, el cual es Python.")
      print("")
      print(Fore.MAGENTA +"Los entornos de desarrollo que fueron utilizados para el desarrollo de Rocky fueron: ")
      time.sleep(2)
      print(Fore.MAGENTA +"""
      - Repl.it (https://repl.it/~)
      - Visual Studio Code
      - IDLE Python
      - Sublimetext
      - Consola windows (Powershell)""")
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
      print(Fore.GREEN + "El objetivo de Rocky ademas de enseñar aspectos frente el Hardware de Arduino, tambien es poder demostrar como la programación desde edades tempranas de conocimiento es ¡Increible!") 
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
      print(Fore.RED + "Gracias a etapas de desarrollo es posible afirmar que este software esta pensado y asi mismo diseñado para que cualquier persona que sepa leer pueda interactuar con Rocky")
      time.sleep(7.5)
      print("Esta caracteristica fue añadida especificamente en la Versión 1.5 del presente software.")
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
      print(Fore.BLUE + "Rocky fue diseñado por los estudiantes de la institución Liceo Nuevos Horizontes ubicado en Bogota - Colombia, ademas hasta el momento cuenta con mas de 700 lineas de codigo. ")
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
elif edad >= 10 and edad <= 17:
  print(f"{nombre} ah vale, eres aun un poco joven, ademas es bueno que aprendas programación desde esta edad.")
  time.sleep(2)
  print("")
  print(Fore.CYAN + "Nose si sabias", nombre,"que personas como Elon Musk, dueño de tesla y spaceX hoy dia empresa que piensa llegar a marte con la programación y personas como bill gates, fundador de apple, a esta edad maso menos ya sabian programar y hoy en día son las personas mas exitosas del mundo, ese mismo mundo al cual han cambiado con su tecnologia.")
  print("")
  time.sleep(7)
  input(f"Presiona una tecla para continuar {nombre}...")
elif edad >= 18:
  print("Increible que a pesar de tu edad y quizas labores que te ocupen intentes aprender sobre programación.")
  time.sleep(2)
  print("Me parece muy bien", nombre,"!" )
  time.sleep(3)
while c == 1:
  genero=input(f"¿{nombre}, eres hombre o mujer? \n")
  if genero == "Mujer" or genero == "MUJER" or genero == "mujer" or genero == "MUjer" or genero == "mujER" or genero == "MUJEr":
    print("Increible eres una mujer... :)")
    time.sleep(1)
    print("Tengo que ser un poco más caballeroso.")
    time.sleep(4)
    break
  elif genero == "Hombre" or genero == "hombre" or genero == "HOMBRE" or genero == "HOMbre" or genero == "homBRE" or genero == "HOMBRe":
    print("Eres hombre increible, tendre que ser un poco mas rudo a la hora de hablar contigo. >:I")
    time.sleep(2)
    print(f"Es broma {nombre}, no te preocupes jajaja.") 
    time.sleep(4)
    input(f"Presiona una tecla para continuar {nombre}...")
    os.system('cls')
    break
  else:
    print("No entendi tu respuesta.")
    c=1
time.sleep(2)
os.system('cls')
print("Rocky necesita saber unos datos tuyos, empecemos.")
while b == 1:
  pais=input(f"{nombre} eres de Colombia? \n")
  if pais == "Si" or pais == "si" or pais == "SI" or pais == "sI":
    print("Vale")
    pais_final = "Colombia"
    time.sleep(2)
    os.system('cls')
    break
  elif pais == "No" or pais == "no" or pais == "NO" or pais == "nO":
    print("Oh vale, increible.")
    time.sleep(0.5)
    print("Y entonces, ¿de que país eres?")
    pais_final=input("")
    os.system('cls')
    break
  else:
    print(f"{nombre}, no entendi tu respuesta responde nuevamente si eres del país colombiano o no.")
    time.sleep(3)
    os.system('cls')
    b=1
time.sleep(1)
tecnologia=input(f"¿Oye y te gusta la tecnología? \n")
if tecnologia == "Si" or tecnologia == "si" or tecnologia == "SI" or tecnologia == "sI":
  print("Me encanta saberlo")
elif tecnologia == "No" or tecnologia == "no" or tecnologia == "NO" or tecnologia =="nO":
  print("¿Por qué no te gusta?")
  respuesta_tec=input()
  print("Oh ok, ahora me quedo un poco mas claro.")
print("")
programacionrta=input(f"¿{nombre} sabes sobre programación? \n")
if programacionrta == "Si" or tecnologia == "si" or tecnologia == "SI" or tecnologia == "sI":
  lenguajes_programacion=input("¿Y cuales lenguajes conoces?\n")
  print("Ohh wao :3")
elif programacionrta == "No" or tecnologia == "no" or tecnologia == "NO" or tecnologia =="nO":
  print("")
  print("No hay problema")
  time.sleep(2)
print(f"Ahora {nombre}, quiero preguntarte:")
time.sleep(1)
vocacion=input(f"{nombre}, ¿en que te piensas especializar en un futuro? \n")
print(Fore.GREEN + "Oh vale.")
print(Fore.YELLOW + "Increible.")
time.sleep(1)
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
if arduinodefinicion == "Si" or arduinodefinicion == "SI" or arduinodefinicion == "si" or arduinodefinicion == "sI":
  Arduino_Definición()
elif arduinodefinicion == "No" or arduinodefinicion == "NO" or arduinodefinicion == "no" or arduinodefinicion == "nO":
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
      
sensores_def=input(f"¿{nombre} quieres saber sobre sensores de Python? \n")
if sensores_def == "Si" or sensores_def == "si" or sensores_def == "SI" or sensores_def == "sI":
  print(Fore.YELLOW + "¡Excelente!")
  os.system('cls')
  sensores_definición()
elif sensores_def =="No" or sensores_def == "no" or sensores_def == "NO" or sensores_def == "nO":
  print(f"Vale, no hay problema {nombre}")
  os.system('cls')
  
print(f"¿Listo {nombre}, ahora quieres aprender sobre algunos motores usados en Arduino?")
motores=input()
if motores == "Si" or motores == "si" or motores == "SI" or motores == "sI":
  print(Fore.YELLOW + "¡Excelente!")
  os.system('cls')
  motor_definición()
elif motores =="No" or motores == "no" or motores == "NO" or motores == "nO":
  print(f"Ok no hay lio {nombre}")
  os.system('cls')
  time.sleep(2)
  print(f"Eso fue todo por hoy. Esperamos que con tus aportes surjan nuevas actualizaciones del software y de esta forma puedas aprender mucho mas.")

print("")
print(Fore.YELLOW + f"{nombre}, espero hayas aprendido muchisimo sobre Arduino y te hayas interesado un poco sobre la programación.")
print("")
print(Fore.BLUE + "Gracias por contribuir a mi conocimiento, ya que de esta forma mejorare algunas cosas y mejorare mi sistema en proximas actualizaciones.")
print("")
print(Fore.RED + "Att. Rocky")
print("")

despedida()

#Versión 1.5 
