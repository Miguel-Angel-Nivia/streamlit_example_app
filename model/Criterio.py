import json


class Criterio:

    def __init__(self, descripcion, categoria):
        self._descripcion = descripcion
        self._categoria = categoria

    def __str__(self) -> str:
        return json.dump(self.__dict__)
