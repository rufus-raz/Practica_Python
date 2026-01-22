"""
Tienes la siguiente cadena de texto que representa un producto en un inventario: 
dato_sucio = " proDuCTo-125:Laptops-Gamer:2500.50 "
Tu objetivo es transformarla para obtener este resultado final:
ID: 000125 | Categoría: LAPTOPS-GAMER | Precio: $2,500.50

"""
dato_sucio = "  proDuCTo-125:Laptops-Gamer:2500.50   "

# 1 y 2. Limpiar y dividir
partes = dato_sucio.strip().split(":") 
# partes ahora es ['proDuCTo-125', 'Laptops-Gamer', '2500.50']

# 3. Procesar el ID
# Reemplazamos el prefijo y rellenamos con ceros
id_limpio = partes[0].replace("proDuCTo-", "").zfill(6)

# 4. Procesar Categoría
categoria = partes[1].upper()

# 5. Precio (opcional: convertir a número para formatear)
precio = float(partes[2])

# Resultado final
resultado = f"ID: {id_limpio} | Categoría: {categoria} | Precio: ${precio:,.2f}"

print(resultado)
