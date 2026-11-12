#prefix[i]= prefix[i-1]+num[i]
# num =     [ 2 4 1 3]
# prefix =  [ 2 6 7 10]

#prefixsum vs slidingwindow


def withArray():
    arr = [2, 4, 1, 5, 3]
    prefix = [0] * len(arr) # create temp array of size num
    prefix[0] = arr[0] # first element

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i] 

    print(prefix) #[2, 6, 7, 12, 15]
    

def withList():
    arr = [2, 4, 1, 5, 3]
    prefix = [0]

    for num in arr:
        prefix.append(prefix[-1] + num)

    print(prefix) #[2, 6, 7, 12, 15]