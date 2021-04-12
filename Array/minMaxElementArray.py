'''
Max and min element in an array
- input array 
- set element at index 0 as min and max
- loop if ele>max if ele<min
- max(list) and min(list)
- Time complexity: O(n)
'''

def elementMaxMin(ar): 
    mn = mx = ar[0]
    for ele in ar:
        if ele > mx: mx = ele
        if ele < mn: mn = ele
    return mx, mn 

def main():
    ar = [int(x) for x in input().split()]
    mx, mn = elementMaxMin(ar)
    print(mx, mn)
    #inbuilt function max(list) and min(list)
    mx_, mn_ = max(ar), min(ar)
    print(mx_, mn_)
    
if __name__ == "__main__":
    main()
