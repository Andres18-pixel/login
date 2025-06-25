usuarios = {"EALZ": "password"}

def login():
    print("\n" + "="*30)
    print(" "*10 + "INICIO DE SESIÓN" + " "*10)
    print("="*30 + "\n")
    
    usuario = input("│ Usuario: ")
    contraseña = input("│ Contraseña: ")
    print("-"*30)
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"\n│ ¡Bienvenido, {usuario}!")
        print("│" + "-"*29)
        
        with open("archivo.txt", "w") as documento:
            documento.write(f"usuario: {usuario} \ncontraseña: {contraseña}")
        return True
    else:
        print("\n│ Credenciales incorrectas")
        print("│" + "-"*29)
        return False

if login():
    print("\n" + "="*30)
    print("│ Acceso concedido")
    print("="*30)
else:
    print("\n" + "="*30)
    print("│ No se pudo iniciar sesión, inténtelo nuevamente")
    print("="*30)

    intentos = 1
    while intentos < 3:
        if login():
            print("\n" + "="*30)
            print("│ Acceso concedido")
            print("="*30)
            break
        else:
            intentos += 1
    else:
        print("\n" + "="*30)
        print("│ Demasiados intentos fallidos")
        print("│ Sistema bloqueado temporalmente")
        print("="*30)