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
    if(type(raw_rooms) is not dict):
        raise Exception("Given map should be dict")
    if('rooms' not in raw_rooms.keys() or 'start' not in raw_rooms.keys()):
        raise Exception("Map should defenitley have a start and rooms")
    raw_rooms['rooms']=roomNamesToNumbers(raw_rooms['rooms'])
    for room in raw_rooms['rooms']:
        rooms.append(validateRoom(room, len(raw_rooms['rooms']) ) )
except Exception as e:
    print('Error', e,file=sys.stderr)
    sys.exit(1)

start_game(rooms, commands)
