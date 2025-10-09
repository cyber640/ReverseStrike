import random
import pyfiglet
from termcolor import colored
from rich.console import Console

console = Console()


ascii_art = pyfiglet.figlet_format("REVERSESTRIKE", font="patorjk's_cheese")


colors = ["green"]
from termcolor import colored
import time, os


colored_art = colored(ascii_art, color=random.choice(colors))
print(colored_art)



