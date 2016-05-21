#funzione per plottare i dati
import matplotlib.pyplot as plt
def plotData(rows, cols, arraydict, vals):
    fig = 1
    t = vals['time']
    xend = max(t)
    for i in range(0, len(arraydict)):
        plt.subplot(rows,cols, fig)
        currentRange = vals[arraydict[i]]
        plt.plot(t, currentRange)
        plt.grid()
        plt.axis([0,xend,min(currentRange) - 1, max(currentRange) + 1])
        plt.title(arraydict[i])
        fig = fig + 1
    plt.show()
    return
