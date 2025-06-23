import statistics

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._voli = DAO.getAllFlights()
        self._coppie_distanze = dict()
        for volo in self._voli:
            aeroporti = (sorted([volo[0], volo[1]]))
            coppia = (aeroporti[0], aeroporti[1])
            if coppia in self._coppie_distanze.keys():
                self._coppie_distanze[coppia].append(volo[2])
            else:
                self._coppie_distanze[coppia] = [volo[2]]
            #(aeroportoA, aeroportoB):[dist1, dist2, ...]
        self._grafo = nx.Graph()

    def seleziona_voli(self, dist_min):
        selezione_voli = list()
        for (a, b) in self._coppie_distanze.keys():
            distanza_media = statistics.mean(self._coppie_distanze.get((a, b)))
            if distanza_media >= dist_min:
                selezione_voli.append((a, b, distanza_media))
        return selezione_voli # lista di tuple (aeroportoA, aeroportoB, distMedia)

    def buildGraph(self, dist_min):
        selezione = self.seleziona_voli(dist_min)
        self._grafo.clear_edges()
        for arco in selezione:
            self._grafo.add_edge(arco[0], arco[1], weight=arco[2])

    def getInfoGrafo(self, dist_min):
        self.buildGraph(dist_min)
        return len(self._grafo.nodes), len(self._grafo.edges), list(self._grafo.edges(data = True))