import flet as ft
from flet import Text, Row, Column, UserControl, Page, ControlEvent, ElevatedButton

class IncrementCounter(UserControl):
    def __init__(self, text: str, start_number: int = 0):
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: Text = Text(value=str(start_number), size=40)

    def increment(self, e: ControlEvent):
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()
    
    def decrement(self, e: ControlEvent):
        self.counter -= 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self):
        return Row(controls=[ft.Text(value=self.text, size=40), ElevatedButton(text='+', on_click=self.increment),
                             self.text_number,
                             ElevatedButton(text='-', on_click=self.decrement),
                             ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    width=300)

def main(page: Page):
    page.title ='Reuse'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    #TODO: 3 increments
    page.add(IncrementCounter('People',3))
    page.add(IncrementCounter('Animals', 4))
    page.add(IncrementCounter('Cars', 3))


if __name__ == '__main__':
    ft.app(target=main)