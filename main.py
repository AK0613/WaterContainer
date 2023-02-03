#Calculate the area of the biggest container
#Use 7 since that's how high up the water can go and also the 9 (Max area)
#[7, 1, 2, 3, 9 ]
#[0, 1, 2, 3, 4] indices
#So 7 x 4 = 28

#Empty or with only one value should return 0

#[6, 9, 3, 4, 5, 8]
#Either 6 and 8 -> 6 x 5 = 30
# or 9 and 8 -> 8 x 4 = 32 <<<---- Correct answer

#Area equals the smallest value of (a,b) x (b_index - a_index)

def get_max(nums):
    max_area = a = 0
    size = b = len(nums)-1
    print(a, b, max_area)
    if size > 2:
        while(a < b):
            print(a, b)
            length = min(nums[a], nums[b])
            width = b - a
            area = length * width
            print(length, width, area)
            max_area = max(area, max_area)
            print(max_area)
            if nums[a] <= nums[b]:
                a +=1
            else:
                b -= 1
        return max_area
    else:
        max_area = 0
    return max_area

nums = [4,8,1,2,3,9]
max= get_max(nums)
print(f'The max area is: {max}')




#Solution one
#
# def get_max(nums):
#     size = len(nums)
#     max_area = 0
#     if size > 2:
#         for a in range(size):
#             for b in range(a + 1, size):
#                 length = min(nums[a], nums[b])
#                 width = b-a
#                 area = length * width
#                 if area > max_area:
#                     max_area = area
#     else:
#         max_area = 0
#     return max_area
