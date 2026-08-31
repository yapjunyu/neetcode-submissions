class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # formula: (target - position) / speed 
        # if this number is smaller, it will catch up to it
        # once it catches up the speed of that car does not matter anymore
        stack = []
        arr = list(zip(position, speed))
        arr.sort()
        for i in range(len(arr)):
            num = (target - arr[i][0]) / arr[i][1]
            while stack and num >= stack[-1]:
                stack.pop()
            stack.append(num)
        return len(stack)