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
    for direct in room['exits'].keys():
        if(room['exits'][direct] >= length or room['exits'][direct] < 0):
            raise Exception("Room exit should be valid room id object")
        exits[direct.lower()] = room['exits'][direct]
    room['exits'] = exits
    special = {}
    if((type(room['special'] ) is not dict) ):
        raise Exception("Room special commands should be a dictonary")
    interactables = {}
    for key in room['interactables'].keys():
        for key1 in room['interactables'][key]:
            if(key1 not in ['dailogue','give'] ):
                raise Exception("Interactables should only dailogue and give keys")
            if(key1 == "give" and type( room['interactables'][key][key1] ) is not dict ):
                raise Exception("Give key should have dictonary of acceptable items and exchanging goods as value")
        interactables[key.lower() ] = room['interactables'][key]
    room['interactables'] = interactables
    for key in room['special'].keys():
        if(type(room['special'][key] ) is not dict):
            raise Exception("Room special commands shoud be a dcitonary")
        if('checklist' not in room['special'][key].keys() and 'success' not in room['special'][key].keys() and type(room['special'][key]['checklist'] ) is not dict and type(room['special'][key]['success'] ) is not str):
            raise Exception("Room special commands shoud have items requiment and success item")
        itms = []
        for elems in room['special'][key]['checklist']:
            itms.append(elems.lower() )
        if('failure' not in room['special'][key].keys() ):
            special[key.lower()] = {'checklist' : itms, 'success' : room['special'][key]['success'].lower()}
        else:
            special[key.lower() ] = {'checklist' : itms, 'success' : room['special'][key]['success'].lower(), 'failure' : room['special'][key]['failure'] }
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