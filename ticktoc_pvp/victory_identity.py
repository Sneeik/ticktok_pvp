class VictoryIdentity:
    def __init__(self, id: int):
        self.__id = id
        
    @property
    def id(self) -> int:
        return self.__id
