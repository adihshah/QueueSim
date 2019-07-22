import numpy as np  
import statistics as S
import matplotlib.pyplot as mp


class customer:
    def __init__(self, arrival, service, patience, time, adjServ):
        self.interArrivalTime = arrival
        self.service_time = service
        self.patience_threshold = patience
        self.absolute_time = time

     

class serviceStation:
    def __init__(self, c , t):
        self.customer = c
        self.timeRemaining = t
       
    #Function Information
    #This function is a simulation of a (GI/GI/1 + GI ) queue.
    
    #Inputs
    #t := time vector such as [0:.001:10]
    #ar := interarrival time vector
    #s := service duration time vector
    #ab := abandonment threshold time vector
    #N := the number of operating service stations
def queueSim (t, ar, s, ab, N):

    # Initialize N empty service stations
    serviceList = []
    for i in range(0,N):
        serviceList.append(0)
    
    # A list (to be filled with customers) that represents the queue
    queueList = []
    queueList.append(customer(ar[0], s[0], ab[0], ar[0], s[0]))

    
    # A list of computed wait times for each customer
    W = []
    
    # A list of LES wait times for each customer
    LES = []
    LES.append(0)

    
    # A list containing the absolute times at which each customer arrives
    N = []
    N.append(ar[0])
    
    LESindices = []
 
    
    # Dummy indices
    i = 1
    LESindex = -1
    
    # Flag variable for ending the simulation
    end = False 
    
    
    for z in t:
        while (N[i-1] < z):
            
            # Update service timers
            serviceList = [x - ar[i] for x in serviceList]
            temp = all(y>0 for y in serviceList)

            # Store the absolute arrival time for the entering customer
            N.append(ar[i] + N[i-1])
            
     

            # Update the state of the queue
            while (temp==False and len(queueList) != 0):
                index_min = serviceList.index(min(serviceList))
                W.append(abs(round(N[i] - queueList[0].absolute_time + serviceList[index_min], 10)))
                serviceList[index_min] = serviceList[index_min] + queueList[0].service_time
                LESindex = LESindex + 1
                queueList.pop(0)
                temp = all(y>0 for y in serviceList)
            serviceList = [max(0, y) for y in serviceList] 
            LESindices.append(LESindex)
            

            # Construct the entering customer and place them in the queue
            queueList.append(customer(ar[i], s[i], ab[i], N[i], s[i]))
         
            
            # Remove any customers that renege prior to the entering customer's arrival time
            for a in queueList:
                if N[i] - a.absolute_time >= a.patience_threshold:
                    a.service_time = 0
                    
            
            # Incremement the system
            i = i + 1
            
            # Simulation exits if it reaches the end of the input data
            if i == len(ar) :
                end = True;
                break;
        if end:
            break;
     # Update service timers
    serviceList = [x - 10000000 for x in serviceList]
    temp = all(y>0 for y in serviceList)
            
            # Store the absolute arrival time for the entering customer
    N.append(10000000 + N[i-1])
                   
    while (temp==False and len(queueList) != 0):
                index_min = serviceList.index(min(serviceList))
                W.append(N[i] - queueList[0].absolute_time + serviceList[index_min])
                serviceList[index_min] = serviceList[index_min] + queueList[0].service_time
                queueList.pop(0)
                temp = all(y>0 for y in serviceList)

                
    
    for i in LESindices:
        LES.append(W[i])
    print(W)      
    print(LES)
    
    sum = 0
    for x in W:
        sum = sum+x
        
    Wnd = np.array(W)
    
    
    print ("Median is" + np.median(W))
    
    sum2 = 0
    
    for x in LES:
        sum2 = sum2+x
        
    print (sum2/len(LES))
    #print(N)= range(0,100)*(max(A)/100))
    print(np.corrcoef(W, LES))
    return np.corrcoef(W, LES)
    #print(W)
    #A = [a for a in W if a > 0]
    #mp.hist(A,bins = range(0,100)*(max(A)/100))
    #mp.show()
    
 

#queueSim([0,1000],[1,2,3,4,5,6,7,8],[15,2,6,5,4,3,2,1],[1,10,3,4,5,1,2,1],1)
#print(les)
#print(delayK(les, 5))   
    
    
    
    
interArrival = np.random.exponential(.01,1000000)
serviceTimes = np.random.exponential(1,1000000)
abandonTimes = np.random.exponential(10,1000000)
queueSim([0,1000000], interArrival, serviceTimes, abandonTimes, 100)
#print(interArrival)
#print(serviceTimes)
#200, 400, 500, 1000
"""nValues = [10, 20, 50, 100, 200, 400, 500, 1000]
thetaValues = [0.5, 1, 2]

correlations = []
finalCorrelations = []
for j in thetaValues:
    correlations.clear()
    finalCorrelations.clear()
    for i in nValues:
        interArrival = np.random.exponential((1/i),1000000)
        serviceTimes = np.random.exponential(1,1000000)
        abandonTimes = np.random.exponential(j,1000000)
        correlations.append(queueSim([0,10000000], interArrival, serviceTimes, abandonTimes, i))

    for k in correlations:
        finalCorrelations.append(k[0][1])
    print(finalCorrelations)"""
#mp.scatter(nValues, [0.002322526754264176, 0.0013782589924879116, 0.0059806714379514615, 0.0039168067865585484, 0.02198516180472931, 0.008364244289894362, 0.0244543757913225, 0.028995109711077955] )
