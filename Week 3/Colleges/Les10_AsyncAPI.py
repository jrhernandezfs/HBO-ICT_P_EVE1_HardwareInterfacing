import aiohttp
import asyncio

async def fetch_weather(session, city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    async with session.get(url) as response:
        return await response.json()

async def main():
    api_key = 'your_api_key_here'
    cities = ["Amsterdam", "Berlin", "London"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city, api_key) for city in cities]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)  # Verwerken van de verkregen weergegevens

if __name__ == '__main__':
    asyncio.run(main())