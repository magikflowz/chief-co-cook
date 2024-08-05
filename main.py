from flet import * 
import flet 
import datetime 
import threading as th

class Input(UserControl):

    def __init__(self,hint_text,icon, password=False):
        super().__init__(),
        self.hint_text = hint_text
        self.icon = icon
        self.password = password
    
    def build(self):
        return Container(
            Row([
                Icon(
                    self.icon,
                    color='white'
                ),
            TextField(
                border='OUTLINE',
                border_color='black',
                color='white',
                cursor_color='white',
                height=40,
                text_style=TextStyle(
                    size=18,
                    font_family='assets/fonts/Adequate-ExtraLight.ttf'
                ),
                password = self.password,
                hint_text = self.hint_text,
                hint_style=TextStyle(
                    size=18,
                    weight='w500',
                    color='white'
                )
            )
        ]), border=border.only(bottom=BorderSide(1, 'white'))
    )

class Button(UserControl):

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.btn = Container(
            Text(
                self.text,
                color = 'white',
                font_family='assets/fonts/Adequate-ExtraLight.ttf',
                weight='w400'
            ),
            border=border.all(1, 'white'),
            border_radius=3,
            padding=padding.only(10,3,10,3),
            alignment=alignment.center,
            on_hover=self.Hover,
            animate=animation.Animation(250),
        )
    
    def Hover(self, e):
        if self.btn.bgcolor == '540b6e65':
            self.btn.bgcolor ='transparent'
        else:
            self.btn.bgcolor = '#540b6e65'
        self.btn.update()

    def build(self):
        return self.btn
    
class TimeLine(UserControl):

    def __init__(self):
        super().__init__()
        self.now = datetime.datetime.now()
        self.date = self.now.strftime("%A, %B %d")
        self.time = self.now.strftime("%H:%M")


    def build(self):
        return Container(
            Column([
                Text(
                    self.date,
                    color='white',
                    size=20,
                    font_family='assets/fonts/Adequate-ExtraLight.ttf',
                )
            ],alignment='center'),
            width=300,
            height=100,
        )

body = Container(
    Stack([
        Image(
            src='kitch2.png',
            width=360,
            height=640,
            top=0
        ),
        Container(
            TimeLine(),
            top=60,
            width=300,
            left=30,
            height=80,
            
        ),
        Container(
            Text(
                "Welcome to the Co-Cooking Experience",
                font_family='assets/fonts/Adequate-ExtraLight.ttf',
                size=18 
            ),
            top=170,
            #width=300,
            left=10,
            height=30,

        ),

        Container(
            Column([
                Input("Username", icons.PERSON),
                Input("Password", icons.PASSWORD, password=True),
                Container(
                    Row([
                        Button("Sign Up"),
                        Button("Sign in"),
                    ], alignment='center', spacing=30)
                )
            ], alignment='30'),
            width=260,
            height=280,
            top=400,
            left=50,
            # bgcolor='red',
        )
    ]),
    width=360,
    height=640
)

def manage(page: Page):
    page.window_width = 360
    page.window_height = 640
    page.window_max_width = 360
    page.window_max_height = 640
    page.padding = 0
    page.add(
        body
    )

flet.app(target=manage)