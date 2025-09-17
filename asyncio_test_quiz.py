import asyncio
async def double(x):
    await asyncio.sleep(0.05)
    return x*2

async def main():
    results=await asyncio.gather(
        double(3),
        double(4),
        double(5))
    
    print(max(results),sum(results))

asyncio.run(main())