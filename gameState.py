def start_game(rooms, commands ):
    present = 0
    myinventory = []
    while(True):
        if(rooms[present]['win'] == True ):
            if('win' in myinventory):
                print('You win\nexiting.....')
                break
            elif('lose' in myinventory):
                print('You lost\nexiting.....')
                break
        print(f"> {rooms[present]['name']}\n")
        print(f"{rooms[present]['desc']}\n")
        commandsInRoom = commands[:]
        if(len(rooms[present]['special'].keys() ) > 0):
            for key in rooms[present]['special'].keys():
                commandsInRoom.append(key)
        if(len(rooms[present]['items'] ) > 0):
            print("Items:",", ".join(rooms[present]['items'] ) )
            print("")
        if(len(rooms[present]['interactables'] ) > 0):
            str_item = 'Interactables:'
            for person in rooms[present]['interactables'].keys():
                str_item += " "+person
            print(str_item, '\n')
        print("Exits:", " ".join(rooms[present]['exits'] ) )
        print("")
        while(True):
            try:
                action = input('What would you like to do? ').lower()
            except EOFError:
                print("\nUse 'quit' to exit.")
                continue
            command=action.split(" ")
            if(command[0] in commandsInRoom):
                if(command[0] == 'quit'):
                    print('Goodbye!')
                    exit()
                elif(command[0] == 'go'):
                    if(len(command) != 2):
                        print("Sorry, you need to 'go' somewhere.")
                        continue
                    if(command[1] not in rooms[present]['exits'].keys() ):
                        print(f"There's no way to go {command[1]}.")
                        continue
                    else:
                        print(f"You go {command[1]}.\n")
                        present = rooms[present]['exits'][command[1]]
                        break
                elif(command[0] == 'look'):
                    break
                elif(command[0] == 'inventory'):
                    if(len(myinventory) == 0):
                        print("You're not carrying anything.")
                    else:
                        print("Inventory:")
                        for item in myinventory:
                            print(f"  {item}")
                    continue
                elif(command[0] == 'get'):
                    if(len(command) < 2):
                        print("Sorry, you need to 'get' something.")
                        continue
                    if(len(command) > 2):
                        for i in range(2, len(command) ):
                            command[1] += (" "+command[i])
                    if(command[1] not in rooms[present]['items'] ):
                        print(f"There's no {command[1]} anywhere.")
                        continue
                    else:
                        print(f"You pick up the {command[1]}.")
                        myinventory.insert(0,command[1] )
                        rooms[present]['items'].remove(command[1] )
                        continue
                elif(command[0] == 'drop'):
                    if(len(command) < 2):
                        print("Sorry, you need to 'drop' something.")
                        continue
                    if(len(command) > 2):
                        for i in range(2,len(command) ):
                            command[1] += (" "+command[i] )
                    if(command[1] not in myinventory):
                        print("There's no " + command[1] + " in your inventory")
                        continue
                    else:
                        print("You droped  " + command[1] + " here")
                        myinventory.remove(command[1] )
                        rooms[present]['items'].append(command[1] )
                        continue
                elif(command[0] == 'talk'):
                    if(len(command) != 2 ):
                        print("Sorry, you need to 'talk' something.")
                        continue
                    if(command[1] not in rooms[present]['interactables'].keys() ):
                        print("There's no "+command[1]+" anywhere")
                        continue
                    else:
                        print(command[1]+" : "+rooms[present]['interactables'][command[1]]['dailogue'])
                        continue
                elif(command[0] == 'give'):
                    if(len(command) != 3):
                        print("Sorry,you need to 'give' something to someone")
                        continue
                    if(command[1] not in rooms[present]['interactables'].keys() ):
                        print("There's no "+command[1]+" anywhere")
                        continue
                    else:
                        if(command[2] not in myinventory):
                            print("sorry, "+command[2]+" is not there in your Inventory")
                            continue 
                        if(command[2] not in rooms[present]['interactables'][command[1]]['give'].keys() ):
                            print("sorry , "+command[1]+" doesn't accept "+command[2] )
                            continue
                        else:
                            myinventory.remove(command[2] )
                            myinventory.append(rooms[present]['interactables'][command[1] ]['give'][command[2] ] )
                            print("By giving "+command[2]+" to "+command[1]+", you got "+rooms[present]['interactables'][command[1]]['give'][command[2]])
                            continue
                elif(command[0] in rooms[present]['special'].keys() ):
                    checklist = rooms[present]['special'][command[0] ]['checklist']
                    checkFlag = True
                    for thing in checklist:
                        if(thing not in myinventory):
                            print("You don't have enough items, missing "+thing+"."+command[0]+" failed")
                            checkFlag = False
                            break
                    
                    if(checkFlag):
                        myinventory.append(rooms[present]['special'][command[0] ]['success'] )
                        print(command[0]+" successful\n")
                        for thing in checklist:
                            if(thing in myinventory):
                                myinventory.remove(thing)
                        break
                    elif('failure' in rooms[present]['special'][command[0] ].keys() ):
                        myinventory.append(rooms[present]['special'][command[0] ]['failure'] )
                        break
                    continue
            else:
                print("Use valid commands")
                continue
