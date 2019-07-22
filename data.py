import function
import numpy as np
data = np.genfromtxt("/Users/adityashah/Desktop/2.txt")
wait = np.ndarray.tolist(data[:, 4])
les = np.ndarray.tolist(data[:, 5])

function.getdata(les, wait)


#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [1, 1, 1, 2, 10, 2, 1, 1, 1, 1]

'''line, = ax.plot(x, y)

ymax = max(y)
xpos = y.index(ymax)
xmax = x[xpos]

ax.annotate('local max', xy=(xmax, ymax), xytext=(xmax, ymax+5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.show()'''
