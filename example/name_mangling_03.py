from datetime import datetime


class Foo:
    def __get(self):
        return self.__class__.__name__

    def get_name(self):
        return self.__get()


class Boo(Foo):
    def _get(self):
        return datetime.now()

    def get_time(self):
        return self._get()


assert Boo().get_name() == "Boo"
