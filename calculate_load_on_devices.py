from numpy import int16

def main(src, dest):
    import numpy as np

    data = np.genfromtxt(src, delimiter=',', usecols=(7, 2), skip_header=1, dtype=['U15', np.uint16])

    count_unique = {}
    for row in data:
        name = row[0]
        t = (str(row[0]), int(row[1]))
        if t not in count_unique:
            count_unique[t] = 0
        count_unique[t] += 1

    result = []
    for device, iter in count_unique.keys():
        count = count_unique[(device, iter)]
        result.append([device, iter, count])
    
    result = np.array(result)
    result = result[result[:, 1].argsort(kind='stable')]
    result = result[result[:, 0].argsort(kind='stable')]

    np.savetxt(dest, result, fmt=['%s','%s','%s'], delimiter=',', comments='', header='IoTDeviceName,Iteration,Count')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(f'Incorrect number of arguments: {len(sys.argv) - 1}; should be 2\n')
        print('Correct use looks like:')
        print(f'\tpython {sys.argv[0]} <src-filename>.csv <dst-filename>.csv')
        sys.exit('')
    
    source = f'osmosis_csv/{sys.argv[1]}'
    dest = f'outputStats/{sys.argv[2]}'
    main(source, dest)
