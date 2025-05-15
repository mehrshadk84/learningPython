# giving back the cpu complexity
def binarySearch(low,max,x,count):
    if low>max:
        return -1
    count += 1
    mid = (low + max)/2 
    mid = int(mid)
    if x == mid:
        return count
    elif x < mid:
        return binarySearch(low,mid -1,x,count)
    elif x > mid:
        return binarySearch(mid +1,max,x,count)
maxsize = int(input("enter the maxsize: "))
inputarrayy = int(input("give me the x: "))
print(binarySearch(0,maxsize,inputarrayy,0))