'''
Sort array of 0, 1, 2 
0 0 0 1 1 2 2
'''

def sortArr(arr):
    i = z = 0
    t = len(arr) - 1
    while i<=t:
        if arr[i]==1:
            i+=1
        if arr[i]==0:
            arr[i], arr[z] = arr[z], arr[i]
            z+=1
            i+=1
        if arr[i]==2:
            arr[i], arr[t] = arr[t], arr[i]
            t-=1
    return arr

def main():
    ar = [int(x) for x in input().split()]
    sortArr(ar)
    print(ar)
    
if __name__ == "__main__":
    main()