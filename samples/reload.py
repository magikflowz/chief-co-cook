import flet as ft
from flet import Page, Row, Text, KeyboardEvent

def main(page: Page):
    page.title = 'keyboard'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    #creating the text views
    key: Text = Text('Key', size=30)
    shift: Text = Text('Shift', size=30, color='blue')
    ctrl: Text = Text('ctrl', size=30, color='green')
    alt: Text = Text('Alt', size=30, color='red')
    meta: Text = Text('Meta', size=30, color='yellow')

    #handling the keyboard events
    def on_keyboard(e: KeyboardEvent):
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta
        print(e.data)
        page.update()
    
    #linking keyboard events
    page.on_keyboard_event = on_keyboard
    
    #creating our basic page
    page.add(
        Text("Press any button"),
        Row(
            controls=[key,shift,ctrl, alt,meta],
            alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == '__main__':
    ft.app(target=main)
