Rishab sharma  rsharma10@stevens.edu
https://github.com/rishabsharma1/text-based-video-game
I spent 40 hours developing the functional code.
I tested the code manually using a variety of inputs and different map configurations.
During testing, I made sure to cover all possible scenarios.
I believe I've fixed all the bugs I found.
There were some bugs such as i couldnt accept a item with spaces in it as i was using a split. Later i tackled it with mereging the splited commands accoring to main command
I assumed exits are only directions and placed a unneccessary validation which ruled out other exits,after removing it evrything worked fine.
I tried different types of printing sequences to resolve the mismatch in printing
Regarding code extensions and interactions,
"Winning and losing conditions"
My code will look if map room object has special field of win and iif its true then it will check for winning situation occured or not if present in that room
If your inventory has win in it and room you present has win field true then you win and in the same way if you have lose you will lose
Win and lose may be added to the inventory by other set of actions.In the map I used if we kill brigadier using special command attack and everything about the command is already given in map 
It is not hard coded.Assesmble is also special command its behaviour is also given in map.
"Interactions"
There are interactable in the map and possible options to interact are give and talk where you can use talk [interactable] to talk and 
give [interactable] [item] where you can give item to interactable .The thing to be noted is you cant talk to all interctables and you cant give anything you wish to them .
interactables only accept specific items and they exchange some other item with you.
There are special iteractions commands as assemble and attack which are not possible for all interactables
"Drop"
A drop command which drop specifed item in the room you present,you need to first have the item in your inventory to drop it.


