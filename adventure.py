import sys
import json
from validator import validateRoom
from validator import roomNamesToNumbers
from gameState import start_game
commands=['go', 'get', 'quit', 'look', 'inventory', 'give', 'talk', 'drop']

if(len(sys.argv) != 2):
    print('Enter valid command line arguments')
f = open(str(sys.argv[1] ) )
rooms = []
try:
    raw_rooms = json.load(f)
    if(type(raw_rooms) is not dict and 'rooms' not in raw_rooms.keys()):
        raise Exception("Given map should be a list")
    print(raw_rooms['rooms'])
    raw_rooms['rooms']=roomNamesToNumber(raw_rooms['rooms'])
    for room in raw_rooms['rooms']:
        rooms.append(validateRoom(room, len(raw_rooms['rooms']) ) )
except Exception as e:
    print('Error', e)
    exit()

start_game(rooms, commands)
