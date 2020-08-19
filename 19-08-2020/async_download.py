import asyncio
import aiohttp

# async with aiohttp.ClientSession() as session:
#     asymc with session.get() as response:
#         pass

def save(file: open, filename:str):
    with open(filename, 'wb') as image:
        image.write(file)

async def meke_request(url: str, session: aiohttp.ClientSession, filename:str):
    async with session.get(url) as response:
        file = await response.content.read()
        save(file, f'{filename}.jpeg')
        return filename


async def make_requests(urls: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for idx, url in enumerate(urls):
            tasks.append(meke_request(url, session,  str(idx) )  )

        results = await asyncio.gather(*tasks)
        print(results)

async def main():
    urls = ['https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg'] * 5
    await make_requests(urls)

asyncio.run(main())