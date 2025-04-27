subdomains = ["api.bykea.net", "maps.bykea.net", "leaflet-map.bykea.net"]
ports = (80, 443, 8080)

def greet(name):
    return f"Hello, {name}!"

print(greet("Cyber Cossack"))

def scan_subdomains(subdomains):
    for subdomain in subdomains:
        print(f"Scanning target: {subdomain}")

def count_requests(max_count=5):
    count = 0
    while count <= max_count:
        print(f"Request attempt {count}")
        count += 1
    

def check_ports(ports):
    for port in ports:
        if port == 443:
            print(f"Port {port} is secure (HTTPS)")
        else:
            print(f"Port {port} might be insecure!")

def find_secure_port(ports):
    for port in ports:
        if port == 443:
            print(f"Secure port {port} found. Stopping scan.")
            break
        else:
            print(f"Scanning port {port}...")

# MISSION EXECUTION 

scan_subdomains(subdomains)
count_requests()
check_ports(ports)
find_secure_port(ports)
