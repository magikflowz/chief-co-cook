import flet as ft
from flet import(UserControl,
                 TextField,
                 InputBorder,
                 Page,
                 ControlEvent,
                 app,
                 FloatingActionButton)

class TextEditor(UserControl):
    
    def __init__(self):
        super().__init__()
        self.textfield = TextField(multiline=True,
                                   autofocus=True,
                                   border=InputBorder.NONE,
                                   min_lines=40,
                                   content_padding=30,
                                   cursor_color='yellow')
        
    def save_text(self, e: ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self):
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = 'Welcome to the text editor'

    def build(self):
        self.textfield.value = self.read_text()
        return self.textfield
    
def main(page: Page):
    page.title = 'notepad'
    page.scroll = True

    page.add(TextEditor())

if __name__ == '__main__':
    app(target=main)