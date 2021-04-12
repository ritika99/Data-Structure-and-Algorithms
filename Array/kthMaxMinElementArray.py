'''
"Kth" max and min element of an array
- input k and array
- sort array 
- max = arr[end - k] and min = arr[k - 1]
- Time Complexity: O(n)
> Can also try Binary Search Tree(BST)
'''

def kElementMaxMin(ar, k):
    ar.sort()
    k_mx = ar[len(ar) - k]
    k_mn = ar[k-1]
    return k_mx, k_mn

def main():
    k = int(input())
    ar = [int(x) for x in input().split()]
    k_mx, k_mn = kElementMaxMin(ar, k)
    print(k_mx, k_mn)
        
if __name__ == "__main__":
     main()
