
import random

def  juego_adivinanza():

    numero_secreto = random.randint(1,100) # numero secreto
    adivinado = False
    intentos = 0

    while not adivinado: # mientras que no sea false o sea true. hacer lo siguiente
        input_numero = input("\n[!] Escribe un  numero del 1 al 100: ")
        

        if input_numero.isdigit():
            input_numero = int(input_numero)
            intentos += 1
 
            if input_numero > numero_secreto:
                print(f"\t\n [+] el numero secreto es menor al numero {input_numero}")
            elif input_numero < numero_secreto:
                print(f"\t\n [+] el numero secreto es mayor al numero {input_numero}")
            else:
                print(f"\t\n [+] Has adivinado el numero felicidades, numero secreto es \"{input_numero}\". \n el numero de intentos es: \"{intentos}\" ")
        else:
            print("\t\n [+] Por favor ingresa un numero del 1 al 100")      
            
juego_adivinanza()


            


