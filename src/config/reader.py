import json
import os 

config_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'config.json'
)

with open(config_path, 'r') as f:
    config = json.load(f)

DEVICE_NAME = config['device_name'] # Для поиска устройства
DEVICE_ADDRESS = config['device_address'] # Если вы уже знаете адрес, иначе None
CHAR_UUID = config['char_uuid'] # Не особо понял, но,
                                # возможно, у каждого устройства
                                # разный, ищите свой сами.
