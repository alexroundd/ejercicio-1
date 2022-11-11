# 1- Declara dues variables float. Fes i mostra per pantalla (per aquest ordre) 

a = 1.5
b = 5.5

print (b-a)
print (a+b)
print (a**b)

a += 1
print (a)
a -= 2
print (a)

print (a%b)
print (a/b)
print (a//b)

# 2- Posa el teu nom en una variable string i mostra’l per pantalla.

name = ('alex round sen')
print (name)

# 3- Escriu un programa que ens digui si una persona és o no major d’edat.

edad = input ('cuantos años tienes?')
edad = int (edad)
if edad < 18:
    print ('eres menor de edad');
elif edad > 17:
    print ('eres mayor de edad');

# 4- Programa un algoritme que ens digui quina qualificació acadèmica té una persona en funció de la nota:

nota = input ('que nota tienes?')
nota = float (nota)
if nota < 5:
    print ('suspendido');
elif 5 < nota < 6:
    print ('bien');
elif 6 < nota < 8:
    print ('notable');
elif 8 < nota < 10:
    print ('excelente');

# 5- Programa el diagrama de flux que has presentat a classe.

s = "si"
respuesta1 = input ('tienes hambre?')

if respuesta1 == s:
    respuesta2 = input ('hay comida?');
else:
    print ('pos muy bien');

if respuesta2 == s:
    respuesta3 = input ('sabes cocinar?');
else:
    print ('ves a comprar');

