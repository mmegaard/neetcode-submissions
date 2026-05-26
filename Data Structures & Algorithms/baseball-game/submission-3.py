class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum_all = 0
        for i,operation in enumerate(operations):
            if operation == "C":
                last_score = stack.pop()
                sum_all -= last_score
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
        