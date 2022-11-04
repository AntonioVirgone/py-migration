import numpy as np


class SplitArrayService:
    @staticmethod
    def split(array, nSection):
        result = np.array(array)
        # splitting the array into two
        new_array1 = np.array_split(result, nSection)
        print('Tne newly split arrays in {0}'.format(nSection))
        return new_array1
