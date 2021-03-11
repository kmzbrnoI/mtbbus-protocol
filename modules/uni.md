MTB-UNI Module
==============

MTB-UNI module is most used MTBbus modules. It contains 16 digital inputs and
16 digital outputs. Any output is capable of S-COM protocol transmission as
well as flickering.

## Outputs state

State of each output is encoded in 1 byte:

* `0b 1xxx xxxx`: S-COM code. `x`'s represent specific [S-COM
  code](https://www.mtb-model.com/elektro/s-com.htm) (0-127).
* `0b 0000 000x`: digital outputs.
   - `x=0` = open collector,
   - `x=1` = output grounded.
* `0b 0100 xxxx`: flicker output. `xxxx`:
   - 1: 1 Hz
   - 2: 2 Hz
   - 3: 3 Hz
   - 4: 4 Hz
   - 5: 5 Hz
   - 6: 10 Hz
   - 7: 33 tick/min
   - 8: 66 tick/min

## Configuration

Configuration consists of 24 bytes:

1. 16 bytes of safe outputs state (outputs indexed in order 0 to 15).
2. 8 bytes of input keep delay.
   - Byte 0: `0bBBBBAAAA`. `A` = delay of input 0, `B` = delay of input 1.
   - Byte 1: delay of input 2, delay of input 3.
   - ...
   Each input has 16 values of input delay. `0`=0.0s, `1`=0.1s, `2`=0.2s, ...,
   `15`=1.5s.

When input goes to logical 0, it must remain in this state for *input keep
delay* to consider the input as logical 0. Only after the time input changed
event is reported to master board.

## Module-specific commands

Master → slave:

* *Set Configuration*: n.o. data bytes: 24. Whole configuration is sent.
* *Get Configuration*: n.o. data bytes: 0.
* *Get Input*: n.o. data bytes: 0.
* *Set Output*: n.o. data bytes: variable.
  - State of all outputs is always sent.
  - Data byte 0: full state mask for outputs `0bFEDCBA98`.
  - Data byte 1: full state mask for outputs `0b76543210`.
  - Data byte 2: binary state of outputs `0bFEDCBA98`.
  - Data byte 3: binary state of outputs `0b76543210`.
  - Data byte 4–n: state of full-state outputs in order 0–F.
  - Examples (only data bytes are written):
    - Set output 1 as active, other as inactive: `0x00 0x00 0x00 0x02`.
    - Set output 8 to S-COM code `0x0A`, output 10 as flickering with period
      2 Hz, output 15 as active, other as inactive:
      `0x05 0x00 0xF0 0x00 0x42 0x8A`.
  - Bits in *binary state output* which are masked by *full state mask* can
    contain any value. This value is ignored.


Slave → master:

* *Module Configuration*: n.o. data bytes: 24. Whole configuration is sent.
* *Input Changed*: n.o. data bytes: 2. Full state of inputs is sent.
  - Data byte 0: inputs 0-7.
  - Data byte 1: inputs 8-15.
  - Order of inputs in byte: `0b76543210`.
* *Input State*: n.o. data bytes: 2. Full state of inputs is sent.
* *Output Set*: n.o. data bytes: variable. Same data bytes as in message *Set
  Output* is sent.