from util import array, readinput


def execute(line, pointer, registers):
    '''
    hlf r sets register r to half its current value, then continues with the next instruction.
    tpl r sets register r to triple its current value, then continues with the next instruction.
    inc r increments register r, adding 1 to it, then continues with the next instruction.
    jmp offset is a jump; it continues with the instruction offset away relative to itself.
    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
    '''
    instr = line[0]
    if instr == 'hlf':
        registers[line[1]] /= 2
        pointer += 1
    elif instr == 'tpl':
        registers[line[1]] *= 3
        pointer += 1
    elif instr == 'inc':
        registers[line[1]] += 1
        pointer += 1
    elif instr == 'jmp':
        offset = line[1]
        pointer += registers[offset] if type(offset) == str else line[1]
    elif instr == 'jie':
        r, offset = line[1], line[2]
        pointer += 1 if registers[r] % 2 != 0 else offset
    elif instr == 'jio':
        r, offset = line[1], line[2]
        pointer += 1 if registers[r] != 1 else offset
    return pointer, registers


def run(instructions, registers, reg_wanted):
    pointer = 0
    while True:
        pointer, registers = execute(instructions[pointer], pointer, registers)
        if pointer < 0 or pointer >= len(instructions):
            return registers[reg_wanted]


def tests():
    example_instr = (('inc', 'a'), ('jio', 'a', 2), ('tpl', 'a'), ('inc', 'a'))
    example_registers = {'a': 0}
    assert run(example_instr, example_registers, 'a') == 2
    print('tests pass')


tests()

INSTRUCTIONS = array(readinput(23))
REGISTERS = {'a': 0, 'b': 0}
print(run(INSTRUCTIONS, REGISTERS, 'b'))
REGISTERS_2 = {'a': 1, 'b': 0}
print(run(INSTRUCTIONS, REGISTERS_2, 'b'))