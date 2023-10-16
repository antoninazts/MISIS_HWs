class MyStack:
    def __init__(self):
        self.my_stack = list()

    def __str__(self):
        return str(", ".join(self.my_stack))

    def push(self, item):
        self.my_stack.append(item)

    def pop(self):
        if len(self.my_stack) == 0:
            return None
        removed = self.my_stack.pop()
        return removed


class TaskManager:
    def __init__(self):
        self.task = {}

    def __str__(self):
        string = ""
        for elem in sorted(self.task.keys()):
            string += str(elem) + " " + str(self.task[elem]) + ";\n"
        return string

    def new_task(self, task, priority):
        if not priority in self.task.keys():
            self.task[priority] = MyStack()
            self.task[priority].push(task)
        else:
            new_stack = MyStack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.push(value)
            new_stack.push(task)
            self.task[priority] = new_stack

    def delete_task(self, priority):
        if not priority in self.task.keys():
            print("Задача с таким приоритетом отсутствует!")
        else:
            print(f"Задача '{self.task[priority].pop()}' удалена")
            if len(str(self.task[priority])) == 0:
                self.task.pop(priority)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.new_task("сделать уборку", 4)
manager.delete_task(4)
manager.delete_task(1)
print(manager)
