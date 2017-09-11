from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        self.assertTrue(solution([38, 47, 39, 25, 42], [22, 19, 8, 23, 31],
                                 [14, 26, 11, 18, 5], 0.05
                                 )
                        )