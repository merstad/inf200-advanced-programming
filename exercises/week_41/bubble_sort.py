"""
Week 41, Task 3.
Bubble sort.
"""

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def bubble_sort(in_data):
    """
    Return sorted copy of in_data.
    """

    # Create a copy of the data. Will will sort this copy.
    s_data = list(in_data)

    # 1. Let N == len(s_data) be the number of elements in the data.
    # 2. At the beginning of each round through the outer loop, we
    #    have already sorted data in s_data[j+1:N-1] and the inner loop
    #    will put the largest element in s_data[0:j] into s_data[j].
    # 3. Since range(len(s_data)) runs from 0..N-1 and we use reversed(...),
    #    we start with j==N-1. Then 2. says that we will put the largest
    #    element in s_data[0:N-1], i.e., in all of s_data, into s_data[N-1],
    #    its correct location.
    # 4. We execute the loop a last time for j==0 and then count down to j==-1
    #    and stop the loop. 2. now tells us that we have sorted data in
    #    s_data[0:N-1], i.e., that all data is sorted.
    # See INF221 for more on this type of analysis.
    for j in reversed(range(len(s_data))):

        # In the inner loop, we run through the elements s_data[0:j-1]
        # and swap neighboring elements if they are not in the right order.
        # At the beginning of every round through the loop, s_data[k] is
        # the largest element in s_data[0:k].
        for k in range(j):
            if s_data[k+1] < s_data[k]:
                s_data[k], s_data[k+1] = s_data[k+1], s_data[k]

    return s_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
