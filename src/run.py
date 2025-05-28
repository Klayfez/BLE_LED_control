import asyncio
from src.led_control.cmds import *
from src.led_control.led import connect_device, disconnect_device, find_device, send_command
from src.config.reader import CHAR_UUID, DEVICE_ADDRESS, DEVICE_NAME

async def example(client):
    await send_command(client, CHAR_UUID, power(False), start_delay=1)
    await send_command(client, CHAR_UUID, power(True), start_delay=1)
    for i in range(0, 125, 25):
        await send_command(client, CHAR_UUID, brightness(i), attempt_delay=1, start_delay=1)
    await send_command(client, CHAR_UUID, brightness(100), start_delay=1)
    await send_command(client, CHAR_UUID, color(255, 0, 0), start_delay=1)
    await send_command(client, CHAR_UUID, color(0, 255, 0), start_delay=1)
    await send_command(client, CHAR_UUID, color(0, 0, 255), start_delay=1)

async def main():
    device_address = DEVICE_ADDRESS
    if not device_address:
        device = await find_device(DEVICE_NAME)
        device_address = device.address

    client = await connect_device(device_address)
    if not client:
        return
    try:
        await example(client)
    finally:
        await disconnect_device(client)

if __name__ == "__main__":
    asyncio.run(main())
