# Aprendizaje-aut-nomo-2

lista_canciones = [
    "Milo J - Rara Vez", 
    "Babydoll", 
    "Duki - Rockstar",
    "Daddy Yankee BZRP"
]


programa_activo = True



while programa_activo == True:
    
    print("\n=======================================")
    print("      🎧 SPOTIFY CONSOLA EDITION 🎧    ")
    print("=======================================")
    print("1. Ver mi biblioteca de canciones")
    print("2. Seleccionar y reproducir canción")
    print("3. Apagar reproductor (Salir)")
    print("=======================================")
    

    opcion = input("Selecciona una opción (1-3): ")
    
   
    if opcion == "1":
        print("\n--- 📜 TU BIBLIOTECA DE MÚSICA ---")
       
        for posicion, cancion in enumerate(lista_canciones, start=1):
            print(f"[{posicion}] - {cancion}")
            
    elif opcion == "2":
        print("\n--- 🎵 REPRODUCIR UNA CANCIÓN ---")
      
        numero_elegido = int(input("Introduce el número de la canción: "))
        
      
        if 1 <= numero_elegido <= len(lista_canciones):
            cancion_actual = lista_canciones[numero_elegido - 1]
            print(f"\n▶️ ¡Reproduciendo ahora mismo: {cancion_actual}! 🔥")
        else:
            print("\n❌ Error: Ese número de canción no está en tu biblioteca.")
            
    elif opcion == "3":
        print("\n👋 Cerrando Spotify Consola. ¡Gracias por escuchar!")
        programa_activo = False  
        
    else:
        print("\n❌ Opción no válida. Por favor, marca 1, 2 o 3.")

