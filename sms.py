#!/usr/bin/python3

#Creando un script que utilice API's Gratuitas para enviar mensajes.
#By Blackster.


#importamos los modulos necesarios.
from colorama import Fore, init
import requests
import os
init()


banner = """
                               ( ( (
                                ) ) )
                               ( ( (
                             '. ___ .'
                            '  (> <) '
                    --------ooO-(_)-Ooo----------
                            SMS SENDER
                                               by Blackster
"""


def main():
    os.system('clear')
    print(Fore.YELLOW)
    print(banner)
    menu = """

███▓▒░░.MENU.░░▒▓███

1-[+]Enviar Mensaje SMS.

00->Salir.
    """
    print(Fore.GREEN)
    print(menu)



def services():
    menu = """
///////////SERVICIOS////////////
1-->Sms77.io

00->Atras.
    """
    print(Fore.YELLOW)
    print(menu)


def sms77_menu():
    os.system('clear')
    menu = """\n[*]1-->Enviar mensaje a un solo numero.\n[*]2-->Enviar mensaje a multiples numeros.\n\n00->>Atras.
    """
    print(Fore.GREEN)
    print(menu)


#creando clases.
class sms77io():
    def __init__(self):
        pass

    def one_message(self):
        self.api = api_sms77
        self.rapidapi_key = api_rapid
        self.url = "https://sms77io.p.rapidapi.com/sms"
        self.country_code = input("[*]Introduce el codigo de tu pais sin el signo ej(1): ")
        self.number = input("[*]Introduce el numero de telefono de la persona: ")
        self.message = input("[*]Introduce el mensaje que quieres enviar: ")
        self.changer = self.message.replace(" ", '%20')
        self.payload = (f"to=%2B{self.country_code}{self.number}&p={self.api}&text={self.changer}")
        #print(self.payload)
        self.headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "sms77io.p.rapidapi.com",
        'x-rapidapi-key': "{}".format(self.rapidapi_key)
        }
        self.response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
        print(self.response.text)
        #print(self.headers)
        input("\nPresione una tecla para continuar..")

    def multiple_users(self):
        self.api = api_sms77
        self.rapidapi_key = api_rapid
        self.url = "https://sms77io.p.rapidapi.com/sms"
        self.country_code = input("[*]Introduce el codigo de tu pais sin el signo ej(1): ")
        self.headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "sms77io.p.rapidapi.com",
        'x-rapidapi-key': "{}".format(self.rapidapi_key)
        }
        self.list = []
        self.i = 0
        self.x = 1
        while self.i < 3:
            ask_ = input("Introduce numero telefonico {}: ".format(self.x))
            self.i += 1
            self.x += 1
            self.list.append(ask_)
        self.message = input("[*]Introduce el mensaje que quieres enviar: ")
        self.changer = self.message.replace(" ", '%20')
        self.y = 0
        while self.y < 3:
            self.payload = (f"to=%2B{self.country_code}{self.list[self.y]}&p={self.api}&text={self.changer}")
            self.response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
            self.y += 1
            print(self.payload)
            print(self.response.text)#si arroja el code 100 es porque se ha enviado el mensaje, de lo contrario al arrojar el code 500 es por falta de fondos.
        print(self.list)
        print(self.list[0], self.list[1])

        input("\nPresiona una enter para continuar: ")


if __name__ == '__main__':
    #API's
    api_rapid = input("[*]Introduce tu API key de rapidapi: ") #pide la api de nuestra cuenta de sms77io.
    while True:
        main()
        ask = int(input("[*]Escoge una opcion: "))
        if ask == 1:
            while True:
                services()
                ask = int(input("[*]Escoge una opcion: "))
                if ask == 1:
                    api_sms77 = input("[*]Introduce tu API key sms77.io: ") #pide la api de nuestra cuenta de sms77io.
                    while True:
                        sms77_menu()
                        ask_ = int(input("Escoge una opcion: "))
                        if ask_ == 1:
                            sms77 = sms77io()
                            sms77.one_message()
                        elif ask_ == 2:
                            sms77 = sms77io()
                            sms77.multiple_users()
                        else:
                            if ask_ == 00:
                                break
                else:
                    if ask == 00:
                        break
        else:
            if ask == 00:
                print("See you...")
                break
