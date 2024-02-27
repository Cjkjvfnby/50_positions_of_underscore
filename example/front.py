def _foo():
    print("Don't use me outside of this file!")


class Greeter:
    def _check_name(self, name: str) -> bool:
        return name[0].isupper()

    def __init__(self, name):
        if self._check_name(name):
            self._name = name
        else:
            msg = f"Name should start from capital letter, got: {name}"
            raise ValueError(msg)

    def greet(self):
        """
        Greet user.
        """
        print(f"Hello {self._name}")
