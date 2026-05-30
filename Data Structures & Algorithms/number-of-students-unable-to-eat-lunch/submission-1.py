class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_prefs = {0:0, 1:0}
        for student in students:
            student_prefs[student] += 1
        for sando in sandwiches:
            if student_prefs[sando] == 0:
                return student_prefs[0] + student_prefs[1]
            else:
                student_prefs[sando] -= 1
        return 0
            