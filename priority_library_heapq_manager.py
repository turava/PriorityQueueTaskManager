import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def add_task(self, task, priority):
        heapq.heappush(self.heap, (-priority, self.count, task))
        self.count += 1

    def remove_task(self):
        if self.heap:
            return heapq.heappop(self.heap)[-1]
        raise KeyError("The priority queue is empty")

def main():
    # Creating the priority queue
    task_queue = PriorityQueue()

    # Adding tasks with given priorities
    tasks = [
        ("Refactorizar código base", 3),
        ("Implementar nueva característica A", 5),
        ("Corregir error crítico B", 3),
        ("Actualizar documentación", 2),
        ("Revisar y aprobar PRs", 4)
    ]

    for task, priority in tasks:
        task_queue.add_task(task, priority)

    # Fetching tasks in priority order
    print("Tasks will be executed in the following order:")
    while True:
        try:
            print(task_queue.remove_task())
        except KeyError:
            break

if __name__ == "__main__":
    main()
