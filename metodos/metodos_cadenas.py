cadena1 = "hola soy seba"
cadena2 = "bienvenido maquinola"

# convierte a mayuscula
mayus = cadena1.upper()
print(mayus) # el resultado sera HOLA SOY SEBA

# convierte a minuscula
minus = cadena1.lower() 
print(minus) # el resultado sera hola soy seba

# primera letra en mayuscula
primera_letra_mayuscula = cadena1.capitalize()
print(primera_letra_mayuscula) # resultado sera Hola soy seba

# buscamos una cadena en otra cadena si n hay coincidencia resultado sera (-1)
busqueda_find = cadena1.find("y") # busca la letra y en "hola soy seba" (lo dice en que caracter esta )
print(busqueda_find) # el resultado sera 7 porque en "hola soy seba" la "y" esta en caracter 7

# buscamos una cadena en otra cadena a dif de find si no hay coincidencia sera "error"
busqueda_index = cadena1.index("y") # busca la letra y en "hola soy seba" (lo dice en que caracter esta )
print(busqueda_index) # el resultado sera 7 porque en "hola soy seba" la "y" esta en caracter 7

# si es numerico devolvera True si no devolvera False
es_numerico = cadena1.isnumeric()
print(es_numerico) #el resultado sera False porque "hola soy seba" no hay numeros

# si es alfanumerico devolvera True si no devolvera False
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico) #el resultado sera False porque "hola soy seba" no hay numeros

# busca la letra y en "hola soy seba" y nos dice cuantas veces esta 
contar_coincidencias = cadena1.count("a") # busca la letra "a" en "hola soy seba" y nos dice el numero de veces que esta
print(contar_coincidencias) # si no encuentra pone 0

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) # se pone al reves porque no es un metodo es una funcion (como print)
print(contar_caracteres)

# verificamos si una cadena empieza con otra cadena dada 
empieza_con = cadena1.startswith("h") # esta cadena empieza con h ? nos va a dar true lo mismo si ponemos "hola" (plabra)
print(empieza_con)

# verificamos si una cadena empieza con otra cadena dada
termina_con = cadena1.endswith("a") # esta cadena termina con "a"? true l mismo palbra "seba" , dara true
print(termina_con)

# reemplaza un pedazo de la cadena dada por otra 
cadena_nueva = cadena1.replace("seba","pedro") #se reemplaza "seba por pedro"
print(cadena_nueva) # print "hola soy pedro" se puede reemplazar letras o plabras "tiene que estar escrito igual"
# si seba estaria en mayus no lo encuentra para reemplazar

# seperar cadena con la cadena que le pasemos 
cadena_separada = cadena1.split("s") #quita las s de la cadena y nos devuelve  en forma de lista ['hola ', 'oy ', 'eba']
print(type(cadena_separada) ) # type no es neces. lo ppnemos para saber que devuelve una list


