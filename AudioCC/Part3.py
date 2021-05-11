# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np



# Create the vectors X and Y
x = np.array(range(100))


equation = input('Enter equation:\n')
y = equation

def graph(x,y):
    # Create the plot
    plt.plot(x,y)

    # Show the plot
    plt.show()

    
graph(x,y)