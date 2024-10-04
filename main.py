class Simpletron:
    def __init__(self):
        self.memory = [0] * 100  # Memory of 100 words
        self.accumulator = 0  # Accumulator register
        self.instruction_counter = 0  # Program counter
        self.instruction_register = 0  # Holds the current instruction
        self.operation_code = 0  # The operation part of the instruction
        self.operand = 0  # The address part of the instruction
        self.halted = False

    def load_program(self, program):
        """
        Load the program into the Simpletron's memory.
        :param program: List of integers representing SML instructions.
        """
        for i, instruction in enumerate(program):
            self.memory[i] = instruction

    def run(self):
        """
        Executes the Simpletron program.
        """
        while not self.halted:
            self.fetch_instruction()
            self.decode_and_execute()

    def fetch_instruction(self):
        """
        Fetch the instruction from memory based on the instruction counter.
        """
        self.instruction_register = self.memory[self.instruction_counter]
        self.operation_code = self.instruction_register // 100
        self.operand = self.instruction_register % 100
        self.instruction_counter += 1

    def decode_and_execute(self):
        """
        Decodes the instruction and executes it.
        """
        if self.operation_code == 10:  # READ
            self.memory[self.operand] = int(input(f"Enter an integer for memory location {self.operand}: "))
        elif self.operation_code == 11:  # WRITE
            print(f"Memory[{self.operand}] = {self.memory[self.operand]}")
        elif self.operation_code == 20:  # LOAD
            self.accumulator = self.memory[self.operand]
        elif self.operation_code == 21:  # STORE
            self.memory[self.operand] = self.accumulator
        elif self.operation_code == 30:  # ADD
            self.accumulator += self.memory[self.operand]
        elif self.operation_code == 31:  # SUBTRACT
            self.accumulator -= self.memory[self.operand]
        elif self.operation_code == 32:  # DIVIDE
            if self.memory[self.operand] == 0:
                print("Error: Division by zero.")
                self.halted = True
            else:
                self.accumulator //= self.memory[self.operand]
        elif self.operation_code == 33:  # MULTIPLY
            self.accumulator *= self.memory[self.operand]
        elif self.operation_code == 40:  # BRANCH
            self.instruction_counter = self.operand
        elif self.operation_code == 41:  # BRANCHNEG
            if self.accumulator < 0:
                self.instruction_counter = self.operand
        elif self.operation_code == 42:  # BRANCHZERO
            if self.accumulator == 0:
                self.instruction_counter = self.operand
        elif self.operation_code == 43:  # HALT
            print("Simpletron execution halted.")
            self.halted = True
        else:
            print(f"Unknown operation code: {self.operation_code}")
            self.halted = True

# Example of loading a program into the Simpletron.
if __name__ == "__main__":
    program = [
        1007,  # READ into memory location 07
        1008,  # READ into memory location 08
        2007,  # LOAD memory location 07 into accumulator
        3008,  # ADD memory location 08 to accumulator
        2109,  # STORE result into memory location 09
        1109,  # WRITE memory location 09
        4300   # HALT
    ]

    simpletron = Simpletron()
    simpletron.load_program(program)
    simpletron.run()
    simpletron.dump_memory()
