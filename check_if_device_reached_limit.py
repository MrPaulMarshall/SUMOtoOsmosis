from numpy import int16

def main(device_id, limit, src):
    import numpy as np

    data = np.genfromtxt(src, delimiter=',', usecols=(7, 2), skip_header=1, dtype=np.object_)#, dtype=['U15', np.uint16])
    iterations = data[data[:, 0] == device_id.encode('utf-8')][:, 1]

    count_unique = {}
    for row in iterations:
        it = int(row)
        if it not in count_unique:
            count_unique[it] = 0
        count_unique[it] += 1

    result = []
    count_exceeded = 0
    for iter in count_unique.keys():
        count = count_unique[iter]
        result.append([iter, count])
        if count > limit:
            count_exceeded += 1
    
    result = np.array(result)
    result = result[result[:, 0].argsort(kind='stable')]

    print(f'Device \'{device_id}\' has exceeded its limit of {limit} request on {count_exceeded} turns')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print(f'Incorrect number of arguments: {len(sys.argv) - 1}; should be 3\n')
        print('Correct use looks like:')
        print(f'\tpython {sys.argv[0]} <device-id> <limit> <src-filename>.csv')
        sys.exit('')
    
    device_id = sys.argv[1]
    limit = int(sys.argv[2])
    source = f'osmosis_csv/{sys.argv[3]}'
    main(device_id, limit, source)
