def minimizeMaximumDifferenceHeights(ar, k):
    ar.sort()
    diff = ar[-1] - ar[0]
    mn, mx = ar[0] + k, ar[-1] - k
    for i in range(len(ar)):
        sb, ad = ar[i] - k, ar[i] + k
        if mn <= sb or mx >= ad: continue
        if mx - sb <= ad - mn: mn = sb
        else: mx = ad
    return min(diff, mx - mn)

def main():
    k = int(input())
    ar = [int(x) for x in input().split()]
    print(minimizeMaximumDifferenceHeights(ar, k))

if __name__ == "__main__":
    main()
