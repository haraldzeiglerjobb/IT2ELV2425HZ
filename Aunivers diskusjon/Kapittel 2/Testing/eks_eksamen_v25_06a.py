class Batteri:

    def __init__(batteriID: str = "", energinivå: float = 0.0, energikapasitet: float = 0.0):
        __batteriID = batteriID
        __energinivå = energinivå
        __energikapasitet = energikapasitet

    def ladOpp(self, energi: float = 0.0) -> None:
        self.__energinivå += energi

    def brukEnergi(self, energi: float = 0.0) -> None:
        self.__energinivå -= energi

    def visEnerginivå(self) -> float:
        print("Energinivået er ",__energinivå)

