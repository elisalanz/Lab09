import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        if self._view._dist_min.value == "":
            self._view.create_alert("Inserire una distanza minima!")
            return
        try:
            dist_min = int(self._view._dist_min.value)
        except ValueError:
            self._view.create_alert("Inserire un numero intero!")
            return
        (nNodi, nArchi, listaArchi) = self._model.getInfoGrafo(dist_min)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodi} vertici e {nArchi} archi.\nDi seguito, l'elenco di tutti gli archi (con relativa distanza):"))
        for arco in listaArchi:
            self._view.txt_result.controls.append(ft.Text(f"Volo tra aeroporto {arco[0]} e aeroporto {arco[1]} con distanza media: {arco[2]["weight"]} miglia"))
        self._view.update_page()


