"""_summary_

"""
_player_inventory = set()


def collect_item(item_name):
    _player_inventory.add(item_name)


def remove_item(item_name):
    _player_inventory.remove(item_name)


def has_item(item_name):
    return item_name in _player_inventory


def all_inventory():
    all = []
    for item_name in _player_inventory:
        all += [item_name]
    return all

if __name__ == "__main__":
    print(remove_item('sword'))
    pass
