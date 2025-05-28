import asyncio
from bleak import BleakClient, BleakScanner

async def find_device(device_name):
    print("Поиск устройства...")
    devices = await BleakScanner.discover()
    # print(devices)
    device = next((d for d in devices if d.name == device_name), None)
    if device:
        print(f"Найдено: {device.name} {device.address}")
    else:
        print("Устройство не найдено.")
    return device

async def connect_device(address):
    client = BleakClient(address)
    try:
        await client.connect()
        if client.is_connected:
            print("Подключено.")
            return client
        else:
            print("Не удалось подключиться.")
            return None
    except Exception as e:
        print("Ошибка при подключении:", e)
        return None

async def disconnect_device(client):
    await asyncio.sleep(2)
    try:
        if client.is_connected:
            await client.disconnect()
            print("Отключено.")
    except Exception as e:
        print("Ошибка при отключении:", e)

async def send_command(client, uuid, command, retries=3, attempt_delay=0.1, start_delay=0.3):
    await asyncio.sleep(start_delay) # Задержка, чтобы большинство запросов исполнялось
    command_bytes = bytes.fromhex(command)
    attempt = 0

    while attempt < retries:
        try:
            if not client.is_connected:
                await client.connect()
                # services = client.services
                # print(f"Services: {services}")
            await client.write_gatt_char(uuid, command_bytes)
            print("Команда отправлена.")
            return
        except Exception as e:
            if "[org.bluez.Error.Failed] Not connected" in str(e):
                print(f"Попытка {attempt + 1}: устройство не подключено. Повторная попытка...")
                try:
                    await client.disconnect()
                except:
                    pass
                attempt += 1
                await asyncio.sleep(attempt_delay)
            else:
                print("Ошибка при отправке команды:", e)
                break
    else:
        print("Не удалось отправить команду после нескольких попыток.")