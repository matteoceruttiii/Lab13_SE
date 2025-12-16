import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.DiGraph(data=True)
        self._dizionario_interazioni = {}
        self._lista_geni = []


# funzione che crea il grafo semplice, pesato e orientato
    def buildGraph(self):
        geni = DAO.getGene()
        self._lista_geni = geni

        # aggiungo i nodi al grafo (solo i cromosomi)
        for gene in geni:
            cromosoma = gene.cromosoma
            if cromosoma not in self.G.nodes() and cromosoma != 0:
                self.G.add_node(cromosoma)
                self._dizionario_interazioni[cromosoma] = gene

        # aggiungo gli archi pesati
        listaInterazioni  = DAO.getInterazione()
        for l in listaInterazioni:
            u_nodo = l.id_gene1
            v_nodo = l.id_gene2
            peso = float(l.correlazione)
            print(f"Nodo1: {u_nodo} - Nodo2: {v_nodo}, peso: {peso}")

            # aggiungo l'arco solo se non è presente
            if not (self.G.has_edge(u_nodo, v_nodo)):
                self.G.add_edge(u_nodo, v_nodo, peso=peso)


# funzione che calcola il numero di archi conoscendo la soglia
    def calcolaSoglia(self, soglia):
        pass


# funzione che crea l'algoritmo di ricorsione richiesto
    def calcolaCammino(self, soglia):
        pass