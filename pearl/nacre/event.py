import asyncio

class Event:

    def __init__(self):
        self.listeners = []

    def addListener(self, listener):
        if not asyncio.iscoroutinefunction(listener):
            raise ValueError("Listener must be a coroutine")
        if listener not in self.listeners:
            self.listeners.append(listener)

    def removeListener(self, listener):
        if not asyncio.iscoroutinefunction(listener):
            raise ValueError("Listener must be a coroutine")
        if listener in self.listeners:
            self.listeners.remove(listener)

    async def fire(self, *args, **kwargs):
        for listener in self.listeners:
            await listener(*args, **kwargs)
