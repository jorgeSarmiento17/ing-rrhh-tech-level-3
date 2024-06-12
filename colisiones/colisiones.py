# colisiones/colisiones.py

def conteo_colisiones(secuencia):
    colisiones = 0
    robots = list(secuencia)
    
    while True:
        choque_ocurrido = False
        nuevos_robots = robots[:]
        
        for i in range(len(robots) - 1):
            if robots[i] == 'R' and robots[i + 1] == 'L':
                nuevos_robots[i] = 'L'
                nuevos_robots[i + 1] = 'R'
                choque_ocurrido = True
                colisiones += 1
        
        if not choque_ocurrido:
            break
        
        robots = nuevos_robots
    
    return colisiones

# Ejemplo de uso
if __name__ == "__main__":
    secuencia = "RLRRLL"
    print(conteo_colisiones(secuencia))  # Salida esperada: 3
