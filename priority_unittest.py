import unittest
from priority_my_heapq_manager import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
        self.tasks = [
            ("Refactorizar código base", 3),
            ("Implementar nueva característica A", 5),
            ("Corregir error crítico B", 9),
            ("Actualizar documentación", 2),
            ("Revisar y aprobar PRs", 4)
        ]

    def test_insertion_order(self):
        for task, priority in self.tasks:
            self.pq.push(task, priority)
        
        expected_order = [
            "Corregir error crítico B",
            "Implementar nueva característica A",
            "Revisar y aprobar PRs",
            "Refactorizar código base",
            "Actualizar documentación"
        ]
        
        results = []
        while self.pq.queue:
            results.append(self.pq.pop())

        self.assertEqual(results, expected_order)

    def test_empty_pop(self):
        with self.assertRaises(IndexError):
            self.pq.pop()
if __name__ == '__main__':
    unittest.main(verbosity=2)