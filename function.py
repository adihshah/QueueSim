import numpy as np
import matplotlib.pyplot as plt


def getdata(LES, Wait):
    gamma = 20
    alphalist = np.arange(0, 1.01, 0.01)
    MSEgamma = []
    #MSE2 = []
    #MSE1andhalf = []
    Abs = []
    avg = sum(Wait)/len(Wait)
    median = np.median(Wait)
    for alpha in np.arange(0, 1.01, 0.01):
        i = 0
        Rkmse = []
        Rkabs = []
        #Rkmse2 = []
        #Rkmse1andhalf = []
        for x in LES:
            Ralpha = (alpha*x + (1-alpha)*avg)
            #Ralpha = (alpha*x + (1-alpha)*median)

            #Rkmse2.append((Ralpha - Wait[i])**2)
            #Rkmse1andhalf.append((Ralpha - Wait[i])**1.5)

            Rkmse.append(max(Ralpha - Wait[i], 0) +
                         gamma*max(Wait[i] - Ralpha, 0))
            Rkabs.append(abs(Ralpha - Wait[i]))
            i = i+1
        MSEgamma.append(sum(Rkmse)/len(Rkmse))
        # MSE2.append(np.mean(Rkmse2))
        # MSE1andhalf.append(np.mean(Rkmse1andhalf))
        Abs.append(sum(Rkabs)/len(Rkabs))

    plt.subplot(2, 1, 1)
    plt.plot(alphalist, MSEgamma)
    plt.ylabel('MSE')
    plt.xlabel('alpha')
    ymax = min(MSEgamma)
    xpos = MSEgamma.index(ymax)
    xmax = alphalist[xpos]
    plt.annotate('local min', xy=(xmax, ymax), xytext=(xmax, ymax),
                 arrowprops=dict(facecolor='black', shrink=0.05),)

    plt.subplot(2, 1, 2)
    plt.plot(alphalist, Abs)
    plt.ylabel('Abs')
    plt.xlabel('alpha')
    ymax2 = min(Abs)
    xpos2 = Abs.index(ymax2)
    xmax2 = alphalist[xpos2]
    plt.annotate('local min', xy=(xmax2, ymax2), xytext=(xmax2, ymax2),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    plt.show()

    #print (MSE)
    #print ("ABS IS")
    #print (Abs)
    # return [MSE, Abs]


# getdata([1,2,4,5,3,2,1],[2,3,4,5,1,3,1])
