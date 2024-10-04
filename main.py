class Simpletron:
    def __init__(self):
        self.memory = [0] * 100  # Memory of 100 words
        self.accumulator = 0  # Accumulator register
        self.instruction_counter = 0  # Program counter
        self.instruction_register = 0  # Holds the current instruction
        self.operation_code = 0  # The operation part of the instruction
        self.operand = 0  # The address part of the instruction
        self.halted = False

    def load_program_from_file(self, filename):
        """
        Load a Simpletron program from a text file.
        :param filename: The path to the file containing the program.
        """
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file):
                    # Strip newlines and convert to integer
                    instruction = int(line.strip())
                    if i >= 100:
                        print("Error: Program exceeds memory size.")
                        break
                    self.memory[i] = instruction
            print("Program loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except ValueError:
            print("Error: Non-numeric instruction encountered in file.")

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

    def dump_memory(self):
        """
        Prints the current state of the Simpletron's memory, accumulator, and registers.
        """
        print("\nREGISTERS:")
        print(f"Accumulator: {self.accumulator}")
        print(f"Instruction Counter: {self.instruction_counter}")
        print(f"Instruction Register: {self.instruction_register}")
        print(f"Operation Code: {self.operation_code}")
        print(f"Operand: {self.operand}\n")

        print("MEMORY:")
        for i in range(0, 100, 10):
            memory_slice = " ".join(f"{self.memory[j]:+05}" for j in range(i, i + 10))
            print(f"{i:02}: {memory_slice}")

# Example of loading a program from a file and running it.
if __name__ == "__main__":
    simpletron = Simpletron()
    
    # Request file name from user
    filename = input("Enter the name of the program file to load: ")
    
    # Load the program from the file
    simpletron.load_program_from_file(filename)
    
    # Run the Simpletron program
    simpletron.run()
    
    # Dump memory after program execution
    simpletron.dump_memory()
