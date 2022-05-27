from numpy import int16

def aggregate_load_data_from_devices(src, dst):
    import pandas as pd

    data = pd.read_csv(src, usecols=['DestinationVmName', 'Iteration'])[['DestinationVmName', 'Iteration']]
    aggregated = data.groupby(['DestinationVmName', 'Iteration']).size().reset_index(name='Count')

    aggregated.to_csv(dst, index=False)

def main(src, dst):
    aggregate_load_data_from_devices(src, dst)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(f'Incorrect number of arguments: {len(sys.argv) - 1}; should be 2\n')
        print('Correct use looks like:')
        print(f'\tpython {sys.argv[0]} <src-filename>.csv <dst-filename>.csv')
        sys.exit('')
    
    source = sys.argv[1]
    dest = sys.argv[2]
    main(source, dest)
