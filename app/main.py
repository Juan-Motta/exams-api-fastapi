from asyncio import get_event_loop, AbstractEventLoop

from app.app import app, startup_event

if __name__ == "__main__":
    loop: AbstractEventLoop = get_event_loop()
    loop.run_until_complete(startup_event())
    loop.run_forever()