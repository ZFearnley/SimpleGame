import types
_health_value: int = 1000
_strength: int = 50


def get():
    return _health_value, _strength


def reduce(pValue):
    global _health_value
    _health_value -= pValue


def increase(pValue):
    global _health_value
    _health_value += pValue

if __name__ == "__main__":
    test = input("Hello")
    print(reduce(test))
    pass