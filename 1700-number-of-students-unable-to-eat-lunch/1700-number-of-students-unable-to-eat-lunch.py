class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
         # Count how many want 0 and 1
        need0 = students.count(0)
        need1 = len(students) - need0  # or students.count(1)

        # Serve sandwiches from top to bottom
        for s in sandwiches:
            if s == 0:
                if need0 == 0:
                    return need1  # stuck
                need0 -= 1
            else:  # s == 1
                if need1 == 0:
                    return need0  # stuck
                need1 -= 1

        # Everyone ate
        return 0
        