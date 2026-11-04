import flet as ft

def main(page: ft.Page):
    page.title = "Portal de Autogestión Institucional"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Componentes de la interfaz
    titulo = ft.Text("Portal Educativo - Consultas y Turnos", size=22, color="black", weight=ft.FontWeight.BOLD)
    subtitulo = ft.Text("Comunidad Educativa IES N° 1", size=14, color="black")
    
    input_dni = ft.TextField(
        label="Ingrese su DNI", 
        width=300, 
        keyboard_type=ft.KeyboardType.NUMBER,
        max_length=8,
        prefix_icon="person"
    )
    
    resultado = ft.Text("", size=14, text_align=ft.TextAlign.CENTER)

    def consultar_estado(e):
        if not input_dni.value or not input_dni.value.isdigit() or len(input_dni.value) != 8:
            resultado.value = "⚠️ Error: Debe ingresar un DNI válido de 8 dígitos numéricos."
            resultado.color = "red"
        else:
            # Simulación de respuesta institucional
            resultado.value = (
                f"✅ DNI: {input_dni.value}\n"
                f"• Estado de trámites: Al día\n"
                f"• Próximo examen: 15/11/2026\n"
                f"• Turno administrativo asignado: No posee pendientes."
            )
            resultado.color = "green"
        page.update()

    btn_consultar = ft.Button(
        "Consultar Estado / Turno", 
        "search",
        on_click=consultar_estado
    )

    # Contenedor principal estructurado en tarjeta
    panel = ft.Container(
        content=ft.Column(
            [
                titulo,
                subtitulo,
                ft.Divider(height=20),
                input_dni,
                btn_consultar,
                ft.Container(content=resultado, padding=10)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=30,
        border_radius=12,
        bgcolor="#F0F0F0",
        width=420
    )

    page.add(panel)

if __name__ == "__main__":
    ft.run(main)