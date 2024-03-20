# definiendo una variable
nombre = "sebastian gonzalez vega" # nombre (variable) "sebastian go.." (definición)
edad = 37 
# concatenar con fstring
bienvenida =f"hola !! { nombre } { edad } ¿como estas?"
print (bienvenida)
# concatenar con +
bienvenida = "hola " + "¿como estas?"
print(bienvenida)
#operadores de pertencia (in and not in)
print ("hola" in bienvenida)  # in va a dar true (hola esta en variable bienvenida)
print ("chau" in bienvenida) # in va a dar falsa (chau no esta en variable bienvenida)
print ("hola" not in bienvenida) #not in va a dar false (hola si esta en variable bienvenida)
print ("chau" not in bienvenida) # not in va a dar true (chau no esta en variable bienvenida)
#variable con camelCase 
nombreCompletoDeTuTio = "Federico Gonzalez Vega" #todas las letras principales en mayus para separar (camelase)
#variable con snake_case (recomienda python)
nombre_completo_de_tu_tio = "Federico Gonzalez Vega" # todas las palabras separadas por guion (tipo serpiente)
print (nombre_completo_de_tu_tio)