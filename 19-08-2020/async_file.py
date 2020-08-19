import asyncio


async def useful_action(seconds):
    print(f'slep for {seconds} seconds')
    await asyncio.sleep(seconds)
    print('woken up')
    return seconds

async def main():
    tasks = []

    tasks.append(asyncio.create_task(useful_action(3)))
    tasks.append(asyncio.create_task(useful_action(5)))
    tasks.append(asyncio.create_task(useful_action(2)))
    tasks.append(asyncio.create_task(useful_action(3)))

    # for t in tasks:
    #     await t
    # results = await asyncio.gather(*tasks)
    # print(results)

    for results in asyncio.as_completed(tasks):
        print(await results)

asyncio.run(main())