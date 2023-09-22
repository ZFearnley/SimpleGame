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
