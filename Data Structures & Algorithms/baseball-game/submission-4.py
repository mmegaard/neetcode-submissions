class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum_all = 0
        for operation in operations:
            if operation == "C":
                sum_all -= stack.pop()
            elif operation == '+':
                sum_scores = stack[- 1] + stack[- 2]
                stack.append(sum_scores)
                sum_all += sum_scores
            elif operation == 'D':
                double_score = stack[- 1] * 2
                stack.append(double_score)
                sum_all += double_score
            else:
                score = int(operation)
                stack.append(score)
                sum_all += score
                
        return sum_all
        