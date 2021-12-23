import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

def realTimePlot(xLabels, yData, line1, identifier='', pause=0.1):
    if line1 == []:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(xLabels, yData, '-o', alpha=0.5)
        plt.ylabel('Tempo')
        plt.title('{}'.format(identifier))
        plt.subplots_adjust(left=0.04, bottom=0.04, right=1, top=1)
        plt.show()

    line1.set_ydata(yData)
    #if np.min(yData) <= line1.axes.get_ylim()[0] or np.max(yData) >= line1.axes.get_ylim()[1]:
    plt.ylim([np.min(yData)-np.std(yData), np.max(yData)+np.std(yData)])
    plt.pause(pause)
    return line1