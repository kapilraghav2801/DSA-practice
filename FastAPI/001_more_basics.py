# # SYNC (blocking - waits and does nothing)
# def make_coffee():
#     time.sleep(3)  # Stops everything for 3 seconds
#     return "Coffee ready"

# # ASYNC (non-blocking - works on other things while waiting)
# async def make_coffee():
#     await asyncio.sleep(3)  # "Pause this, go help other customers, come back in 3 seconds"
#     return "Coffee ready"