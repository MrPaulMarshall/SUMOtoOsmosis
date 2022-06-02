def print_error(argv):
    print(f'Incorrect number of arguments: {len(argv) - 1}; should be 2\n')
    print('Correct use looks like:')
    print(f'\tpython {argv[0]} <src-filename>.csv <dst-filename>.csv')

def mkdir(dst):
    import os
    path_struct = dst.split('/')
    if len(path_struct) > 1:
        os.makedirs('/'.join(path_struct[:-1]), exist_ok=True)

def aggregate_load_data_from_devices(src, dst):
    import pandas as pd

    data = pd.read_csv(src, usecols=['DestinationVmName', 'Iteration'])[['DestinationVmName', 'Iteration']]
    aggregated = data.groupby(['DestinationVmName', 'Iteration']).size().reset_index(name='Count')

    aggregated.to_csv(dst, index=False)

def main(src, dst):
    mkdir(dst)
    aggregate_load_data_from_devices(src, dst)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print_error(sys.argv)
        sys.exit('')

    source = sys.argv[1]
    dest = sys.argv[2]
    main(source, dest)
