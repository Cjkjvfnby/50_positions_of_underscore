from datetime import datetime


class Foo:
    def _Foo__get(self):
        return self.__class__.__name__

    def get_name(self):
        return self._Foo__get()


class Boo(Foo):
    def _get(self):
        return datetime.now()

    def get_time(self):
        return self._get()


assert Boo().get_name() == "Boo"
