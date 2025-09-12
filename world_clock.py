from datetime import datetime
import pytz
from rich.console import Console
from rich.table import Table

console=Console()
cities=["Asia/Kolkata","America/New_York","Europe/London","Asia/Tokyo"]
table=Table(title=" World Clock",style="cyan",show_header=True)
table.add_column("City",style="magenta",justify="center")
table.add_column("Current Time",style="green",justify="center")

for c in cities:
    tz=pytz.timezone(c)
    city_name=c.split('/')[1]
    current_time=datetime.now(tz).strftime("%H:%M:%S")
    table.add_row(city_name,current_time)
    
console.print(table)
   