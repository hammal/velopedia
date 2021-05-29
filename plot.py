import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    plt.rcParams['figure.figsize'] = [12, 8]
    fig = plt.figure()
    ax = plt.gca()
    x = np.arange(5)
    y = np.sqrt(x)
    ax.plot(x,y)
    
    ax.text(1,1, 'Bike', fontsize=15)
    ax.text(3,2, 'Velo', fontsize=15)
    ax.set_xlabel('Gravel')
    ax.set_ylabel('?')
    plt.savefig('docs/plt.svg')
    # plt.show()