class whatEver:
    def __init__(self):
        pass

class whatEver2(whatEver):
    """docString"""
    def __init__(self, hei: int = 0):
        super().__init__()
        self.hei = hei

    def someMethod(self) -> int:
