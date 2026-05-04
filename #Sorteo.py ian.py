#Sorteo
#ian dominguez
original =[49, 16, 80, 10, 56]
nueva = sorted(original)
desc = sorted(original, reverse=True)

print("Lista de participantes:", original)

print('ascendente:', original)
print('descendente:', original)
      
print('original:', original)
print('Ganador sorteo:', desc[0])