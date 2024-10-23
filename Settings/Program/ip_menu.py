import subprocess
import requests
import socket
import platform
import concurrent.futures
import os
import re
from pystyle import Colors, Colorate, Center
import whois as python_whois
import time


def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

def ping_ip(ip_address):
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}"))
        Slow(result.stdout)
    except subprocess.TimeoutExpired:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "Timeout expired. No response received."))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def get_ip_information(ip_address):
    try:
        api_key = 'bf609e0ae94346a69905706a764efce5'
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}").json()

        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nIP Information\n{'=' * 60}"))

        ip_info = {
            "IP Address": response.get("ip"),
            "Continent": f"{response.get('continent_name')} ({response.get('continent_code')})",
            "Country": f"{response.get('country_name')} ({response.get('country_code3')})",
            "Region": response.get("state_prov"),
            "City": response.get("city"),
            "Postal Code": response.get("zipcode") if response.get("zipcode") else "Not available",
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "Time Zone": format_timezone(response.get('time_zone')),
            "ISP": response.get("isp"),
            "Organization": response.get("organization"),
            "Domain": response.get("domain") if response.get("domain") else "Not available",
            "ASN": response.get("asn"),
            "Altitude": response.get("altitude") if response.get("altitude") else "Not available",
            "Threat Level": response.get("threat").get("is_tor") if response.get("threat") else "Not available"
        }

        for key, value in ip_info.items():
            if value:
                Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {value}"))

    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def format_timezone(timezone_info):
    if timezone_info:
        return f"{timezone_info.get('name')} (UTC{timezone_info.get('offset')})"
    else:
        return ""

def traceroute_ip(ip_address, max_hops=30, timeout=5):
    try:
        if platform.system().lower() == "windows":
            command = ['tracert', '-h', str(max_hops), '-w', str(timeout * 1000), ip_address]
        else:
            command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), ip_address]

        result = subprocess.run(command, capture_output=True, text=True)

        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nTRACEROUTE {ip_address}\n{'=' * 60}"))
        Slow(result.stdout)

    except subprocess.CalledProcessError as cpe:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Command failed with error: {cpe}"))
    except FileNotFoundError:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "Traceroute command not found. Please ensure it is installed on your system."))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def reverse_dns_lookup(ip_address, dns_server=None):
    try:
        command = ['nslookup', ip_address]
        if dns_server:
            command.append(dns_server)

        result = subprocess.run(command, capture_output=True, text=True)

        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nREVERSE DNS LOOKUP {ip_address}\n{'=' * 60}"))
        Slow(result.stdout)

    except subprocess.CalledProcessError as cpe:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Command failed with error: {cpe}"))
    except FileNotFoundError:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "nslookup command not found. Please ensure it is installed on your system."))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def scan_port(ip_address, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Error scanning port {port}: {e}"))
        return None

def port_scan(ip_address, start_port=1, end_port=1024, timeout=1, max_workers=100):
    open_ports = []
    Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Scanning ports on {ip_address} from {start_port} to {end_port}... This may take a while."))

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_port, ip_address, port, timeout): port for port in range(start_port, end_port + 1)}
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Port {port} is open"))

        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nOPEN PORTS ON {ip_address}\n{'=' * 60}"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"Open ports: {open_ports}"))

    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred during port scanning: {e}"))

def whois_lookup(ip_address):
    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_address):
            Slow(Colorate.Horizontal(Colors.blue_to_cyan, "Invalid IP address format."))
            return

        result = python_whois.whois(ip_address)

        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nWHOIS LOOKUP {ip_address}\n{'=' * 60}"))

        if result:
            for key, value in result.items():
                if value:
                    if isinstance(value, list):
                        for item in value:
                            Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {item}"))
                    else:
                        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {value}"))
        else:
            Slow(Colorate.Horizontal(Colors.blue_to_cyan, "No WHOIS information found for the IP address."))

    except python_whois.parser.PywhoisError as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"WHOIS lookup failed: {e}"))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def blacklist_check(ip_address):
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}", headers={
            'Key': '173b1074344847a7968aeee29091c3bea4db13e52eeb78e9f921ba1fe043468bf9d965d63666d411', 
            'Accept': 'application/json'
        }).json()
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nBLACKLIST CHECK {ip_address}\n{'=' * 60}"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, str(response)))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def dns_records(ip_address):
    try:
        import dns.resolver
        record_types = ['A', 'MX', 'NS', 'TXT']
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nDNS RECORDS {ip_address}\n{'=' * 60}"))

        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(ip_address, record_type)
                for rdata in answers:
                    Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"{record_type} Record: {rdata}"))
            except Exception as e:
                Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"No {record_type} records found for {ip_address}: {e}"))
    except ImportError:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "dns.resolver module not found. Please install dnspython."))
    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def menu():
    while True:
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "\nMenu"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "1. Ping an IP address"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "2. Get IP information"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "3. Traceroute to an IP address"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "4. Reverse DNS Lookup"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "5. Port Scan"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "6. WHOIS Lookup"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "7. Blacklist Check"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "8. DNS Records"))
        Slow(Colorate.Horizontal(Colors.blue_to_cyan, "9. Quit"))

        choice = input("Enter your choice: ")

        if choice == "1":
            ip_address = input("Enter IP address to ping: ")
            ping_ip(ip_address)
        elif choice == "2":
            ip_address = input("Enter IP address to get information: ")
            get_ip_information(ip_address)
        elif choice == "3":
            ip_address = input("Enter IP address to traceroute: ")
            traceroute_ip(ip_address)
        elif choice == "4":
            ip_address = input("Enter IP address for reverse DNS lookup: ")
            reverse_dns_lookup(ip_address)
        elif choice == "5":
            ip_address = input("Enter IP address for port scan: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            port_scan(ip_address, start_port, end_port)
        elif choice == "6":
            ip_address = input("Enter IP address for WHOIS lookup: ")
            whois_lookup(ip_address)
        elif choice == "7":
            ip_address = input("Enter IP address for blacklist check: ")
            blacklist_check(ip_address)
        elif choice == "8":
            ip_address = input("Enter IP address for DNS records: ")
            dns_records(ip_address)
        elif choice == "9":
                input("[x] Appuyer sur entrée pour retourner au menu principal.")
                os.system('python ../../main.py')
        else:
            Slow(Colorate.Horizontal(Colors.blue_to_cyan, "Invalid choice. Please try again."))

if __name__ == "__main__":
    menu()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')