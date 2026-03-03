import flet as ft

def main(page: ft.Page):
    page.title = "Aplicación Interactiva"
    page.padding = 20

    titulo = ft.Text("Bienvenido a nuestro registro",
                    size=30, 
                    weight=ft.FontWeight.BOLD)

    nombre = ft.TextField(label="Nombre")

    tipo_evento = ft.Dropdown(
        label="Tipo de Evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion")
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(label="¿Requiere inscripción previa?")

    cantidad_horas = ft.Slider(min=1,
                        max=10,
                        divisions=9, 
                        value=1,
                        label="{value}")

    resumen = ft.Text(
        size=15,
    color=ft.Colors.PINK,

    )

    def mostrar_resumen(e):
        resumen.value = f"""
Nombre: {nombre.value}
Evento: {tipo_evento.value}
Modalidad: {modalidad.value}
Inscripcion: {"Sí" if inscripcion.value else "No"}
Cantidad De Horas: {int(cantidad_horas.value)}
"""
        page.update()

    boton = ft.ElevatedButton("Registrar",
                            on_click=mostrar_resumen,
                            bgcolor=ft.Colors.BLUE,
                            color=ft.Colors.WHITE)

    page.add(
        titulo,
        nombre,
        tipo_evento,
        modalidad,
        inscripcion,
        cantidad_horas,
        boton,
        ft.Divider(),
        resumen
    )

ft.app(target=main)