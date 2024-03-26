# and, or, not

gas = True
ignition = False
age = 18

if ignition and age >= 18 and gas:
    print("Nice")
if ignition and gas:
    print("Corte circuito")
if gas or ignition:
    print("Corte circuito")
