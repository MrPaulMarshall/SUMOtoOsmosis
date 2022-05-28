from numpy import int16

def extract_dir_path(dst):
    path_struct = dst.split('/')
    
    if len(path_struct) == 1:
        return ''
    else:
        return '/'.join(path_struct[:-1])

def mkdir(dst):
    import os
    dir_path = extract_dir_path(dst)
    if len(dir_path) > 0:
        os.makedirs(dir_path, exist_ok=True)

def aggregate_load_data_from_devices(src, dst):
    import pandas as pd

    data = pd.read_csv(src, usecols=['DestinationVmName', 'Iteration'])[['DestinationVmName', 'Iteration']]
    aggregated = data.groupby(['DestinationVmName', 'Iteration']).size().reset_index(name='Count')

    aggregated.to_csv(dst, index=False)

def main(src, dst):
    mkdir(dst)
    aggregate_load_data_from_devices(src, dst)

def validate_args(argv):
    import sys
    if len(argv) != 3:
        print(f'Incorrect number of arguments: {len(argv) - 1}; should be 2\n')
        print('Correct use looks like:')
        print(f'\tpython {argv[0]} <src-filename>.csv <dst-filename>.csv')
        sys.exit('')

    if len(argv[1]) < 1 or len(argv[2]) < 1:
        print('Invalid argument: empty string')
        sys.exit('')

if __name__ == '__main__':
    import sys
    validate_args(sys.argv)
    
    source = sys.argv[1]
    dest = sys.argv[2]
    main(source, dest)
