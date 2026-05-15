import requests
from rich.console import Console

console = Console()

def iplookup():
    console.print("\n[bold cyan]─── IP TRACKER ───[/bold cyan]\n")
    
    lIP = console.input("[bold white] Enter IP Address: [/bold white]")
    url = f"http://ip-api.com/json/{lIP}"
    
    try:
        data = requests.get(url, timeout=10).json()

        if data.get("status") == "fail":
            console.print(f"[bold red]![/bold red] Error: {data.get('message')}")
        else:
            lat = data.get('lat')
            lon = data.get('lon')
            
            res = {
                "Target IP": data.get('query'),
                "Location ": f"{data.get('city')}, {data.get('country')} ({data.get('countryCode')})",
                "ISP      ": data.get('isp'),
                "GPS      ": f"{lat}, {lon}",
                "Maps     ": f"https://www.google.com/maps?q={lat},{lon}"
            }

            for key, value in res.items():
                console.print(f"[bold cyan]{key}[/bold cyan] [white]❯[/white] [bold white]{value}[/bold white]")

    except Exception as e:
        console.print(f"[bold red]![/bold red] Connection error: {e}")

    console.input("\n[cyan]❯[/cyan] Press Enter to return...")

if __name__ == "__main__":
    iplookup()
