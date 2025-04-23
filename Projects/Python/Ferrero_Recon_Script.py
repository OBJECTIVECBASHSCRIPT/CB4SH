import aiohttp
import asyncio
import socket

WILDCARD_DOMAINS = [ 
    "*.nutella.com",
    "*.kinder.com",
    "*.halotop.com",
    "*.bluebunny.com",
    "*.babyruth.com"
]

WORDLIST = ["www", "dev", "api", "test", "staging", "portal", "mail", "cdn", "beta", "admin"]

async def resolve_and_probe(session, domain):
    socket.gethostbyname(domain)

    async with session.get(f"http://{domain}", timeout=5) as resp:
        if resp.status < 500:
            print(f"[complete] Live {domain} ({resp.status})")
            return domain

    return None

async def main():
    tasks = []
    results = []

    async with aiohttp.ClientSession() as session:
        for base in WILDCARD_DOMAINS:
            root = base.replace("*.", "")
            for sub in WORDLIST:
                domain = f"{sub}.{root}"
                tasks.append(resolve_and_probe(session, domain))

        resolved = await asyncio.gather(*tasks, return_exceptions=True)

        for r in resolved:
            if isinstance(r, str):
                results.append(r)

    print("\n[INFO] Resolved and responsive domains:")
    for r in results:
        print(f" - {r}")

if __name__ == "__main__":
    asyncio.run(main())
