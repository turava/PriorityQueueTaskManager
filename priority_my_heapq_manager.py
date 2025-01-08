class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        # Find the right position to insert the task to keep the queue ordered by priority
        if not self.queue:
            self.queue.append((priority, item))
        else:
            for i in range(len(self.queue)):
                if priority > self.queue[i][0]:
                    self.queue.insert(i, (priority, item))
                    break
            else:
                # If the task has the lowest priority, append it at the end
                self.queue.append((priority, item))

    def pop(self):
        # Remove and return the highest priority task
        if self.queue:
            return self.queue.pop(0)[1]
        raise IndexError("pop from an empty priority queue")

def main():
    pq = PriorityQueue()
    pq.push("Refactorizar código base", 3)
    pq.push("Implementar nueva característica A", 5)
    pq.push("Corregir error crítico B", 9)
    pq.push("Actualizar documentación", 2)
    pq.push("Revisar y aprobar PRs", 4)

    print("Tasks will be executed in the following order:")
    while pq.queue:
        print(pq.pop())

if __name__ == '__main__':
    main()
