class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_q = deque(students)
        sando_s = deque(sandwiches)
        length = len(students)
        cycled = 0
        while sando_s and student_q and cycled < length:
            student = student_q.popleft()
            if student != sando_s[0]:
                student_q.append(student)
                cycled += 1
            else:
                sando_s.popleft()
                length -=1
                cycled = 0
        return length
        