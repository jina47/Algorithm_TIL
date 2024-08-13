from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def daq(x):
            if x.isdigit():
                return [int(x)]
            
            result = []
            for idx in range(len(x)):
                if not x[idx].isdigit():
                    left = daq(x[:idx])
                    right = daq(x[idx+1:])

                    for l in left:
                        for r in right:
                            if x[idx] =='+':
                                result.append(l+r)
                            elif x[idx] == '-':
                                result.append(l-r)
                            else:
                                result.append(l*r)
            return result

        return daq(expression)


# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:
#         def compute(left, right, op):
#             results = []
#             for l in left:
#                 for r in right:
#                     results.append(eval(str(l) + op + str(r)))
#             return results
        

#         if expression.isdigit():
#             return [int(expression)]
        
#         results = []
#         for index, value in enumerate(expression):
#             if value in "+-*":
#                 left = self.diffWaysToCompute(expression[:index])
#                 right = self.diffWaysToCompute(expression[index+1:])

#                 results.extend(compute(left, right, value))
        
#         return results