# Comando: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

#--------------------------------------------------------------
#            CONVERSAO DE DISTANCIA
#--------------------------------------------------------------

dist = float(input("Digite uma distancia em metros: "))

dam = dist / 10
hm = dam / 10
km = hm / 10
dm = dist * 10
cm = dm * 10
mm = cm * 10

print(f"A distancia de {dist}m corresponde a: ")
print(f"{km}km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")