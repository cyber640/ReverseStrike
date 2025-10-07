import random
import pyfiglet
from termcolor import colored
from rich.console import Console

console = Console()

# Create ASCII text
ascii_art = pyfiglet.figlet_format("REVERSESTRIKE", font="patorjk's_cheese")

# Random color list
colors = ["green"]
from termcolor import colored
import time, os


# Option 1: static color
colored_art = colored(ascii_art, color=random.choice(colors))
print(colored_art)

# Option 2: rainbow gradient using rich (uncomment to use)
# console.print(ascii_art, style="bold rainbow")

