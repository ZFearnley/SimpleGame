"""_summary_
Manages the commands - may not be the best name at this time

"""
# import typing
import cmd_parser.token as token
import inventory.contents as inventory
import status.health as health
import fighting.fight as battle

# Game commands


def move(game_place):
    """_summary_

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state

    location = game_place[1]
    game_state = location

    story_result = show_current_place()

    return story_result


def talk_to_hermit(game_place):
    """_summary_
        Hermit gives a key
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("key")
    return move(game_place)

def talk_to_blacksmith(game_place):
    """_summary_
        Blacksmith gives a sword
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("sword")
    return move(game_place)

def enter_castle(game_place):
    result = ""
    if inventory.has_item('key'):
        result = move(game_place)
    else:
        result = "Visit the hermit to recieve a key to enter the castle.\n"+show_current_place()
    return result




game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the east is a Village.\nTo the south is a castle.\nTo the west is a swamp',
                          'North': (move, 'Cave'), 'East': (move, 'Village'), 'South': (move, 'Castle'), 'West': (move, 'Swamp'),  'Image': 'forest.png'},
               'Cave': {'Story': 'You are at the hermit\'s cave.\n Talk to the hermit? To the south is forest.',
                        'South': (move, 'Forest'), 'Talk': (talk_to_hermit, 'Hermit'), 'Image': 'forest_circle.png'},
               'Village': {'Story': 'You are in a village.\n Talk to the blacksmith?\nTo the west is forest.',
                           'West': (move, 'Forest'), 'Talk': (talk_to_blacksmith, 'Blacksmith'), 'Image': 'village.png'},        
               'Castle': {'Story': 'You are at the castle.\n Enter the castle?\nTo the north is forest.',
                          'North': (move, 'Forest'), 'Enter': (enter_castle, 'InCastle'), 'Image': 'frog.png'},
               'Hermit': {'Story': 'The hermit does not talk, but gives you a key.\n To the south is forest.',
                          'South': (move, 'Forest'), 'Image': 'frog.png'},
               'Blacksmith': {'Story': 'The blacksmith offers you a free sword.\n To the west is forest.',
                              'West': (move, 'Forest'), 'Image': 'village.png'},
               'InCastle': {'Story': 'You are inside the Castle.\n A knight is standing in front of you with sword drawn.\n You can leave, or fight.', "Leave": (move, "Castle"), "Fight": (battle.fight, "Castle"), 'Image': 'frog.png'},
               'Battle': {'Story'},
               'CastleFoyer': {'Story': 'You defeated the Knight.\n You are in the main foyer of the castle\n The door shuts behind you and you can not return that way.\n to the south is a locked room.\n to the east is a ktichen. \n to the west is a stairwell', "East": (move, "Kitchen"), "West": (move, "Stairwell"), 'Image': 'frog.png'}
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    health.reduce(10)  # Lose health as you move
    current_health, current_strength = health.get()
    return f"[Health={current_health}]\nStrength={current_strength}\n"+game_places[game_state]['Story']


def game_play(command_input):
    """
    Runs the game_play

    Args:
        command input string:
    Returns:
        string: the story at the current place, after an action
    """
    global game_state
    story_result = ''
    valid_tokens = token.valid_list(command_input)
    if not valid_tokens:
        story_result = 'Can not understand that sorry\n'+show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            the_place = atoken.capitalize()
            if the_place in game_place:
                place = game_place[the_place]
                story_result = place[0](place)  # Run the action
            else:
                story_result = f"Can't {the_place} here\n"+show_current_place()
    return story_result
