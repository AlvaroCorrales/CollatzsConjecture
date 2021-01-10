#%% CREATE CLASS TO COMPUTE THE SEQUENCE ARISING FROM COLLATZ'S CONJECTURE
# Alvaro Corrales Cano
# January 2020
# For more info about Collatz's conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture

#%% Import required libraries
import numpy as np
import matplotlib.pyplot as plt

#%% Define class
# We'll assign two methods: we can either just calculate the sequence or calculate the sequence and plot it

class Collatz:
    
    def __init__(self, initial_numbers):
        
        self.initial_numbers = initial_numbers
    
    # 1. Calculate sequence for several initial points and plot results
    def sequence(self, iterations = 100, plot = False):
        
        """
        Implements function in Collatz's conjecture for a starting point 'initial_number'
        (integer) and a number of 'iterations'. It plots the results if plot == True 
        (by default plot = False)
        """
        
        # Initialize sequence        
        starting_points = []
        try:
            starting_points.extend(self.initial_numbers)
        except:
            starting_points.append(self.initial_numbers)    
        

        seq = np.zeros((iterations, len(starting_points)))
        seq[0] = starting_points
        
        # Sequence
        for j in range(len(starting_points)): # Iterate over columns (number of sequences)
            
            for i in range(1, iterations): # iterate over rows (values of sequence)
                
                if seq[i-1, j] % 2 == 0:
                    seq[i, j] = seq[i-1, j] / 2
                else:
                    seq[i, j] = seq[i-1, j] * 3 + 1
        
        # Plot
        if plot == True:

            plt.plot(seq)
            plt.title("Collatz's sequence for selected starting points")
            plt.xlabel('Iterations')
            plt.ylabel('Value of sequence')
            plt.legend(starting_points)
            plt.show()  
        
        return np.asarray(seq)
    
    # 2. Compute stopping times       
    def stopping_times(self, plot = False, bins = 100):
        
        """
        Calculates the time until a Collatz sequence starting at 'initial_number' (integer)
        before it converges to 1. 
        
        It also plots the results: if plot ==  'scatter', it plots the number of 
        interations for each initial number in a scatter. If plot == 'hist', it 
        reports an histogram of the distribution the number of iterations needed 
        for convergence over the list of initial numbers (set False by default).
        """
        
        i = []
        
        # Initialize sequence - try to pass to list with length > 1, otherwise just 0  
        try: # Case when we have a list of numbers passed as argument
            last_iteration = list(np.ones(len(self.initial_numbers)))
            i.extend(self.initial_numbers)
        
        except: # Case when we have just an integer passed as argument
            last_iteration = [1]
            i.append(self.initial_numbers)
            
        # Compute stopping times for each input   
        for j in range(len(i)):
        
            while i[j] != 1:
                
                if i[j] % 2 == 0:
                    i[j] = i[j] / 2
                else:
                    i[j] = i[j] * 3 + 1
                
                last_iteration[j] += 1
        
        # Plot
        if plot == 'scatter':
            
            plt.scatter(x = self.initial_numbers, y = last_iteration, 
                        marker = ".", edgecolors = 'blue', facecolors = 'white')
            plt.xlabel('Starting point')
            plt.ylabel('Number of iterations')
            plt.title("Iterations before Collatz's sequence converges to 1")
            plt.show()
            
        elif plot == 'hist':
            
            plt.hist(x = last_iteration, bins = bins, color = 'darkblue')
            plt.title("Distribution of iterations before Collatz's seq. converges to 1")
            plt.xlabel('Number of iterations')
            plt.ylabel('Frequency')
            plt.show()
            
        elif plot != False and plot != 'hist' and plot != 'scatter':
            print("ERROR: Please set plot = False or enter a valid plot name: 'hist' or 'scatter'")
            
        return np.asarray(last_iteration)
    
    # 3. Compute highest value in the sequence given a starting point
    def max_value(self, plot = False, ylim = False):
        
        """
        Computes the highest number reached by the Collatz sequence generated from 
        initial_numbers. 
        It also plots a scatter of the maximum points by starting point when plot = True
        (False by default). ylim = tuple allows to set the limits of the y axis in 
        the plot s.t. bottom = y[0] top = y[1].
        """
        i = []
        candidates = []
        max_number = []
        
        # Initialize sequence - try to pass to list with length > 1, otherwise just 0  
        try: # Case when we have a list of numbers passed as argument
            last_iteration = list(np.ones(len(self.initial_numbers)))
            check_point = list(np.zeros(len(self.initial_numbers)))
            candidates.extend(self.initial_numbers)
            i.extend(self.initial_numbers)
            max_number.extend(self.initial_numbers)
        
        except: # Case when we have just an integer passed as argument
            last_iteration = [1]
            check_point= [0]
            candidates.append(self.initial_numbers)
            i.append(self.initial_numbers)
            max_number.append(self.initial_numbers)
        
        # Compute length of sequence until convergence
        for j in range(len(i)):
        
            while i[j] != 1:
                
                if i[j] % 2 == 0:
                    i[j] = i[j] / 2
                else:
                    i[j] = i[j] * 3 + 1
                
                last_iteration[j] += 1
        
        # Compute maximum of each sequence
        for j in range(len(candidates)):
            
            while check_point[j] < last_iteration[j]:
                
                if candidates[j] % 2 == 0:
                    candidates[j] = candidates[j] / 2
                    if max_number[j] <= candidates[j]: max_number[j] = candidates[j] 
                else:
                    candidates[j] = candidates[j] * 3 + 1
                    if max_number[j] <= candidates[j]: max_number[j] = candidates[j] 
                
                check_point[j] += 1
        
        # Plot
        if plot == True:
            
            plt.scatter(x = self.initial_numbers, y = max_number,
                        marker = ".", edgecolors = 'red', facecolors = 'white')
            plt.xlabel('Starting point')
            plt.ylabel('Maximum of the sequence')
            plt.title("Max of Collatz's sequence for different starting points")
            if ylim != False: plt.ylim(bottom = ylim[0], top = ylim[1])
            plt.show()
       
        return np.asarray(max_number)
                               
    
#%%Test
#seq_test = Collatz([454, 8090]).sequence(plot = True)
#stop_test = Collatz([235, 345, 982]).stopping_times()
#stop_test = Collatz(list(range(1, 1000000, 1))).stopping_times(plot = 'hist', bins = 200)       
max_test = Collatz(list(range(1, 10000, 1))).max_value(plot = True, ylim = (0, 100000))