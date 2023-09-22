import status.npc_health as enemy_health
import status.health as player_health
import cmd_parser.command_manager as cm
import inventory.contents as inventory
import random

def npc_won_fight():
    result = False
    npc_strength = enemy_health.get()[1]
    print("NPC won fight", npc_strength)
    npc_hit = random.randrange(1, npc_strength )
    player_hit = random.randrange(1, player_health.get()[1])
    return npc_hit > player_hit
    

def fight(game_place):
    """

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """

    result = ""
    if inventory.has_item('sword'):
        if npc_won_fight():
            player_health.reduce(enemy_health.get()[1])
            if player_health.get()[0] <= 0: 
                player_health.increase(100)
                cm.move((cm.move, 'Forest'))
                result = "you lost you have been resurrected in the forest\n" + cm.show_current_place()
            else:
                result = "Enemy attacked you but you survived\n" + cm.show_current_place()    
        else: 
            if enemy_health.get()[0] <= 0:
                cm.move((cm.move, 'CastleFoyer'))
                result = "Enemy dead you continue through the castle\n" + cm.show_current_place()
            else:
                enemy_health.reduce(player_health.get()[1])
                result = "Enemy took damage\n" + cm.show_current_place() 
    else:
        result = "Visit the blacksmith to get a sword.\n"+cm.show_current_place()
    return result

