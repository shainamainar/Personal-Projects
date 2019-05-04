#given a list of nums and a num k
# return whether any 2 nums add up to k

def sum(nums, k):
    b = False
    for i in range(len(nums) - 1):
        for j in range(len(nums)):
            if(i != j):
                print(nums[i] + nums[j])
                if (int(nums[i] + nums[j])) == k:
                    return True
                else:
                    b = False
        
    return b
    
def main():
    arr = [10, 15, 3, 7]
    k = 17
    print(sum(arr, k))

main()
