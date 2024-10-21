import networkx as nx
import matplotlib.pyplot as plt

# Definindo pontos de interesse com coordenadas ajustadas para melhor visualização
localizacoes = {
    "Ginásio": (0, 0),
    "Refeitório": (10, 20),
    "Cantina": (15, 30),
    "Guarita": (25, 40),
    "Biblioteca e Pedagógico": (35, 50),
    "Auditório": (45, 15),
    "Laboratórios": (55, 30),
    "Galpão de Máquinas": (65, 5),
    "Salas de Aula": (75, 60),
    "Administrativo": (85, 20),
    "Estacionamento Descoberto": (95, 40),
    "Garagem Coberta Aberta": (105, 60),
    "Subestação": (115, 30)
}

# Criando um grafo para representar o mapa do campus
mapa_campus = nx.Graph()

# Adicionando os pontos de interesse ao grafo
for local, coordenada in localizacoes.items():
    mapa_campus.add_node(local, pos=coordenada)

# Definindo conexões entre os pontos de interesse e suas respectivas distâncias
conexoes_distancias = [
    ("Refeitório", "Ginásio", 20), ("Cantina", "Ginásio", 30), ("Guarita", "Ginásio", 40), 
    ("Biblioteca e Pedagógico", "Ginásio", 50), ("Auditório", "Ginásio", 60), 
    ("Laboratórios", "Ginásio", 30), ("Galpão de Máquinas", "Ginásio", 40), 
    ("Salas de Aula", "Ginásio", 60), ("Administrativo", "Ginásio", 25), 
    ("Estacionamento Descoberto", "Ginásio", 40), ("Garagem Coberta Aberta", "Ginásio", 50), 
    ("Subestação", "Ginásio", 40), ("Cantina", "Refeitório", 10), ("Guarita", "Refeitório", 30),
    ("Biblioteca e Pedagógico", "Refeitório", 25), ("Auditório", "Refeitório", 20), 
    ("Laboratórios", "Refeitório", 25), ("Galpão de Máquinas", "Refeitório", 40),
    ("Salas de Aula", "Refeitório", 30), ("Administrativo", "Refeitório", 20), 
    ("Estacionamento Descoberto", "Refeitório", 50), ("Garagem Coberta Aberta", "Refeitório", 55), 
    ("Subestação", "Refeitório", 60), ("Guarita", "Cantina", 35), ("Biblioteca e Pedagógico", "Cantina", 40),
    ("Auditório", "Cantina", 15), ("Laboratórios", "Cantina", 20), ("Galpão de Máquinas", "Cantina", 45),
    ("Salas de Aula", "Cantina", 35), ("Administrativo", "Cantina", 25), 
    ("Estacionamento Descoberto", "Cantina", 50), ("Garagem Coberta Aberta", "Cantina", 55), 
    ("Subestação", "Cantina", 60), ("Biblioteca e Pedagógico", "Guarita", 30), 
    ("Auditório", "Guarita", 40), ("Laboratórios", "Guarita", 25), ("Galpão de Máquinas", "Guarita", 40),
    ("Salas de Aula", "Guarita", 50), ("Administrativo", "Guarita", 20), 
    ("Estacionamento Descoberto", "Guarita", 60), ("Garagem Coberta Aberta", "Guarita", 70),
    ("Subestação", "Guarita", 40), ("Auditório", "Biblioteca e Pedagógico", 10), 
    ("Laboratórios", "Biblioteca e Pedagógico", 15), ("Galpão de Máquinas", "Biblioteca e Pedagógico", 35),
    ("Salas de Aula", "Biblioteca e Pedagógico", 20), ("Administrativo", "Biblioteca e Pedagógico", 15), 
    ("Estacionamento Descoberto", "Biblioteca e Pedagógico", 40), ("Garagem Coberta Aberta", "Biblioteca e Pedagógico", 50), 
    ("Subestação", "Biblioteca e Pedagógico", 45), ("Laboratórios", "Auditório", 25), 
    ("Galpão de Máquinas", "Auditório", 40), ("Salas de Aula", "Auditório", 30), 
    ("Administrativo", "Auditório", 20), ("Estacionamento Descoberto", "Auditório", 50), 
    ("Garagem Coberta Aberta", "Auditório", 55), ("Subestação", "Auditório", 40), 
    ("Galpão de Máquinas", "Laboratórios", 40), ("Salas de Aula", "Laboratórios", 30), 
    ("Administrativo", "Laboratórios", 20), ("Estacionamento Descoberto", "Laboratórios", 50), 
    ("Garagem Coberta Aberta", "Laboratórios", 60), ("Subestação", "Laboratórios", 50), 
    ("Salas de Aula", "Galpão de Máquinas", 40), ("Administrativo", "Galpão de Máquinas", 30), 
    ("Estacionamento Descoberto", "Galpão de Máquinas", 50), ("Garagem Coberta Aberta", "Galpão de Máquinas", 60), 
    ("Subestação", "Galpão de Máquinas", 55), ("Administrativo", "Salas de Aula", 30), 
    ("Estacionamento Descoberto", "Salas de Aula", 50), ("Garagem Coberta Aberta", "Salas de Aula", 60), 
    ("Subestação", "Salas de Aula", 55), ("Estacionamento Descoberto", "Administrativo", 40), 
    ("Garagem Coberta Aberta", "Administrativo", 50), ("Subestação", "Administrativo", 45), 
    ("Garagem Coberta Aberta", "Estacionamento Descoberto", 20), 
    ("Subestação", "Estacionamento Descoberto", 30), ("Subestação", "Garagem Coberta Aberta", 25)
]

# Adicionando conexões ao grafo
for conexao in conexoes_distancias:
    mapa_campus.add_edge(conexao[0], conexao[1], weight=conexao[2])

# Função para determinar o caminho mais curto usando o algoritmo de Dijkstra
def encontrar_caminho_mais_curto(grafo, inicio, destino):
    try:
        # Usando o algoritmo de Dijkstra para encontrar o caminho mais curto entre os pontos de interesse
        caminho_curto = nx.dijkstra_path(grafo, inicio, destino, weight='weight')
        distancia_total = nx.dijkstra_path_length(grafo, inicio, destino, weight='weight')
        print(f"Menor caminho entre {inicio} e {destino}: {caminho_curto}")
        print(f"Distância total: {distancia_total} unidades")
        return caminho_curto
    except nx.NetworkXNoPath:
        # Caso não exista caminho entre os pontos especificados
        print(f"Não existe caminho entre {inicio} e {destino}.")
        return []

# Exemplo: definir ponto de partida e ponto de chegada
ponto_inicial = "Guarita"
ponto_final = "Subestação"

# Encontrar o caminho mais curto entre dois pontos
menor_caminho = encontrar_caminho_mais_curto(mapa_campus, ponto_inicial, ponto_final)

# Destacar todos os caminhos e o caminho mais curto no gráfico
plt.figure(figsize=(14, 10))

# Definir cores para os nós
# Nós relacionados a estacionamento e garagem recebem uma cor diferente para destaque
cores_dos_nos = ['lightgreen' if 'Estacionamento' in no or 'Garagem' in no else 'lightblue' for no in mapa_campus.nodes]

# Extraindo informações de posição e peso das arestas
posicoes = nx.get_node_attributes(mapa_campus, 'pos')
pesos = nx.get_edge_attributes(mapa_campus, 'weight')

# Desenhando todas as conexões possíveis entre os pontos de interesse
nx.draw(
    mapa_campus,
    posicoes,
    with_labels=True,
    node_size=4000,
    node_color=cores_dos_nos,
    font_size=9,
    font_weight="bold",
    edge_color="gray",
    width=1
)

# Destacar o menor caminho em vermelho
if menor_caminho:
    # Desenha o caminho mais curto encontrado pelo algoritmo de Dijkstra
    arestas_caminho_curto = list(zip(menor_caminho, menor_caminho[1:]))
    nx.draw_networkx_edges(mapa_campus, posicoes, edgelist=arestas_caminho_curto, edge_color="red", width=4)

# Colocando rótulos de distância nas arestas
# Cada aresta é rotulada com seu respectivo peso, representando a distância entre os pontos
nx.draw_networkx_edge_labels(mapa_campus, posicoes, edge_labels=pesos, font_size=9)

# Exibir o gráfico final
plt.title("Mapa do Campus - Todos os Caminhos Possíveis e o Mais Curto", fontsize=15, fontweight="bold")
plt.show()
