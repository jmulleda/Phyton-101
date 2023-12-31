import unittest

def merge_sort(L, verbose=False):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    """

    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
        
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0

    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]
        

class TestMergeSort(unittest.TestCase):
    """Tests MergeSort Function"""
    # your code here
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)