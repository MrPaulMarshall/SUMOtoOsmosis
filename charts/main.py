import pandas as pd
import matplotlib.pyplot as plt


def number_of_requests_per_iteration(path):
    df = pd.read_csv(path).groupby(['Iteration'])['Iteration'].count().reset_index(name='Counts')

    x_axis = df['Iteration']
    y_axis = df['Counts']

    plt.plot(x_axis, y_axis)
    plt.title('Number of requests per iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Number of requests')
    plt.show()


if __name__ == '__main__':
    number_of_requests_per_iteration('Test_Simulation_Berlin_100.csv')
