class CoursePlan:
    def __init__(self):
        self.graph = {}

    def add_course(self, course):
        self.graph[course] = []

    def add_requisite(self, course1, course2):
        self.graph[course1].append(course2)

    def visit(self, course):
        if self.state[course] == 1:
            self.cycle = True
            return
        if self.state[course] == 2:
            return
        
        self.state[course] = 1
        for next_course in self.graph[course]:
            self.visit(next_course)

        self.state[course] = 2
        self.order.append(course)

    def find_order(self):
        self.state = {}
        for course in self.graph:
            self.state[course] = 0

        self.order = []
        self.cycle = False

        for course in self.graph:
            if self.state[course] == 0:
                self.visit(course)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order

if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None