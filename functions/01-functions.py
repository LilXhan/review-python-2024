def greeting(name, lastname):
    print("Hello World")
    print(f"Welcome {name} {lastname}")

greeting("Flavio", "Alvarado Tucto")
greeting("Chanchito", "happy")

# optional

def greeting2(name, lastname=""):
    print("hello world")
    print(f"welcome {name} {lastname}")

greeting2("Nicolas")
greeting2("Chanchito", "Feliz")


greeting(lastname="Alvarado Tucto", name="Flavio")