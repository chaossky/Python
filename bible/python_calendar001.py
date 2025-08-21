import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console=Console()
    months=[calendar.monthcalendar(year, m) for m in range(1, 13)]
    
    for month in range(12):
        month_name=calendar.month_name[month + 1]
        
        table=Table(title=f"[bold cyan]{month_name} ({year})[/bold cyan]",show_lines=True)
        table.add_column("Mon", style="green", justify="center")
        table.add_column("Tue", style="green", justify="center")
        table.add_column("Wed", style="green", justify="center")
        table.add_column("Thu", style="green", justify="center")
        table.add_column("Fri", style="green", justify="center")    
        table.add_column("Sat", style="blue", justify="center")
        table.add_column("Sun", style="red", justify="center")
        for week in months[month]:
            table.add_row(*[str(day) if day != 0 else "" for day in week])
            
        console.print(table)
        console.print("\n")
        
colorful_calendar(2025)
        

    