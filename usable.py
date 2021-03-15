from rich.console import Console
from rich.layout import Layout
from rich import print
import os

console = Console()


def printui():
    print()
    health = ''.join(' ' for i in range(10))
    stamina = "100"
    player_name = "Corengenie"
    player_floor = 14
#     console.print(f'''
# [bold green]Здоровье: [/bold green][white on green]{health}[/white on green]
# __ffhkfghkfghjffgggggggggggggggggggggh__
# [bold cyan]Will[/bold cyan]
#     ''', justify="center")

    layout = Layout()

    layout.split(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].split(
        Layout(name="tabs"),
        Layout(name="stats"),
        Layout(name="maplevel"),
        direction="horizontal"
    )

    layout["upper"]["tabs"].size = 3
    layout["upper"]["stats"].size = 27
    layout["upper"]["maplevel"].size = 70

    layout["upper"]["tabs"].update("")
    layout["upper"]["stats"].update(f'''


Персонаж: {player_name}
Этаж: {player_floor}

[bold green]Здоровье: [/bold green][white on green]{health}[/white on green]
[bold gold1]Выносливость: {stamina}[bold gold1]
Очки защиты: 10
Очки уворота: 2

    
    ''')
    print(layout)


if __name__ == '__main__':
    os.system("mode con cols=100 lines=60")
    printui()
