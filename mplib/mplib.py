import pickle
import math
import matplotlib.pyplot as plt

# Кто трогал код
# X = [i for i in range(-9, 10)]
# Q = [2, 4]
# V = [3, 5]
# B = [2, 5]
# STYLES = ["-", '--', '-.']
# WIDTH = [1, 2, 3]
# k = 0
# for i in B:
#     for j in V:
#         for m in Q:
#             y = []
#             for n in X:
#                 y.append(math.sin(n * math.pi / 4) * m * i * j)
#             plt.plot(X, y, linestyle=STYLES[k//3], linewidth=WIDTH[k%3], label=f'q = {m}, v = {j}, B = {i}')
#             plt.legend()
#             k+=1
# ax = plt.gca()
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.plot((1), (0), marker=">", ms=7, color="k",
#         transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot((0), (1), marker="^", ms=7, color="k",
#         transform=ax.get_xaxis_transform(), clip_on=False)

# plt.title(r"$Fл=q\cdot v\cdot B\cdot sin\alpha$")
# plt.xlabel(r"$\alpha$")
# plt.show() 


class LorenzPowerGraph:
    data = []
    Q = [2, 4]
    V = [3, 5]
    B = [2, 5]
    STYLES = ["-", '--', '-.']
    WIDTH = [1, 2, 3]
    Y = []
  

    def __init__(self, data=[], q=[], v=[], b=[]):
        self.data = data
        self.Q = q
        self.B = b
        self.V = v
      

    def calculate_Y(self):
        X = self.data
        for i in self.B:
            for j in self.V:
                for m in self.Q:
                    y = []
                    for n in X:
                        y.append(math.sin(n * math.pi / 4) * m * i * j)
                    self.Y.append(y)


    def build_graph(self):
        X = self.data
        k = 0
        for i in self.B:
            for j in self.V:
                for m in self.Q:
                    y = self.Y[k]
                    plt.plot(X, y, linestyle=self.STYLES[k//3], linewidth=self.WIDTH[k%3], label=f'q = {m}, v = {j}, B = {i}')
                    plt.legend()
                    k+=1
        ax = plt.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.plot((1), (0), marker=">", ms=7, color="k",
                transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), marker="^", ms=7, color="k",
                transform=ax.get_xaxis_transform(), clip_on=False)

        plt.title(r"$Fл=q\cdot v\cdot B\cdot sin\alpha$")
        plt.xlabel(r"$\alpha$")
        plt.show() 


    def import_data(self, file):
        with open(file, "rb") as f:
            a = pickle.load(f)
        self.Q, self.V, self.B, self.data, self.Y = a[0], a[1], a[2], a[3], a[4]


    def export_data(self, file):
        with open(file, "wb") as f:
            pickle.dump((self.Q, self.V, self.B, self.data, self.Y), f)
                        

a = LorenzPowerGraph([x for x in range(-9, 10)], [2, 3], [3, 6], [7, 5])
a.calculate_Y()
a.export_data("a.pickle")
b = LorenzPowerGraph()
b.import_data("a.pickle")
b.build_graph()