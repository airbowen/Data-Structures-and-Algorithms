# 求一个数组中的第k大的数字（或第k小的数字）是一个常见的算法问题
# 可以使用多种方法来解决。下面介绍几种常见的解法：

# simple solution 
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出：5


# heap solution
import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出：5


# heapq.nlargest 内部已经实现了堆化过程。
# 为了更清晰地展示堆化过程，可以使用 heapq 模块的 heapify 函数，
# 并手动进行堆化和维护堆。以下是完整的代码示例，
# 展示了如何使用最小堆来找到第k大的元素。

import heapq

def findKthLargest(nums, k):
    # 创建一个最小堆
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # 堆化过程
    
    # 遍历剩余的元素
    for num in nums[k:]:
        if num > min_heap[0]:  # 如果当前元素大于堆顶元素
            heapq.heappop(min_heap)  # 弹出堆顶元素
            heapq.heappush(min_heap, num)  # 插入当前元素
    
    return min_heap[0]  # 返回堆顶元素，即第k大的元素

# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出：5

#选择适合的算法取决于具体的需求和数据规模。
# 堆排序的期望时间复杂度为O(n log n)，适用于一般情况。

# 堆排序的空间复杂度为O(n)，
# 快速选择的空间复杂度为O(1)。

import random

def partition(nums, left, right):
    pivot_index = random.randint(left, right)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] > pivot:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index

def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]
    pivot_index = partition(nums, left, right)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)

def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, k - 1)

# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出：5
