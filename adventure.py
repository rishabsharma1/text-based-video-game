import sys
import json
from validator import validateRoom 
from gameState import start_game
commands=['go', 'get', 'quit', 'look', 'inventory', 'give', 'talk', 'drop']

if(len(sys.argv) != 2):
    print('Enter valid command line arguments')
f = open(str(sys.argv[1] ) )
rooms = []
try:
    raw_rooms = json.load(f)
    if(type(raw_rooms) is not list):
        raise Exception("Given map should be a list")
    for room in raw_rooms:
        rooms.append(validateRoom(room, len(raw_rooms) ) )
except Exception as e:
    print('Error', e)
    exit()

start_game(rooms, commands)
