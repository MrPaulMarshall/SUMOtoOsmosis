from numpy import int16

def count_turns_with_exceeded_limit(device_id, limit, src):
    import pandas as pd

    data = pd.read_csv(src, usecols=['DestinationVmName', 'Iteration'])[['DestinationVmName', 'Iteration']]
    iterations = data[data['DestinationVmName'] == device_id]
    aggregated = iterations.groupby('Iteration').size().reset_index(name='Count')
    exceeded = aggregated[aggregated['Count'] > limit]

    print(exceeded.shape[0])

def main(device_id, limit, src):
    count_turns_with_exceeded_limit(device_id, limit, src)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print(f'Incorrect number of arguments: {len(sys.argv) - 1}; should be 3\n')
        print('Correct use looks like:')
        print(f'\tpython {sys.argv[0]} <device-id> <limit> <src-filename>.csv')
        sys.exit('')
    
    device_id = sys.argv[1]
    limit = int(sys.argv[2])
    source = sys.argv[3]
    main(device_id, limit, source)
