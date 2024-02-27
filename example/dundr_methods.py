class Foo:
    def __init__(self, value: int):
        self._value = value

    def __add__(self, other):
        return Foo(self._value + other._value)

    def __hash__(self):
        return hash(self._value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._value})"


one = Foo(1)
two = Foo(2)
three = Foo(1) + Foo(2)

print(one, two, three)
print(hash(one))
