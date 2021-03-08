# About

This software simulates the breadboard computer made
by Ben Eater. You can write programs for it
using Ben Eaters assembly language or
directly write binary code.
It was made by Luis Michaelis. You are allowed
to edit this program and redistribute it as
it is free and open source software.

## Setup & Usage

For this program to run you will need
Python 3.6 which you can download for all
platforms from [https://www.python.org/](python.org).

To start open a terminal or command-line window
in the folder of the program. Type in:

``` shell
    python[3] cpu.py test.prg.bin
```

For linux users the command is python3
This will launch the included test program
which counts up until it reaches 256, then
it counts down until it reaches 0 and does
this in a loop. To see the assembly code just
open the test.prg in your favourite text
editor. This code needs to be compiled before
it can be used. To compile the code type in
a terminal:

``` shell
    python[3] compiler.py test.prg
```

This will compile the assembly code stored in
test.prg into the compiled file test.prg.bin.
You can open this file with a text editor too
and see the compiled binary code.

To summarize:
You can compile your program using:

``` shell
    python[3] compile.py [yourfilename]
```

You can run the program by typing:

``` shell
    python[3] cpu.py [youfilename].bin
```

For more information about the programs
type:
    python[3] [program].py -h

## Writing Code

You can write your code either in Ben Eater's
assembly language or directly write binary code.
For convenience, here the table of assembly
code, binary representation and description:

|Assembly | Binary    | Description                                                   | Argument
|--------|-----------|---------------------------------------------------------------|----------------------------
|NOP      | 0000 xxxx | Do nothing (No Operation)                                     | Not Required (set to 0)
|LDA      | 0001 xxxx | Load value from RAM into the A register (Load A)              | Required (memory location)
|ADD      | 0010 xxxx | Add a value from RAM to the value in the A register and put the result back into the A register (Add) | Required (memory location)
|SUB      | 0011 xxxx | Subtract a value from RAM from the value in the A register and put the result back into the A register (Subtract) | Required (memory location)
|STA      | 0100 xxxx | Store the value in the A register into RAM (Store A)          | Required (memory location)
|LDI      | 0101 xxxx | Load a immediately using the argument (Load immediately)      | Required (number to load)
|JMP      | 0110 xxxx | Jump to a specified 'line' in code (!Lines start at 0) (Jump) | Required (line number)
|JPC      | 0111 xxxx | Jump to a specified 'line' in code (!Lines start at 0) if the result of the previous operation was less than 0 or more than 255 (Jump Carry) | Required (line number)
|JPZ      | 1000 xxxx | Jump to a specified 'line' in code (!Lines start at 0) if the result of the previous operation was equal to 0 (Jump if Zero) | Required (line number)
|OUT      | 1110 xxxx | Write the value in the A register to the CLI (Output)         | Not Required (set to 0)
|HLT      | 1111 xxxx | Halt the system (Halt)                                        | Not Required (set to 0)

## Rules

- Line starts either with instruction or memory
  address and colon:

Assembly:

```asm
ADD 15
15: 5
```

Binary:

```text
0010 1111
1111: 00000101
```

Line with memory address specifies variable address:variable
Line without specifies instruction

- Except variables (255/0b11111111), all given numbers may not be
  larger than 15/0b1111

- Hashes (#) introduce comments

- PLEASE NOTE THAT MEMORY LOCATIONS WILL OVERWRITE IF
  THEY ARE SET MULTIPLE TIMES. This also applies for
  instructions: Every instruction gets automatically
  a space in memory, starting at 0000 and incrementing
  by one for every detected instruction:

Assembly

```asm
LDA 15  # Memory address 0
OUT 0   # Memory address 1 (and so on ...)

15: 6   # Memory address 15
```

Binary

```text
0001 1111 # Memory address 0
1110 0000 # Memory address 1 (and so on ...)

1111: 00000110 # Memory address 15
```

The simulation program (cpu.py) can only run compiled
binary code which could either be written by yourself
or be result of the compiler. The compiler (compiler.py)
only compiles assembly files.
