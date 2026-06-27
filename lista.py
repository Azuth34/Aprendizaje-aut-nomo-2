lista_canciones = [
    "Milo J - Rara Vez (Apoyo a Artistas Emergentes)", 
    "Pódcast - El Impacto de la IA en el Empleo", 
    "Duki - Rockstar (Cultura Urbana)",
    "Pódcast - Salud Mental y Redes Sociales"
]

historial_reproduccion = []
programa_activo = True
limite_diario = 5

def filtrar_podcasts(lista):
    return [c for c in lista if "Pódcast" in c]

def calcular_minutos(historial):
    return len(historial) * 3

while programa_activo:
    print("\n=======================================================")
    print("      🌱 ECO-SOUNDS: TECNOLOGÍA Y SOCIEDAD 🌱    ")
    print("=======================================================")
    print("1. Ver biblioteca de contenido social y local")
    print("2. Seleccionar y reproducir contenido")
    print("3. Ver historial e impacto")
    print("4. Filtrar solo Pódcasts educativos")
    print("5. Salir del sistema")
    print("=======================================================")
    
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        print("\n--- 📜 CONTENIDO DISPONIBLE ---")
        for posicion, cancion in enumerate(lista_canciones, start=1):
            print(f"[{posicion}] - {cancion}")
            
    elif opcion == "2":
        if len(historial_reproduccion) >= limite_diario:
            print("\n⚠️ Alerta: Has alcanzado el límite de uso responsable por hoy.")
        else:
            print("\n--- 🎵 REPRODUCIR CONTENIDO ---")
            try:
                numero_elegido = int(input("Introduce el número del contenido: "))
                if 1 <= numero_elegido <= len(lista_canciones):
                    cancion_actual = lista_canciones[numero_elegido - 1]
                    print(f"\n▶️ Transmitiendo: {cancion_actual} 🔥")
                    historial_reproduccion.append(cancion_actual)
                else:
                    print("\n❌ Error: Ese número no está en la lista.")
            except ValueError:
                print("\n❌ Error: Debes ingresar un número válido.")
                
    elif opcion == "3":
        print("\n--- 📊 ESTADÍSTICAS DE USO ---")
        if not historial_reproduccion:
            print("No has reproducido contenido en esta sesión.")
        else:
            print(f"⏱️ Tiempo total escuchado: {calcular_minutos(historial_reproduccion)} minutos.")
            print(f"🔄 Contenidos reproducidos: {len(historial_reproduccion)}")
            print("\n📝 Detalle de lo escuchado:")
            for item in historial_reproduccion:
                print(f" -> {item}")
                
    elif opcion == "4":
        print("\n--- 🎙️ PÓDCASTS DE CONCIENTIZACIÓN ENCONTRADOS ---")
        podcasts = filtrar_podcasts(lista_canciones)
        for p in podcasts:
            print(f" -> {p}")
                
    elif opcion == "5":
        print("\n👋 Cerrando Eco-Sounds. ¡Gracias por usar la plataforma!")
        programa_activo = False  
        
    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")
