class Solution:
    def check_nabour(self, num):
        flag = True
        count = 1

        while flag:
            if (num + 1) not in num_set:
                flag = False
            else:
                count += 1
                num += 1

        return count

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        global num_set
        num_set = set(nums)
        result = 0

        for num in nums:
            if (num - 1) not in num_set:
                count = self.check_nabour(num)

                if count > result:
                    result = count

        return result


##################################
#  with count and consecutive subsequence list
##################################
class Solution:
    def check_nabour(self, no):
        flag = True
        res = [no]
        count = 1

        while flag:
            if (no + 1) not in num_set:
                flag = False
            else:
                res.append(no + 1)
                count += 1
                no += 1

        return count, res

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        global num_set
        result = [0, 0]
        num_set = set(nums)

        for num in nums:
            if (num - 1) not in num_set:
                count, lst = self.check_nabour(num)

                if count > result[0]:
                    result[0] = count
                    result[1] = lst

        return len(result[1])
