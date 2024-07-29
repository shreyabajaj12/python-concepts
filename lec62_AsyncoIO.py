import time
import asyncio
# helps to download things parallely rather then one by one
async def function1():
    await asyncio
    print("func1")
async def function2():
    time.sleep(3)
    print("func2")
async def function3():
    time.sleep(3)
    print("func3")

async def main():
    await function1()
    await function2()
    await function3()

asyncio.reun(main())
