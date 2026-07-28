from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from rich.console import Console
from rich.panel import Panel

console = Console()


def metadata():
    legal_info = """
[bold cyan]Deepnut Metadata Reader Module[/bold cyan]

This module extracts metadata from image files.

Supported data:
- Camera information
- Software information
- Creation dates
- GPS coordinates (if available)

Built using [bold white]Pillow[/bold white].
Use only with files you are authorized to analyze. Or dont. Just dont do anything illegal.
    """
    console.print(Panel(legal_info, border_style="cyan"))
    console.print("\n[bold cyan]─── METADATA READER ───[/bold cyan]\n")
    file = console.input("[bold white] Enter image path: [/bold white] ")
    try:
        image = Image.open(file)
        exif = image.getexif()
        if not exif:
            console.print(
                "[bold yellow]![/bold yellow] No metadata found"
            )
        else:
            res = {}
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_data = {}
                    for gps_id in value:
                        gps_tag = GPSTAGS.get(gps_id, gps_id)
                        gps_data[gps_tag] = value[gps_id]
                    res["GPS"] = gps_data
                else:
                    res[tag] = value

            for key, value in res.items():
                console.print(
                    f"[bold cyan]{key}[/bold cyan] "
                    f"[white]❯[/white] "
                    f"[bold white]{value}[/bold white]"
                )

    except FileNotFoundError:
        console.print(
            "[bold red]![/bold red] File not found"
        )

    except Exception as e:
        console.print(
            f"[bold red]![/bold red] Error: {e}"
        )

    console.input("\n[cyan]❯[/cyan] Press Enter to return...")


if __name__ == "__main__":
    metadata()
