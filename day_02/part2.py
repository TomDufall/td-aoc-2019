from collections import namedtuple
from typing import List, Optional

from part1 import load_input, Parser

InputTuple = namedtuple("InputTuple", "noun, verb")


def find_inputs(program: List[str], target_value: str) -> Optional[InputTuple]:
    for noun in range(100):
        for verb in range(100):
            custom_program = program.copy()
            custom_program[1] = noun
            custom_program[2] = verb
            parser = Parser(custom_program)
            parser.execute()
            output = parser.program[0]
            if output == target:
                return InputTuple(noun, verb)
    return None


if __name__ == "__main__":
    program = load_input()
    target = "19690720"
    inputs = find_inputs(program, target)
    if inputs is None:
        print("No input found for target")
    else:
        print(100 * inputs.noun + inputs.verb)
