#REI ASSET LIST

assets = [
    "https://rei.com/lists",
    "engineering.rei.com",
    "rei.gladly.com",
    "vpn.rei.com",
    "rei.jobs"
]

# SAVE 

with open("rei_assets.txt", "w") as f:
    for asset in assets:
        f.write(asset + "\n")

# SCAN
with open("rei_assets.txt", "r") as f:
    for line in f:
        asset = line.strip()
        print(f"Scanning asset: {asset}")
