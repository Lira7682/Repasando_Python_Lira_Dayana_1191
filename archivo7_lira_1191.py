print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
def tri_recursion(k):#define la funcion
  if(k > 0):#verifica si es verdadera 
    result = k + tri_recursion(k - 2)#secuencia de operacion
    print(result)#imprime resultado 
  else:#verifica si es falsa
    result = 0  #resultado si es falsa
  return result #regresa el resultado

print("\n\nRecursion Example Results")
tri_recursion(100)#numero de secuencia
print(" ")#espacio