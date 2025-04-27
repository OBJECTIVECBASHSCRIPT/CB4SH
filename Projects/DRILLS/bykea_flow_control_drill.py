
subdomains = ["api.bykea.net", "maps.bykea.net", "leaflet-map.bykea.net"]

#FOR LOOP drill

for subdomain in subdomains:
    print(f"Scanning target: {subdomain}")

#WHILE LOOP drill

count = 0 
while count <= 5:
    print(f"Request attempt {count}")
    count += 1


#IF-ELSE drill

ports = (80, 443, 8080)

for port in ports:
    if port == 443:
        print(f"Port {port} is secure (HTTPS)")
    else:
        print(f"Port {port} might be insecure!")

# BREAK/CONTINUE drill

for port in ports:
    if port == 443: 
        print(f"Secure port {port} found. Stopping scan.")
        break  
    else: 
        print(f"Scanning port {port}...")


