import types
_npc_health_value: int = 500
_strength: int = 40


def get():
    return _npc_health_value, _strength


def reduce(pValue):
    global _npc_health_value
    _npc_health_value -= pValue


def increase(pValue):
    global _npc_health_value
    _npc_health_value += pValue

if __name__ == "__main__":
    test = input("Hello")
    print(reduce(test))
    pass