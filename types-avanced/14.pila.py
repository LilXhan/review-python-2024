# LIFO -> last in first out

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimateEelement = pila.pop()
print(ultimateEelement)
print(pila)
print(pila[-1])

if not pila: # "", [], 0 -> FALSE
    print('empty list')

