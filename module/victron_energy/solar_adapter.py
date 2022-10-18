import module
from module.module import Module

class SolarAdapter(Module):
    def __init__(self):
        print(self.name)

    def description() -> str:
        return "Victron solar adapter"