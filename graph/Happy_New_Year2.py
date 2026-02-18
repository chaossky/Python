import random
from pyfiglet import Figlet
from termcolor import colored

fonts=['slant','banner3-D','big','block',
       'bubble','digital','doom','isometric1',
       'mini','small','starwars']
colors=['red','green','yellow','blue',
        'magenta','cyan']

F=Figlet(font=random.choice(fonts))
print(colored(F.renderText("Happy New Year 2026"),
              random.choice(colors)))
