# Estructuras de datos: Introducción

"""Las estructuras de datos son formas de organizar y almacenar los datos en un programa de manera eficiente. Python ofrece varias estructuras 
    de datos integradas que facilitan la manipulación y el acceso a los datos."""
# Las estructuras de datos no son solo contenedores; son las herramientas que determinaran la eficienia, escalabilidad y legilibilidad de tu
# código

#* Lists ( Listas ): El caballo de batalla
"""Las listas son colecciones ordenadas y mutables que permiten almacenar
   - Cuándo usarlas: Cuando el orden importa y vas a estar agregando, eliminando o modificando elemnentos frecuentemente.
   - Sintaxis: Se definen usando corchetes [] y los elementos se separan por comas.
   - Contexto Backend: Una fila de mensajes pendientes por porcesar o una lista de publicaciones en un muro que se cargan cronológicamente."""
# Ejemplo: Lista de tareas
tasks = ["Validar email", "Limpiar DB", "Enviar Notificaciones"]
tasks.append("Genera Reporte") # Dinámico

#* Tuples ( Tuplas ): La integridad de los datos
"""Las tuplas son ordenadas pro inmutables (no cambian tras su creación).
   - Cuando usarlas: Para datos que representan una "unidad" o un registro fijo. Son más rápidas que las listas y protegen la integridad de los 
   datos (nadie puede cmbiar un valor por error).
   - Sintaxis: Se definen usando paréntesis () y los elementos se separan por comas.
   - Contexto Backend: Coordenadas geograficas (latidud, longitud) o configuraciones de conexión a la DB (host, puerto), o el retorno de 
   múltiples valores en una función."""
# Ejemplo: Configuración de servidor
DB_CONFIG = ("127.0.0.1", 5432, "damin_user")

#* Sets ( Conjuntos ): La búsqueda de la unicidad
"""Son desordenadas y sus elemetos son únicos.
   - Cuándo usarlas: Cuando necesitas eliminar duplicados automáticamente o realizar operaciones matemáticas (unión, intersección). Su gran 
   ventaja es que la búsqueda de un elemento es increiblemetne rápida: O(1).
   - Sintaxis: Se definen usando llaves {} o la función set().
   - Contexto Backend: Almacenar IDs de usuarios qeu están "online" en este momento (no quieres que el mismo ID aparezca dos veces)."""
# ejemplo: Tags únicos de un blog
tags = {"python", "backend", "api", "python"}
print(tags) # {'python', 'backend', 'api'} -> El duplicado desapareció

#* Dictionaries ( Diccionarios ): El rey del Backend
"""Estructuras de clave-valor. En Python, los diccionarios son la baase de casi todo, incluyendo los objetos y, por supuesto, el formato JSON.
   - Cuándo usarlas: Siempre qeu necesites mapear una etiqueta (clave) un dato (vlore). El la forma más eficiente de buscar información si 
   conoces la clave.
   - Sintaxis: Se definen usando llaves {} con pares clave-valor separados por comas. Cada par usa dos puntos : para separar clave y valor.
   - Contexto Backend: Prácticamente cualquier respuesta de una API REST es un diccionario converido a JSON."""


