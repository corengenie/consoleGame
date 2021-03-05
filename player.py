from usable import clear
from rich.console import Console


console = Console()


def end_game(string, stat=0):
    clear()
    console.print(f'''
Привет [red]{string}[/red]!
Если ты видишь это сообщение, значит мобы оказались сильнее тебя...
За время игры ты убил {stat} мобов и {stat} боссов.
Тебе нанесли {stat} урона.

Хочешь взять реванш? <[green]Д[/green]/[red]Н[/red]>''', justify='center')
    i = input()
    if i in ('exit', 'e'):
        exit()


class Player:

    x, y = None, None

    stats = {
        'magic_res' : 10,
        'physical_res' : 10,
    }

    def __init__(self, name):
        self.max_health = 100
        self.current_health = 100
        self.name = name

        print(self.stats.get('magic_res'))

    def hurt(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            end_game(self.name)

    def heal(self, healing):
        self.current_health += healing
        if self.current_health >= self.max_health: self.current_health = self.max_health
