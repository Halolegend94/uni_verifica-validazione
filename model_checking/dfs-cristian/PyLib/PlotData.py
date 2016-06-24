#funzione per plottare i dati
import matplotlib.pyplot as plt
def plotData(rows, cols, arraydict, vals):
    fig = 1
    plt.figure()
    t = vals['time']
    xend = max(t)

    for i in range(0, len(arraydict)):
        plt.subplot(rows,cols, fig)
        currentRange = vals[arraydict[i]]
        plt.plot(t, currentRange)
        plt.grid()
        ma = max(currentRange)
        mi = min(currentRange)
        r =  ma - mi
        factor = 0.2

        if ma == mi:
            r = 1
            factor = 1

        plt.axis([0, xend, mi -factor*r, ma + factor*r])
        plt.title(arraydict[i])
        fig = fig + 1
    plt.show()
    return
