#if True: 
    #accion se ejecuta
#if False:
    # accion no se ejecuta

# ejemplo

edad = 11
if edad >= 18: #si la edad es mayor o igual a 18 podes pasar 
    print( "podes pasar") 
    # lo que se escriba aqui forma parte del codicional
    
else:
    print("no podes pasar")    
    #lo que se escriba aqui forma parte del codicional
    
# aqui ya no forma parte

# ejemplo 2 contraseñas 

contraseña_almacenada = "soysebas" #si son iguales (==) "iniciando sesion " if
contraseña_escrita = "soysebas" #si son diferentes "contraseña incorrcta" else
 
if contraseña_almacenada == contraseña_escrita:
   print( "INICIANDO SESION ....") 
else:
    print("contraseña incorrecta" )    
 