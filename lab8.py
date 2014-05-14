import matplotlib.pyplot as plt

class Plot(object):
    def __init__(self):
        self.poly = []
        self.fig, self.ax = plt.subplots()
        self.ax.axis([0, 10, 0, 10])
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        plt.show()

    def on_click(self, event):
        if event.button == 1:
            self.poly.append((event.xdata, event.ydata))
        elif event.button == 3:
            self.draw_poly()

    def draw_poly(self):
        self.ax.clear()
        self.ax.axis([0, 10, 0, 10])
        self.ax.fill(*zip(*self.poly))
        self.poly = []
        self.fig.canvas.draw()

Plot()
