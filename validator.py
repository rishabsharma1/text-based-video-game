def validateRoom(room, length):
    if(type(room) is not dict):
        raise Exception("List should have valid rooms which are dictionries")
    if(('items' not in room.keys() ) ):
        room['items'] = []
    if(('interactables' not in room.keys() ) ):
        room['interactables'] = {}
    if(('special' not in room.keys() ) ):
        room['special'] = {}
    if(('win' not in room.keys() ) ):
        room['win'] = False
    if(type(room['win'] ) is not bool and room['win'].lower() == "false" ):
        room['win'] = False
    if(type(room['win'] ) is not bool and room['win'].lower()=="true" ):
        room['win'] = True
    if(('name' not in room.keys() ) or ('desc' not in room.keys() ) or ('exits' not in room.keys() ) ):
        raise Exception("Room should have name,description and exits")
    if(len(room.keys() ) > 7 ):
        raise Exception("Room should have only valid keys")
    if(type(room['name'] ) is not str):
        raise Exception("Room name should be string")
    if(type(room['desc'] ) is not str):
        raise Exception("Room description should be string")
    exits = {}
    if((type(room['exits'] ) is not dict) ):
        raise Exception("Room exits should be a dictonary")
    for exit in room['exits'].keys():
        if(room['exits'][exit] >= length or room['exits'][exit] < 0):
            raise Exception("Room exit should be valid room id object")
        exits[exit.lower()] = room['exits'][exit]
    room['exits'] = exits
    special = {}
    if((type(room['special'] ) is not dict) ):
        raise Exception("Room special commands should be a dictonary")
    interactables = {}
    for index in room['interactables'].keys():
        for index1 in room['interactables'][index]:
            if(index1 not in ['dailogue','give'] ):
                raise Exception("Interactables should only dailogue and give keys")
            if(index1 == "give" and type( room['interactables'][index][index1] ) is not dict ):
                raise Exception("Give key should have dictonary of acceptable items and exchanging goods as value")
        interactables[index.lower() ] = room['interactables'][index]
    room['interactables'] = interactables
    for index in room['special'].keys():
        if(type(room['special'][index] ) is not dict):
            raise Exception("Room special commands shoud be a dcitonary")
        if('checklist' not in room['special'][index].keys() and 'success' not in room['special'][index].keys() and type(room['special'][index]['checklist'] ) is not dict and type(room['special'][index]['success'] ) is not str):
            raise Exception("Room special commands shoud have items requiment and success item")
        itms = []
        for elems in room['special'][index]['checklist']:
            itms.append(elems.lower() )
        if('failure' not in room['special'][index].keys() ):
            special[index.lower()] = {'checklist' : itms, 'success' : room['special'][index]['success'].lower()}
        else:
            special[index.lower() ] = {'checklist' : itms, 'success' : room['special'][key]['success'].lower(), 'failure' : room['special'][index]['failure'] }
    room['special'] = special
    items = []
    if(len(room['items'] ) > 0 ):
        if((type(room['items'] ) is not list) ):
            raise Exception("Items should be a list")
        for l in room['items']:
            if((type(l) is not str) ):
                raise Exception("Item should be a string")
            items.append(l.lower() )
    room['items'] = items
    if(type(room['win'] ) is not bool):
        raise Exception("winning is possible or not should be a boolean in the room")
    return room
def roomNamesToNumbers(rooms):
    roomNames = [r['name'] for r in rooms]
    rNames = set(roomNames)
    if(len(rNames)!=len(roomNames)):
        raise Exception("Duplicate Room Names")
    for i in range(len(rooms)):
        room = rooms[i]
        for exit in room['exits'].keys():
            if(type(room['exits'][exit]) is str and room['exits'][exit] in roomNames):
                rooms[i]['exits'][exit] = roomNames.index(room['exits'][exit])
            elif(type(room['exits'][exit]) is str):
                raise Exception('room exits have invalid keys')
    return rooms
