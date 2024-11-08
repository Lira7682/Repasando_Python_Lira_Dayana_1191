print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print (" ")#espacio

nota = float(input("Introduce tu nota: ")) #solicita ingresar nota
if 0 <= nota < 5: #abriendo if
    print("reprobado") #imprime texto
elif 5 <= nota < 6: #abriendo elif
    print("pasate") #imprime texto
elif 6 <= nota < 7: #abriendo elif
    print("bien") #imprime texto
elif 7 <= nota < 9: #abriendo elif
    print("muy bien") #imprime texto
elif 9 <= nota <= 10: # abriendo elif
    print("demasiado bien ") #imprime texto
else: #verifica si la condicion es falsa
    print("no valido") #imprime texto

print(" ") #espacio