class Calculation:
    def __init__(self,operation,items):
        self.operation = operation
        self.items = items
        self.result = 0

    def do_calculation(self):
        if self.operation == 'addition':
            return self.addition(self.items)
        if self.operation == 'subtraction':
            return self.subtraction(self.items)
        if self.operation == 'multiplication':
            return self.multiplication(self.items)
        if self.operation == 'division':
            return self.division(self.items)

    def addition(self, items):
        for item in range(len(items)):
            self.result += items[item]
        return str(self.result)
    def subtraction(self, items):
        for item in range(len(items)):
            self.result -= items[item]
        return str(self.result)

    def multiplication(self, items):
        for item in range(len(items)):
            self.result *= items[item]
        return str(self.result)

    def division(self, items):
        for item in range(len(items)):
            self.result /= items[item]
        return str(self.result)