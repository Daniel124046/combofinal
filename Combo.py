import os
import sys
import requests
import marshal
import urllib.request
from string import Template

class pkm():
    poke_name =""
    com =""
    lati =""
    longi =""
    sang =""
    fena =""
    dia =""
    mes =""
    na =""
    sg =""
    ty =""
    ed1 =""
    pokeid =""
    imag=""
#Almacen de Datos PkM:
pokem = []

url_api = 'https://pokeapi.co/api/v2/pokemon/'

#signos:
signo = ["Aries", "Tauro", "Gemenis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
fecha = [20, 20, 21, 22, 23, 23, 24, 23, 23, 22, 20, 20]
filein = open('Template/plantilla.html')
src = Template(filein.read())
#menu principal:
def menu():
    os.system("cls")
    print("Bienvenido a tu Pokedex")
    print("Elige unas de las opciones")
    print()
    print("A - Agregar PKM")
    print("V - Ver PKM'S")
    print("R - Reportes")
    print("E - Exportar PKM")
    print("M - Exportar PKM en el Mapa")
    print("S - Salir")
    print()   
    
    preg = input("Digite su opcion deseada: ")
    
    if preg.lower() == "a":
        agregar()       
    elif preg.lower() == "v":
        ver()
    elif preg.lower() == "r":
        report()
    elif preg.lower() == "e":
        export_pkm()
    elif preg.lower() == "m":
        export_map()
    elif preg.lower() == "s":
        exit()      
    else:
        print()
        print("INCORRECTO, Digite una opcion correcta.")
        menu()

    

#Agregando PKM'S
def agregar():
    os.system("cls")
 #validacion de nombre pokemon:
    p = pkm()
    p.poke_name = input("Ingrese el nombre del pokemon: ")
    poke_url = url_api + p.poke_name
    

    response = requests.get(poke_url)
    data = response.json()        

    #validadcion:
    if response.status_code == 200:
        print("Validando")
        print("Muy ahora vamos a tomar datos del PKM")
        
    else:
        print("Pokemon incorrecto")
        input("presione enter para volver")
        agregar()


    #obteniendo datos
    #nombre:


    #Comida:
    p.com = input("Ingrese la comida favorita: ")


    #longitud y latitud del pkm capturado:
    p.lati = input("Ingrese la latitud: ")

    p.longi = input("Ingrese la longitud: ")

    
    #Tipo de sangre:
    p.sang = input("Ingrese el tipo de sangre: ")


    #Fecha de Nacimiento:
    p.dia = int(input("Ingrese el dia de nacimiento: "))
    p.mes = int(input("Ingrese el mes de nacimiento: "))
    #Obteniendo el signo:
    p.mes = p.mes - 1
    if p.dia > fecha[p.mes]: 
        p.mes = p.mes - 1
    if p.mes == 12:
        p.mes = 0
    
    #Obteniendo la edad:
    p.na = 0
    p.ed1 = 0
    ano = 2018
    p.na = int(input("Ingrese el año de nacimiento: "))
    p.ed1 = int(2018) - int(p.na)
    #edad del PKM:

    
    #fecha nacimiento
    p.fena = p.dia, p.mes, p.na
    #signo
    p.sg = (signo[p.mes])

    #Tipo del PKM:
    pokemon_type = [types['type']['name'] for types in data['types']]   
    p.ty = (f" ".join(pokemon_type))    

    #id del pkm:
    p.pokeid = data["id"]

   
    pokem.append(p)

    input("Datos agregados, Presione enter para continuar")  

    menu()
    return p

#Mostrando pokemones capturados
def ver():
    os.system("cls")
    print("Pokemones Agregados en tu pokedex.")
    print()
    for p in pokem:

        print("Nombre:", p.poke_name)
        print("Comida favorita:",p.com)
        print("Latitud:",p.lati)
        print("Longitud:",p.longi)
        print("Tipo de sangre:",p.sang)
        print("Fecha de nacimiento:",p.fena)
        print("El signo zodiacal:",p.sg)
        print("Tipo:",p.ty)
        print("Edad:",p.ed1)
        
        print()
      
    print()
    input("Estos son tus Pokemones, Presiona enter si quieres ir al menu principal")
    menu()

#Aqui se Buscan los PKM 
def report():
    os.system("cls")
    print("Aqui tendremos un reporte de todos los pokemones.")
    print()
    print("C - Buscar Pokemon por mes de cumpleaños")
    print("T - Buscar Pokemon por tipo")
    print("Q - Buscar Pokemon gusto de comida")
    print()
    pregu = input("Ingrese la opcion deseada: ")

    if pregu == "c":
        print("hola")
    
    elif pregu == "t":
        print("hola")
    elif pregu == "q":
        print("hola")

#Exportando PKM'S
def export_pkm():
    os.system("cls")
    print("Aqui podra exportar el pokemon en un archivo HTML")
    print()
    for p in pokem:
        print("Nombre:", p.poke_name)
    print()

    export = input("Digite el nombre del pokemon a exportar: ")
    for p in pokem:
        if export == p.poke_name:
            d = { 'poke_name':p.poke_name, 'com':p.com, 'lati':p.lati, 'longi':p.longi, 'sang':p.sang, 'na':p.na, 'sg':p.sg, 'ty':p.ty, }            
            result = src.substitute(d)
            try:
                os.mkdir("pokemones")
                filein2 = open('pokemones/'+str(export)+'.html', 'w') 
                filein2.writelines(result)
                print("Creando carpeta...")
                print("Guardando...")
            except OSError:
                if os.path.exists("pokemones"):
                    filein2 = open('pokemones/'+str(export)+'.html', 'w')
                    filein2.writelines(result)
                    print("Guardando...")
            
            input("Datos Exportados, Presione enter para volver al menu")
            menu()

def file_get_contents(filename):
    if os.path.exists(filename):
        fp = open(filename, "r")
        content = fp.read()
        fp.close()
        return content

def export_map():
    os.system("cls")
    print("Aqui podemos exportar los PKM en un mapa")
    print()
    base = file_get_contents("ejemplo.html")
    pkma = []
    for p in pokem:
        tmp = """L.marker([""" + p.lati + """,""" + p.longi +"""])
        .addTo(map)
        .bindPopup('""" + p.poke_name + """');"""
        pkma.append(tmp)
    sep = " "
    tmp = sep.join(pkma)
    base = base.replace("{MARCADORES}",tmp)
    insert = open("mapa.html", "w")
    insert.write(base)
    insert.close()
    print("Exportado")
    input("Presione enter para regresar al menu")
    menu()





menu()
