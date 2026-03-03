import flet as ft

def main(page: ft.Page):
    page.title = "Aplicación Interactiva"
    page.padding = 20

    titulo = ft.Text("BIENVENIDO",
                    size=24, 
                    weight=ft.FontWeight.BOLD)

    nombre = ft.TextField(label="Nombre")

    tipo_evento = ft.Dropdown(
        label="Tipo de Evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Seminario")
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

    certificado = ft.Checkbox(label="¿Deseas certificado?")

    cantidad = ft.Slider(min=1,
                        max=10,
                        divisions=9, 
                        value=1,
                        label="{value}")

    resumen = ft.Text()

    def mostrar_resumen(e):
        resumen.value = f"""
Nombre: {nombre.value}
Evento: {tipo_evento.value}
Modalidad: {modalidad.value}
Certificado: {"Sí" if certificado.value else "No"}
Cantidad: {int(cantidad.value)}
"""
        page.update()

    boton = ft.ElevatedButton("Registrar", on_click=mostrar_resumen)

    page.add(
        titulo,
        nombre,
        tipo_evento,
        modalidad,
        certificado,
        cantidad,
        boton,
        ft.Divider(),
        resumen
    )

ft.app(target=main)