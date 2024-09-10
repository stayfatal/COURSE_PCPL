class FigureColor:
    def __init__(self):
        self.__color=None

    @property
    def color(self): return self.__color

    @color.setter
    def color(self,color): self.__color=color
        