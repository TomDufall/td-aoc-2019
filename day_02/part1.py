from typing import List


def load_input() -> List[str]:
    with open("input.txt") as file:
        text = file.read()
    program = text.split(",")
    return program


class Parser:
    def __init__(self, program):
        self.program = program
        self.pointer = 0

    def step(self):
        instr = self.program[self.pointer]
        if instr == "99":
            return
        elif instr == "1":
            # Add
            index1, index2, index3 = [
                int(index)
                for index in self.program[int(self.pointer) + 1 : int(self.pointer) + 4]
            ]
            self.program[index3] = str(
                int(self.program[index1]) + int(self.program[index2])
            )
            self.pointer += 4
        elif instr == "2":
            # Multiply
            index1, index2, index3 = [
                int(index)
                for index in self.program[int(self.pointer) + 1 : int(self.pointer) + 4]
            ]
            self.program[index3] = str(
                int(self.program[index1]) * int(self.program[index2])
            )
            self.pointer += 4
        else:
            raise ValueError("Unrecognised instruction")

    def execute(self):
        while self.program[self.pointer] != "99":
            self.step()


if __name__ == "__main__":
    program = load_input()
    program[1] = "12"
    program[2] = "2"
    parser = Parser(program)
    parser.execute()
    print(parser.program[0])
