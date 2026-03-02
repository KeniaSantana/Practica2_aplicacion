import flet as ft 
def main (page: ft.Page):
    page.title="Aplicación Interactiva"
    page.padding=20
    
    titulo=ft.Text(
    value="BIENVENIDO",
    size=24,
    weight=ft.FontWeight.BOLD
)
    nombre=ft.TextField(
    label="Nombre",
    hint_text="Ingresa tu nombre",
    )

    tipo_evento=ft.Dropdown(
        label="Tipo de Eventos",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Seminario")
        ],
        value="Conferencia"
    )
    modalidad=ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual")
        ]),
        value="Presencial"
    )
    
    certificado=ft.Checkbox(
        label="¿Deseas el certificado?",
        value=False
    )
    
    cantidad=ft.Slider(
        min=1,
        max=10,
        divisions=9,
        label="{value}",
        value=1
    )
    
    
ft.run(main)
