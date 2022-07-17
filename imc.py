# calculadora de IMC
# definiendo varliabres

nombre = input("¿Cómo te llamas?")
try:
    peso = float(input("¿Cúantos Kg pesas?"))
    altura = float(input("¿Cúal es tu estatura expresada en metros?"))
except: 
    print("Error. Ingresa peso y altura en datos numéricos")
    exit()
#calculando IMC
IMC = peso / (altura ** 2)

# imprimir resultado
print ("Hola", nombre, "su IMC es: ", IMC)