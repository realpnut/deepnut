import time
import os
from rich.console import Console

console = Console()

def print_gradient_menu():
    console.print("[bold cyan]DEEPNUT v0.1 | WIP[/bold cyan]", justify="center")
    
    lines = [
        "╔═══════════════════════════════════════╗",
        "║               DEEPNUT                 ║",
        "╠═══════════════════════════════════════╣",
        "║                                       ║",
        "║  1. User Search (Sherlock)            ║",
        "║  2. IP Tracker (IP-API)               ║",
        "║                                       ║",
        "║  0. Exit                              ║",
        "║                                       ║",
        "╚═══════════════════════════════════════╝"
    ]

    colors = ["#00ffff", "#1affff", "#33ffff", "#4dffff", "#66ffff", "#80ffff", "#99ffff", "#b3ffff", "#ccffff", "#e6ffff", "#f2ffff", "#ffffff"]

    for i, line in enumerate(lines):
        color = colors[i] if i < len(colors) else "#ffffff"
        console.print(line, style=color, justify="center")

while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    print_gradient_menu()
    
    menu = input("\nSelect an option: ")

    if menu == "1":
        os.system("python3 mods/sherlock.py")
    elif menu == "2":
        os.system("python3 mods/iplookup.py")
    elif menu == "0":
        console.print("[bold red]Exiting...[/bold red]")
        break
    else:    
        console.print("[bold yellow]Invalid option. Please try again.[/bold yellow]") 
        time.sleep(1)
