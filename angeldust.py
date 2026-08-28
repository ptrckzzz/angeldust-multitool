import os
import sys
import platform
import socket
import tempfile
import shutil
import hashlib
import base64
import requests
import psutil
from pystyle import Colors, Colorate, Center

from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

console = Console()

RED = "#ff0055"
PURPLE = "#a805ff"
PINK = "#ff00aa"
WHITE = "#ffffff"

ASCII_ART = """
                          (                   
   (                    ( )\ )             )  
   )\         (  (    ( )(()/(    (     ( /(  
((((_)(  (    )\))(  ))((_)(_))  ))\ (  )\()) 
 )\ _ )\ )\ )((_))\ /((_)(_))_  /((_))\(_))/  
 (_)_\(_)(_/( (()(_|_))| ||   \(_))(((_) |_   
  / _ \| ' \)) _` |/ -_) || |) | || (_-<  _|  
 /_/ \_\_||_|\__, |\___|_||___/ \_,_/__/\__|  
             |___/                            
"""

DISCORD_INVITE = "https://discord.gg/8wRzTTVtTE"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear()
    print(Colorate.Horizontal(Colors.red_to_purple, ASCII_ART))
    print(Center.XCenter(Colorate.Horizontal(Colors.purple_to_red, "[ ANGELDUST MULTI-TOOL v1.0 // SYSTEM DIAGNOSTICS & NETWORK HUD ]")))
    print("\n")

def print_menu():
    t1 = Table(title=f"[{PURPLE}]SYSTEM TOOLS[/]", border_style=PURPLE, show_header=False, box=None, padding=(0, 1))
    t1.add_column("ID", justify="center")
    t1.add_column("Name")
    t1.add_row(f"[{RED}][01][/]", f"[{WHITE}]System Summary[/]")
    t1.add_row(f"[{RED}][02][/]", f"[{WHITE}]Hardware Telemetry[/]")
    t1.add_row(f"[{RED}][03][/]", f"[{WHITE}]Disk Partition Usage[/]")
    t1.add_row(f"[{RED}][04][/]", f"[{WHITE}]Active Processes Top 10[/]")
    t1.add_row(f"[{RED}][05][/]", f"[{WHITE}]Battery & Power Status[/]")

    t2 = Table(title=f"[{PURPLE}]NETWORK TOOLS[/]", border_style=PURPLE, show_header=False, box=None, padding=(0, 1))
    t2.add_column("ID", justify="center")
    t2.add_column("Name")
    t2.add_row(f"[{RED}][06][/]", f"[{WHITE}]Show Public & Local IP[/]")
    t2.add_row(f"[{RED}][07][/]", f"[{WHITE}]Host Latency Ping[/]")
    t2.add_row(f"[{RED}][08][/]", f"[{WHITE}]DNS Lookup[/]")
    t2.add_row(f"[{RED}][09][/]", f"[{WHITE}]IP Geolocation Lookup[/]")
    t2.add_row(f"[{RED}][10][/]", f"[{WHITE}]Local Port Checker[/]")

    t3 = Table(title=f"[{PURPLE}]UTILITIES[/]", border_style=PURPLE, show_header=False, box=None, padding=(0, 1))
    t3.add_column("ID", justify="center")
    t3.add_column("Name")
    t3.add_row(f"[{RED}][11][/]", f"[{WHITE}]Secure Password Gen[/]")
    t3.add_row(f"[{RED}][12][/]", f"[{WHITE}]Base64 Encoder/Decoder[/]")
    t3.add_row(f"[{RED}][13][/]", f"[{WHITE}]Flush Temp Files[/]")
    t3.add_row(f"[{RED}][14][/]", f"[{WHITE}]Hash Generator[/]")
    t3.add_row(f"[{RED}][15][/]", f"[{WHITE}]Exit Multi-Tool[/]")

    p1 = Panel(t1, border_style=PURPLE, padding=(0, 1))
    p2 = Panel(t2, border_style=PURPLE, padding=(0, 1))
    p3 = Panel(t3, border_style=PURPLE, padding=(0, 1))

    columns = Columns([p1, p2, p3], equal=True, expand=True)
    console.print(columns)

    gradient_text = Text()
    msg = "JOIN OUR DISCORD COMMUNITY: "
    colors = ["#ff0055", "#e0026e", "#c10488", "#a206a1", "#8308ba", "#640ad3", "#450cec"]
    for i, char in enumerate(msg):
        gradient_text.append(char, style=colors[i % len(colors)])

    disc_panel = Panel(
        Text.assemble(gradient_text, (DISCORD_INVITE, f"{RED} underline link {DISCORD_INVITE}")),
        border_style=RED,
        subtitle=f"[{PURPLE}]CTRL + CLICK TO OPEN[/]",
        subtitle_align="right"
    )
    console.print(disc_panel)
    print("\n")

def sys_info():
    print_header()
    console.print(f"[{PURPLE}][+] OS:[/] {platform.system()} {platform.release()} ({platform.version()})")
    console.print(f"[{PURPLE}][+] Architecture:[/] {platform.machine()}")
    console.print(f"[{PURPLE}][+] Processor:[/] {platform.processor()}")
    console.print(f"[{PURPLE}][+] Hostname:[/] {socket.gethostname()}")

def hw_telemetry():
    print_header()
    console.print(f"[{PURPLE}][+] CPU Load:[/] {psutil.cpu_percent(interval=1)}%")
    console.print(f"[{PURPLE}][+] CPU Cores:[/] {psutil.cpu_count(logical=False)} Physical / {psutil.cpu_count(logical=True)} Logical")
    ram = psutil.virtual_memory()
    console.print(f"[{PURPLE}][+] RAM Usage:[/] {ram.percent}% ({ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB)")

def disk_usage():
    print_header()
    for disk in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(disk.mountpoint)
            console.print(f"[{PURPLE}][+] Partition {disk.device}:[/] Free: {usage.free // (1024**3)} GB / Total: {usage.total // (1024**3)} GB ({usage.percent}% used)")
        except PermissionError:
            continue

def top_processes():
    print_header()
    console.print(f"[{PINK}]Top 10 Processes by Memory Usage:[/\n")
    procs = sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), key=lambda p: p.info['memory_percent'], reverse=True)[:10]
    for p in procs:
        console.print(f"  [{RED}]•[/] PID: {p.info['pid']} | Name: {p.info['name']} | RAM: {p.info['memory_percent']:.2f}%")

def battery_status():
    print_header()
    battery = psutil.sensors_battery()
    if battery:
        plugged = "Plugged In" if battery.power_plugged else "Running on Battery"
        console.print(f"[{PURPLE}][+] Battery Percentage:[/] {battery.percent}%")
        console.print(f"[{PURPLE}][+] Power State:[/] {plugged}")
    else:
        console.print(f"[{RED}][!] No battery detected (Desktop PC)[/]")

def network_ip():
    print_header()
    try:
        pub_ip = requests.get('https://api.ipify.org', timeout=5).text.strip()
        console.print(f"[{PURPLE}][+] Public IP:[/] {pub_ip}")
    except:
        console.print(f"[{RED}][!] Unable to retrieve public IP[/]")
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    console.print(f"[{PURPLE}][+] Local IP:[/] {local_ip}")

def ping_host():
    print_header()
    target = input("Enter target host or IP (e.g. 8.8.8.8 or google.com): ").strip()
    if target:
        param = '-n' if platform.system().lower()=='windows' else '-c'
        os.system(f"ping {param} 4 {target}")

def dns_lookup():
    print_header()
    domain = input("Enter domain for DNS resolution (e.g. discord.com): ").strip()
    if domain:
        try:
            ip = socket.gethostbyname(domain)
            console.print(f"\n[{PURPLE}][+] Target:[/] {domain}")
            console.print(f"[{PURPLE}][+] Resolved IP:[/] [{RED}]{ip}[/]")
        except socket.gaierror:
            console.print(f"\n[{RED}][!] Failed to resolve hostname.[/]")

def ip_geolocation():
    print_header()
    ip = input("Enter IP to Geolocate (Leave blank for own IP): ").strip()
    try:
        url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
        res = requests.get(url, timeout=5).json()
        if res.get('status') == 'success':
            console.print(f"\n[{PURPLE}][+] Target IP:[/] {res.get('query')}")
            console.print(f"[{PURPLE}][+] Country:[/] {res.get('country')} ({res.get('countryCode')})")
            console.print(f"[{PURPLE}][+] City/Region:[/] {res.get('city')}, {res.get('regionName')}")
            console.print(f"[{PURPLE}][+] ISP:[/] {res.get('isp')}")
            console.print(f"[{PURPLE}][+] Coordinates:[/] {res.get('lat')}, {res.get('lon')}")
        else:
            console.print(f"[{RED}][!] Invalid target or lookup failed.[/]")
    except Exception as e:
        console.print(f"[{RED}][!] Error fetching geolocation data: {e}[/]")

def port_checker():
    print_header()
    host = input("Enter target host (default 127.0.0.1): ").strip() or "127.0.0.1"
    ports = [21, 22, 80, 443, 3306, 8080]
    console.print(f"\n[{PINK}]Scanning common ports on {host}...[/]\n")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            console.print(f"  [{RED}]•[/] Port {port}: [{RED}]OPEN[/]")
        else:
            console.print(f"  [{PURPLE}]•[/] Port {port}: [dim]CLOSED[/dim]")
        s.close()

def gen_password():
    print_header()
    import random
    import string
    try:
        length = int(input("Enter password length (default 16): ") or 16)
    except ValueError:
        length = 16
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = "".join(random.choice(chars) for _ in range(length))
    console.print(f"\n[{PURPLE}][+] Generated Secure Password:[/] [{RED}]{pwd}[/]")

def base64_tool():
    print_header()
    console.print(f"[{PINK}]1.[/] Encode to Base64")
    console.print(f"[{PINK}]2.[/] Decode from Base64")
    mode = input("\nSelect operation (1/2): ").strip()
    text = input("Enter string: ").strip()
    
    if mode == '1':
        encoded = base64.b64encode(text.encode()).decode()
        console.print(f"\n[{PURPLE}][+] Base64 Encoded:[/] [{RED}]{encoded}[/]")
    elif mode == '2':
        try:
            decoded = base64.b64decode(text.encode()).decode()
            console.print(f"\n[{PURPLE}][+] Base64 Decoded:[/] [{RED}]{decoded}[/]")
        except Exception:
            console.print(f"\n[{RED}][!] Invalid Base64 payload.[/]")

def flush_temp():
    print_header()
    console.print(f"[{PINK}]Flushing system temporary directory...[/]\n")
    temp_path = tempfile.gettempdir()
    deleted = 0
    errors = 0
    for item in os.listdir(temp_path):
        item_path = os.path.join(temp_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                deleted += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                deleted += 1
        except Exception:
            errors += 1
    console.print(f"[{PURPLE}][+] Successfully cleared {deleted} items.[/]")
    if errors > 0:
        console.print(f"[{RED}][!] Skipped {errors} locked active process files.[/]")

def hash_generator():
    print_header()
    text = input("Enter string to compute hashes: ").strip()
    if text:
        md5 = hashlib.md5(text.encode()).hexdigest()
        sha1 = hashlib.sha1(text.encode()).hexdigest()
        sha256 = hashlib.sha256(text.encode()).hexdigest()
        console.print(f"\n[{PURPLE}][+] MD5 Hash:[/] {md5}")
        console.print(f"[{PURPLE}][+] SHA-1 Hash:[/] {sha1}")
        console.print(f"[{PURPLE}][+] SHA-256 Hash:[/] [{RED}]{sha256}[/]")

def main():
    while True:
        print_header()
        print_menu()
        choice = console.input(f"[{RED}]angeldust@multitool[/][{PURPLE}]:~# [/]").strip()

        if choice in ['1', '01']: sys_info()
        elif choice in ['2', '02']: hw_telemetry()
        elif choice in ['3', '03']: disk_usage()
        elif choice in ['4', '04']: top_processes()
        elif choice in ['5', '05']: battery_status()
        elif choice in ['6', '06']: network_ip()
        elif choice in ['7', '07']: ping_host()
        elif choice in ['8', '08']: dns_lookup()
        elif choice in ['9', '09']: ip_geolocation()
        elif choice in ['10']: port_checker()
        elif choice in ['11']: gen_password()
        elif choice in ['12']: base64_tool()
        elif choice in ['13']: flush_temp()
        elif choice in ['14']: hash_generator()
        elif choice in ['15', 'exit', 'quit']:
            console.print(f"\n[{PINK}]Terminating Multi-Tool session...[/]")
            sys.exit()
        else:
            console.print(f"[{RED}][!] Invalid selection.[/]")
        
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()