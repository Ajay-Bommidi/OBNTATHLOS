import os
import sys
import requests
import whois
import json
from colorama import Fore, Style, init
import dns.resolver
from urllib.parse import urlparse
import re

# Initialize colorama
init(autoreset=True)

# Global Configuration
CONFIG = {
    "ipinfo_api_key": "d337f3dbdd65ad",
    "output_dir": "./osint_results"
}

# Create output directory if not exists
os.makedirs(CONFIG["output_dir"], exist_ok=True)

# Welcome Banner
def display_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
   ____  ____  _   _ _______    _______ _    _ _      ____   _____ 
  / __ \|  _ \| \ | |__   __|/\|__   __| |  | | |    / __ \ / ____|
 | |  | | |_) |  \| |  | |  /  \  | |  | |__| | |   | |  | | (___  
 | |  | |  _ <| . ` |  | | / /\ \ | |  |  __  | |   | |  | |\___ \ 
 | |__| | |_) | |\  |  | |/ ____ \| |  | |  | | |___| |__| |____) |
  \____/|____/|_| \_|  |_/_/    \_\_|  |_|  |_|______\____/|_____/  
                [Automated OSINT Collection Tool]
                        Author: Ajay
    """)

    
# Install dependencies if missing
def check_dependencies():
    required_libraries = ["requests", "beautifulsoup4", "colorama", "tabulate", "python-whois", "dnspython"]
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            print(Fore.YELLOW + f"[!] Installing missing library: {lib}")
            os.system(f"pip install {lib} --quiet")  # Quiet installation
            print(Fore.GREEN + f"[+] {lib} installed successfully")

# Save results to a file
def save_result(filename, result):
    try:
        with open(filename, 'a') as file:
            file.write(result + "\n\n")
    except Exception as e:
        print(Fore.RED + f"[!] Error saving result to file: {str(e)}")

# IPinfo.io Geolocation Integration
def ipinfo_lookup(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json?token={CONFIG['ipinfo_api_key']}"
        response = requests.get(url)
        if response.status_code == 200:
            result = f"[+] IP Geolocation for {ip}: {response.json()}"
            print(Fore.GREEN + result)
            save_result(f"{CONFIG['output_dir']}/ipinfo_results.txt", result)
        else:
            print(Fore.RED + f"[!] Error in IPinfo.io lookup: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[!] Error in IPinfo.io lookup: {str(e)}")

# WHOIS Lookup
def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        result = f"[+] WHOIS Info for {domain}:\n{json.dumps(w, indent=4, default=str)}"
        print(Fore.GREEN + result)
        save_result(f"{CONFIG['output_dir']}/whois_results.txt", result)
    except Exception as e:
        print(Fore.RED + f"[!] Error in WHOIS lookup: {str(e)}")

# DNS Lookup
def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        result_str = f"[+] DNS Lookup Results for {domain}:"
        for ipval in result:
            result_str += f"\nIP: {ipval.to_text()}"
        print(Fore.GREEN + result_str)
        save_result(f"{CONFIG['output_dir']}/dns_results.txt", result_str)
    except Exception as e:
        print(Fore.RED + f"[!] Error in DNS lookup: {str(e)}")

# Directory Fuzzing & Finding Documents
def directory_fuzzing(url):
    try:
        # Interactive fuzzing with customizable directories and extensions
        common_dirs = [
            "/admin", "/login", "/dashboard", "/uploads", "/robots.txt", 
            "/.git", "/.env", "/admin.php", "/backup", "/config", "/cgi-bin"
        ]
        custom_dirs = input(Fore.LIGHTCYAN_EX + "[?] Enter custom directories (comma separated, leave empty to skip): ").strip()
        if custom_dirs:
            common_dirs += [d.strip() for d in custom_dirs.split(',')]

        common_exts = ['.php', '.html', '.txt', '.json', '.xml', '.bak']
        custom_exts = input(Fore.LIGHTCYAN_EX + "[?] Enter custom extensions (comma separated, leave empty to skip): ").strip()
        if custom_exts:
            common_exts += [ext.strip() for ext in custom_exts.split(',')]

        found = []
        
        # Fuzzing directories and extensions
        for directory in common_dirs:
            for ext in common_exts:
                target_url = url + directory + ext
                response = requests.get(target_url)
                if response.status_code == 200:
                    found.append(target_url)
                elif response.status_code == 301 or response.status_code == 302:
                    found.append(f"Redirected: {target_url}")

        if found:
            result = "[+] Directories and Documents Found:\n" + "\n".join(found)
            print(Fore.GREEN + result)
            save_result(f"{CONFIG['output_dir']}/directory_fuzzing_results.txt", result)
        else:
            print(Fore.YELLOW + "[!] No common directories or documents found.")
    
    except Exception as e:
        print(Fore.RED + f"[!] Error in Directory Fuzzing: {str(e)}")

# Google Dorking Search (Interactive with advanced options)
def google_dorking(query):
    try:
        dork_options = [
            f"site:{query} filetype:pdf", f"site:{query} inurl:login", f"site:{query} inurl:admin",
            f"site:{query} ext:php", f"site:{query} inurl:robots.txt", f"site:{query} intitle:index.of",
            f"site:{query} inurl:wp-login.php", f"site:{query} inurl:admin/ login", f"site:{query} inurl:.git",
            f"site:{query} inurl:backup", f"site:{query} inurl:config", f"site:{query} inurl:docker-compose.yml"
        ]
        
        print(Fore.LIGHTGREEN_EX + "[+] Available Google Dorking Options:")
        print(Fore.CYAN + "\n".join([f"[{i+1}] {dork}" for i, dork in enumerate(dork_options)]))
        
        selection = input(Fore.LIGHTMAGENTA_EX + "[?] Select a Google Dork by number (comma separated for multiple): ").strip()
        
        selected_dorks = [dork_options[int(i)-1] for i in selection.split(',') if i.isdigit()]

        print(Fore.GREEN + f"[+] Running Google Dorks for '{query}':")
        result = "\n".join([f"https://www.google.com/search?q={dork}" for dork in selected_dorks])
        print(Fore.LIGHTCYAN_EX + result)
        save_result(f"{CONFIG['output_dir']}/google_dorking_results.txt", result)
        
    except Exception as e:
        print(Fore.RED + f"[!] Error in Google Dorking: {str(e)}")

# Email Scraping (Website)
def scrape_emails(url):
    try:
        response = requests.get(url)
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
        if emails:
            result = f"[+] Found Emails for {url}:\n" + "\n".join(emails)
            print(Fore.GREEN + result)
            save_result(f"{CONFIG['output_dir']}/email_scraping_results.txt", result)
        else:
            print(Fore.YELLOW + "[!] No emails found.")
    except Exception as e:
        print(Fore.RED + f"[!] Error in Email Scraping: {str(e)}")

# Main Menu
def main_menu():
    print(Fore.LIGHTMAGENTA_EX + """
    [1] IPinfo.io Geolocation (IP)
    [2] WHOIS Lookup (Domain)
    [3] DNS Lookup (Domain)
    [4] Directory Fuzzing & Document Finding (URL)
    [5] Google Dorking (Search Query)
    [6] Email Scraping (Website)
    [7] Run All Modules
    [8] Exit
    """)
    choice = input(Fore.LIGHTGREEN_EX + "[?] Select an option: ").strip()
    return choice

# Main Execution
def main():
    display_banner()
    check_dependencies()
    while True:
        choice = main_menu()
        if choice == "1":
            ip = input(Fore.LIGHTBLUE_EX + "[?] Enter IP for IPinfo.io Geolocation: ").strip()
            ipinfo_lookup(ip)
        elif choice == "2":
            domain = input(Fore.LIGHTBLUE_EX + "[?] Enter Domain for WHOIS Lookup: ").strip()
            whois_lookup(domain)
        elif choice == "3":
            domain = input(Fore.LIGHTBLUE_EX + "[?] Enter Domain for DNS Lookup: ").strip()
            dns_lookup(domain)
        elif choice == "4":
            url = input(Fore.LIGHTBLUE_EX + "[?] Enter URL for Directory Fuzzing & Document Finding: ").strip()
            directory_fuzzing(url)
        elif choice == "5":
            query = input(Fore.LIGHTBLUE_EX + "[?] Enter search query for Google Dorking: ").strip()
            google_dorking(query)
        elif choice == "6":
            url = input(Fore.LIGHTBLUE_EX + "[?] Enter URL for Email Scraping: ").strip()
            scrape_emails(url)
        elif choice == "7":
            print(Fore.LIGHTYELLOW_EX + "[+] Running All Modules...")
            skip = input(Fore.LIGHTCYAN_EX + "[?] Do you want to skip any module? (comma separated, e.g. 1,3,5): ").strip()
            modules_to_skip = skip.split(",")
            
            if "1" not in modules_to_skip:
                ipinfo_lookup(input("Enter IP for Geolocation: "))
            if "2" not in modules_to_skip:
                whois_lookup(input("Enter domain for WHOIS: "))
            if "3" not in modules_to_skip:
                dns_lookup(input("Enter domain for DNS: "))
            if "4" not in modules_to_skip:
                directory_fuzzing(input("Enter URL for Directory Fuzzing: "))
            if "5" not in modules_to_skip:
                google_dorking(input("Enter search query for Google Dorking: "))
            if "6" not in modules_to_skip:
                scrape_emails(input("Enter URL for Email Scraping: "))
                
        elif choice == "8":
            print(Fore.CYAN + "[!] Exiting...")
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid Option!")

if __name__ == "__main__":
    main()
