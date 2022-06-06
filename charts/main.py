import pandas as pd
import matplotlib.pyplot as plt


def number_of_requests_per_iteration(path, title):
    df = pd.read_csv(path)

    df2 = df.groupby(['Iteration'])['Iteration'].count().reset_index(name='Counts')

    print(df2)

    x_axis = df2['Iteration']
    y_axis = df2['Counts']

    plt.plot(x_axis, y_axis)
    plt.hlines(y=y_axis.max(), xmin=x_axis.min(), xmax=x_axis.max(), color='red', label='test')
    plt.title(f'Number of requests per iteration ({title})')
    plt.xlabel('Iteration')
    plt.ylabel('Number of requests')
    plt.show()


if __name__ == '__main__':
    number_of_requests_per_iteration('Test_Simulation_Berlin_100.csv', 'all within distance')
    number_of_requests_per_iteration('Test_Simulation_Berlin_100_nearest_neighbours.csv', 'nearest neighbours')
