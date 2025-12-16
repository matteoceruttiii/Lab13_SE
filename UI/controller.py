import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model


# funzione che gestisce l'handler della creazione del grafo
    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        grafo = self._model.buildGraph()
        minimo = min(self._model.G.edges(data=True))
        massimo = max(self._model.G.edges(data=True))
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Numero di archi: {len(self._model.G.nodes())}'))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Informazioni sui pesi degli archi -'
                                                                   f'valore minimo: {minimo} '
                                                                   f'e valore massimo: {massimo}'))
        self._view.update()


# funzione che gestisce l'handler per il conteggio degli archi
    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        (min, max) = self._model.calcolaSoglia(e)
        self._view.lista_visualizzazione_2.clean()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {min}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {max}"))
        self._view.update()



# funzione che gestisce l'handler del problema ricorsivo sulla ricerca del cammino
    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        self._model.calcolaCammino(e)
        self._view.lista_visualizzazione_3.clean()
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Numero archi percorso più lungo: "))
        self._view.update()

