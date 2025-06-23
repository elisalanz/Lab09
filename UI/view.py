import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP Lab 09"
        self._page.horizontal_alignment = 'CENTER'
        self._controller = None
        self._title = None
        self._dist_min = None
        self._btn = None


    def load_interface(self):
        self._title = ft.Text("Flights Manager", color="blue", size=24)
        self._page.controls.append(self._title)
        self._dist_min = ft.TextField(label="Distanza Minima", width=400, hint_text="Inserire la distanza minima (in miglia)")
        self._btn_analizza = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handle_analizza)
        row1 = ft.Row([self._dist_min, self._btn_analizza],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
