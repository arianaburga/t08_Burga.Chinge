#operacion-CONCATENACION 01
#    0         10        20        30
#    012345678901234567890123456789012345
str="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789"
#nombre y edad

#imput
#Edad y nombre
edad=(str[27]+str[35])
nombre=(str[10]+str[4]+str[22]+str[8]+str[13]+" "+str[2]+str[7]+str[8]+str[6]+str[13]+str[4])
print(nombre+" tiene "+edad+" años")



#operacion-CONCATENACION 02
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#input
#Pais y departamento
pais=(str.upper()[16]+str[4]+str[18]+str[21])
departamento=(str.upper()[11]+str[0]+str[12]+str[1]+str[0]+str[25]
              +str[4]+str[17]+str[4])
print("soy de:"+pais ," y vivo en el departamento de:"+departamento)




#operacion-CONCATENACION 03
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#input
#Nro de DNI Y estado civil
DNI=(str[34]+str[30]+str[29]+str[31]+str[29]+str[33]+str[27]+str[28])
civil=(str.upper()[19]+str[15]+str[20]+str[4]+str[18]+str[15])
print("Mi numero de DNI es:"+DNI+" Y mi estado civil:"+civil)



#operacion-CONCATENACION 04
#    0         10        20        30
#    012345678901234567890123456789012345678
str="abcdefghijklmnñopqrstuvwxyz0123456789@."
#MI correo elctronicao
a=(str[9]+str[15]+str[13]+str[2]+str[7]+str[8]+str[6]+str[13]+str[4]+
   str[28]+str[36]*3)
b=(str[37]+str[6]+str[12]+str[0]+str[8]+str[11]+str[38]+str[2]+str[15]+str[12])
print("mi correo Electronico es:"+a+b)



#operacion-CONCATENACION 05
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#sexo y Fecha de nacimiento
sexo=(str[12]+str[0]+str[19]+str[2]+str[21]+str[11]+str[8]+str[13]+str[15])
fecha=(str[28]+str[32]+" "+str[3]+str[4]+" "+str[3]+str[8]+str[2]+str[8]+str[4]+str[12]+str[1]+
       str[18]+str[4]+" "+str[3]+str[2]+" "+str[28]+str[36]*3)
print("Sexo:"+sexo+" Y fecha de nacimiento:"+fecha)



#operacion-CONCATENACION 06
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#coleguio de procedencia
a=(str.upper()[9]+str[15]+str[19]+str[4])
b=(str.upper()[12]+str[0]+str[18]+str[8]+str[0])
c=(str.upper()[0]+str[18]+str[6]+str[4]+str[3]+str[0]+str[19])
print("Colguio de procedencia:"+a+" "+b+" "+c)



#operacion-CONCATENACION 07
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#Carreara y curso
a=(str.upper()[8]+str.upper()[13]+str.upper()[6])
b=(str.upper()[4]+str[11]+str[4]+str[2]+str[20]+str[18]+str[15]+str[13]+str[8]+
   str[2]+str[0])
c=(str.upper()[16]+str[18]+str[15]+str[6]+str[18]+str[0]+str[12]+str[0]+str[2]+
   str[8]+str[15]+str[13])
print("Carrera profesional:"+a+" "+b+" y curso:"+c)



#operacion-CONCATENACION 08
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#La pelicula y su protagonista
a=(str.upper()[5]+str[18]+str[15]+str[26]+str[4]+str[13]+"'"+str.upper()[8]*2+"'")
b=(str.upper()[4]+str[11]+str[19]+str[0])
print("La pelicula:"+a+" y su protagonista es:"+b)




#operacion-CONCATENACION 09
#    0         10        20        30
#    0123456789012345678901234567890123456789
str="abcdefghijklmnñopqrstuvwxyz0123456789@.%"
#oro
a=(str[29]+str[28]+str[39])
b=(str[15]+str[18]+str[15])
c=(str.upper()[16]+str[4]+str[18]+str[21])
d=(str.upper()[11]+str[0]+" "+str.upper()[11]+str[8]+str[1]+str[4]+str[18]+
   str[20]+str[0]+str[3])
#output
print("El "+a+" de "+b+" del "+c+" esta en la reguion "+"'"+d+"'")



#operacion-CONCATENACION 10
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"
#Ganador del balon de oro
a=(str.upper()[11]+str[8]+str[15]+str[13]+str[4]+str[11])
b=(str.upper()[12]+str[4]+str[19]*2+str[8])
print("El balon de oro es para:"+a+" "+b+" :D")



#operacion-CONCATENACION 11
#Independencia del Peru
#input
a="Valparaiso"
b="Agosto"
c=1820
#output
print("La escuadra libertadora zarpo de: "+a+" en "+b+" de "+str(c))



#operacion-CONCATENACION 12
#Proclamacion de independencia
#input
a="28 de julio"
b=1821
c="San Marin"
d="Peru"
#output
print("El "+a+" de "+str(b)+" Don jose de "+c+" Proclamo la independencia del "+d)



#operacion-CONCATENACION 13
#El soldado de la ley

#input
a="Ramon Castilla"
b="El soldado de la LEY"
#outpup
print("Gracias a las grandes obras de "+a+"\n"
      " Fue apodado como:"+b)



#operacion-CONCATENACION 14
#El hombre del milenio

#input
a="Miguel Grau"
b="El hombre del milenio"
c="se le reconocio por todo el mundo"
#output
print("Traz los heroicos actos de:"+a+"\n"+
      " en la guerra con CHILE "+c+" como:"+"\n"+
      b)


#operacion-CONCATENACION 15
#Muerte T.T
#input
a="Chester Bennington"
b=2017
c="lloran su muerte"
#output
print("El vocalista de la banda de 'Linkin Park':"+a+"\n"+
      "murio el 20 de julio del "+str(b)+"\n"+
      "sus compañeros "+c +"    T.T")

