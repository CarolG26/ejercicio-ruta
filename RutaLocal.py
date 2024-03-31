#librería 'networkx', nos sirve para trabajar con grafos y encontrar rutas óptimas en un sistema de transporte

import networkx as nx

# Crear un grafo dirigido para representar las conexiones entre lugares
G = nx.DiGraph()

# Definir la base de conocimiento con las reglas lógicas que describe conexiones y distancias entre lugares
conexiones = [("Terreros", "VillaMayor", 10), 
              ("Terreros", "CAD", 15), 
              ("VillaMayor", "Gobernacion", 20), 
              ("CAD", "Gobernacion", 10), 
              ("CAD", "El Dorado", 5), 
              ("Gobernacion", "Puente Aereo", 15), 
              ("El Dorado", "Puente Aereo", 7), 
              ("Puente Aereo", "Aeropuerto", 12)]

# Agregar nodos y aristas al grafo con sus respectivas distancias
for origen, destino, distancia in conexiones:
    G.add_edge(origen, destino, weight=distancia)

# Punto de partida y llegada
origen = "Terreros"
destino = "Aeropuerto"

# Encontrar la ruta más corta entre dos lugares
mejor_ruta = nx.shortest_path(G, origen, destino, weight='weight')
distancia_mejor_ruta = nx.shortest_path_length(G, origen, destino, weight='weight')

print(f"La mejor ruta desde {origen} hasta {destino} es: {mejor_ruta}, con una distancia de {distancia_mejor_ruta}")
