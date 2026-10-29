
# ----- FUNCTION -----
# Simple addition 
def summ(a , b): 
    return a + b


# Main function bubble sorting 
def sorting(array : list):
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
    return array
