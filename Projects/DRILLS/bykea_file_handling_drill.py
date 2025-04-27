# SUBDOMAINS 

def load_subdomains(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Clean whitespace
    return [line.strip() for line in lines if line.strip()]

# ALIVE

def save_alive_subdomain(subdomain):
    with open('alive.txt', 'a') as file:
        file.write(subdomain + '\n')

# SCAN

def scan_subdomains(subdomains):
    for subdomain in subdomains:
        print(f"Scanning target: {subdomain}")
        #Dummy alive check
        if "api" in subdomain:
            print(f"[+] {subdomain} is alive!")
            save_alive_subdomain(subdomain)

# MISSION EXECUTION

subdomains = load_subdomains('subdomains.txt')
scan_subdomains(subdomains)
