class Solution:
    def minMaxDifference(self, num: int) -> int:
        number = [int(x) for x in str(num)]
        maxNumber = number.copy()
        minNumber = number.copy()
        maxReplaceDigit = minReplaceDigit = None

        for i in range(len(number)):
            digit = number[i]
            if maxReplaceDigit is None and digit < 9:
                maxReplaceDigit = digit
                # print(maxReplaceDigit)

            if minReplaceDigit is None and digit > 0:
                minReplaceDigit = digit
                # print(minReplaceDigit)

            if maxReplaceDigit is not None and digit == maxReplaceDigit:
                maxNumber[i] = 9
                # print(maxNumber)

            if minReplaceDigit is not None and digit == minReplaceDigit:
                minNumber[i] = 0

        # print(maxNumber, minNumber)

        maxNum = int(''.join([str(n) for n in maxNumber]))
        minNum = int(''.join([str(n) for n in minNumber]))

        return maxNum - minNum
