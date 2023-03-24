import numpy as np
import matplotlib.pyplot as plt

class Simple_graph():

    def __init__(self) -> None:
        
        self.fig = plt.figure()

        return None

    def __add_point_on_g__(self, x, y) -> None:
        

        scatter1 = plt.scatter(0.0, 1.0)
        #print('Scatter: ', type(scatter1))
        grid1 = plt.grid(True) # линии вспомогательной сетки
        plt.show()

        return None
    def __add_line__(self):

        graph1 = plt.plot([-1.0, 1.0], [0.0, 1.0])

        return None
    def draw(self):

        self.__add_line__()
        self.__add_point_on_g__(10, 10)

        return None