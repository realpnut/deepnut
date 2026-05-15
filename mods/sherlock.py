import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_sherlock():
    legal_info = """
    [bold cyan]Deepnut Search Module[/bold cyan]
    This module acts as a wrapper for [bold white]Sherlock Project[/bold white].
    Sherlock is licensed under the MIT License.
    Copyright (c) 2026 Sherlock Project
    """
    console.print(Panel(legal_info, border_style="cyan"))

    username = console.input("\n[bold cyan]Enter username to investigate: [/bold cyan]")
    
    if not username:
        console.print("[red]Error: Username cannot be empty![/red]")
        return

    try:
        os.system(f"sherlock {username}")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")

    input("\n[cyan]>[/] Press Enter to return to Deepnut Menu...")

if __name__ == "__main__":
    run_sherlock()
