'''Reverse an array 
- input array 
- start and end 
- swap the front and last element 
- reversed(list) and list.reverse()
- Time Complexity: O(n)
'''

def reverseArray(arr):
    front, back = 0, len(arr) - 1
    while front<back:
        arr[front], arr[back] = arr[back], arr[front]
        front += 1
        back -= 1
    return arr 

def main():
    arr = [int(x) for x in input().split()]
    reverseArr = reverseArray(arr)
    print(reverseArr)
    #inbuilt function list.reverse() -> reverse the list
    arr.reverse()
    print(arr)
    #inbuilt function reversed(list) -> reversed iterator of the list
    reversedArr = list(reversed(arr))
    print(reversedArr)
     
if __name__ == "__main__":
    main()
    