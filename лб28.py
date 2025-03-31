import os
import asyncio
import aiohttp

def create_project_structure():
    folders = ["controllers", "models", "views"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    with open("requirements.txt", "w") as f:
        f.write("aiohttp\n")

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    create_project_structure()
    print("Структура проекту створена успішно.")
    
    test_urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 11)]
    results = asyncio.run(fetch_multiple_urls(test_urls))
    
    for result in results:
        print(result[:100] + "...")