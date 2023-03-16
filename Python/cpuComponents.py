# 이것도 왜 만들라 한 것인지는 모르겠지만 index를 어떻게 사용해야 할지 알게 되었다.

print("Components of a CPU")

cpuComponents = [
  "CU", "ALU", "Accumulator", "PC", "Memory Address Register",
  "Memory Data Register", "Current Instruction Register", "Cache",
  "Address Bus", "Data Bus", "Control Bus", "Interrupt Register"
]
cpuDefinitions = [
  "•	Coordinates all CPU activities\n•	Directs flow of data between the CPU and other devices\n•	Coordinates and communicates with all parts of the CPU",
  "•	Arithmetic operations on fixed and floating-point numbers",
  "•	One of several general-purpose registers in modern CPUs\n•	Often stores data or control information\n•	The results of calculation",
  "•	Hold the address of the next instruction to be executed\n•	It could be the next instruction in a sequence of instructions or the address to jump ",
  "•	Holds the address of the memory location that data or an instruction is to be fetched from or written to memory",
  "•	Used to temporarily store data that is read from or written to memory",
  "•	Holds the current instruction being executed\n•	If the MDR is holding an instruction, it is copied to the current instruction register",
  "•	A small are of memory, often located on or near the CPU, that provides fast access to frequently used instructions and data\n•	Physically close to the CPU than RAM and faster to access but has a smaller capacity",
  "•	Carries memory addresses that identify where data is being read from or written to memory",
  "•	Carries the binary 1s and 0s that make up the actual information being transmitted around the CPU/Computer",
  "•	Carries command and control signals to and from every other component of the CPU/Computer",
  '•	Checked by the CPU to see if an interrupt is waiting to be processed'
]

asdf = input("Enter a component name: ")
whatcomponent = cpuComponents.index(asdf)
print(f"Definition of {asdf}:\n" + cpuDefinitions[whatcomponent])