# Conteo de Colisiones

Este directorio contiene la solución al problema de conteo de colisiones entre robots, parte de la prueba técnica de selección L3.

## Descripción del Problema

Dada una hilera de robots, cada uno representado con la letra `R` si se está desplazando hacia la derecha y `L` si se está desplazando hacia la izquierda, se debe escribir una función que determine cuántas veces colisiona cada robot, dados los siguientes supuestos:
- La distancia inicial entre ellos es de 2 metros.
- Cuando dos robots chocan, cambian de dirección instantáneamente.
- El espacio es infinito en cualquiera de las direcciones.

### Ejemplos

#### Ejemplo 1

- **Entrada:** `"RLRRLL"`
- **Salida Esperada:** `3`

#### Ejemplo 2

- **Entrada:** `"RRLL"`
- **Salida Esperada:** `0`

## Solución

La solución implementada está en el archivo `colisiones.py`. La función `conteo_colisiones` recibe una secuencia de símbolos `R` y `L` y devuelve el número total de colisiones.

### Código de la Función

```python
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

