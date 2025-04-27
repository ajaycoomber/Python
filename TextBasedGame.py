#Ajay Coomber

#import sys to provide exit command
import sys

#game instructions
def show_instructions():
    print('Welcome to the gym bro game')
    print('You need to collect all 6 of the gym bros items to convince the gym bro to leave')
    print('Type move commands are: "go North, go East, go South, go West"')
    print('Type "get" followed by the name of the item to get an item')
    print('Type exit at any time to quit the game')

#function to show status of player each time through gameplay loop
def show_status(current_room, rooms, inventory):
    print('Current Location: {}'.format(current_room))
    print('Current Inventory:', inventory)
    #if-else depending if there is item available
    if 'item' in rooms[current_room]:
        print("Available item in this room:", rooms[current_room]['item'])
    else:
        print("No items available to collect in this room.")

#function to change rooms based on user input
def change_room(direction, rooms, current_room):
    if direction not in rooms[current_room].keys():
        print('*** INVALID ENTRY ***')
        pass
    else:
        current_room = rooms[current_room][direction]
    return current_room

#function to get items based on room
def get_item(inventory, noun, rooms, current_room):
    current_item_available = rooms[current_room].get('item')
    #check if item is available and user_input matches item
    if current_item_available != None and noun == current_item_available:
        #add item to inventory
        if noun in rooms[current_room]['item']:
            inventory.append(noun)
            rooms[current_room].pop('item')
            return inventory
    #print invalid entry if item not available or wrong item is requested
    else:
        print('*** INVALID ENTRY ***')
        return inventory


def main():
    #set current room, define inventory and rooms library, show gameplay instructions
    current_room = 'Front Desk'
    inventory = []
    show_instructions()
    rooms = {
        'Front Desk': {'north': 'Locker Room', 'east': 'Tanning Bed', 'south': 'Squash Court', 'west': 'Swimming Pool'},
        'Locker Room': {'east': 'Pilates Room', 'south': 'Front Desk', 'item': 'board shorts'},
        'Pilates Room': {'west': 'Locker Room', 'item': 'yoga mat'},
        'Swimming Pool': {'east': 'Front Desk', 'item': 'towel'},
        'Squash Court': {'north': 'Front Desk', 'east': 'Basketball Court', 'item': 'water bottle'},
        'Basketball Court': {'west': 'Squash Court', 'item': 'basketball shoes'},
        'Tanning Bed': {'north': 'Weight Room', 'west': 'Front Desk', 'item': 'sunglasses'},
        'Weight Room': {'south': 'tanning bed', 'item': 'gym bro'}
    }

    #gameplay loop, runs until player enters Weight Room
    while current_room != 'Weight Room':
        #show status and obtain command
        show_status(current_room, rooms, inventory)
        print('-----------------------')
        user_input = input(str('Please enter a command:')).lower()
        #split user input
        user_input = user_input.split()
        #check for exit command
        if user_input == ['exit']:
            sys.exit('Exiting the game, thank you for playing!')
        #check first word of user input, if "go", execute change room function
        if user_input[0] == 'go':
            verb = user_input[0]
            direction = user_input[1]
            current_room = change_room(direction, rooms, current_room)
        #if first word is "get", combine words two and three as item name if necessary
        #execute get_item function
        elif user_input[0] == 'get':
            if len(user_input) <= 2:
                noun = user_input[1]
            else:
                noun = user_input[1] + ' ' + user_input[2]
            inventory = get_item(inventory, noun, rooms, current_room)
        else:
            print('invalid entry')
    #winning condition upon entering Weight Room
    if len(inventory) == 6:
        print('Congratulations, you win the game! You brought the gym bro all of his things')
    else:
        print('Game Over, you need to collect all of the items before you enter the weight room. Please try again')

if __name__ == '__main__':
    main()

