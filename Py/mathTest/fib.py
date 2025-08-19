import asyncio
import functools


def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except asyncio.TimeoutError:
                print(f"Function '{func.__name__}' timed out after {seconds} seconds.")

        return wrapper

    return decorator


@timeout(1)
async def fib(length):
    fib = 0
    for i in range(length):
        fib += i
        print(i)
        await asyncio.sleep(0)  # Allow cancellation


def main():
    asyncio.run(fib(100000000))


main()
