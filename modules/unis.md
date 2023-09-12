MTB-UNIS Module
==============

This specification applies for module types listed below:

| Code   | Module type                                     |
|--------|-------------------------------------------------|
| `0x50` | MTB-UNIS with ATmega128 and 6 servo outputs     |

MTB-UNIS module is like MTB-UNI modules. It contains 16 digital inputs and
16 digital outputs. But have extra 6 servo outputs. Any of 16 digital output is capable of S-COM protocol
transmission as well as flickering. Servo is controlled via aditional 12 virtual outputs.
Thus module have 16 iput signals and 28 output signals.

## Outputs state

State of each output is encoded in 1 byte:

* `0b 1xxx xxxx`: S-COM code. `x`'s represent specific [S-COM
  code](https://www.mtb-model.com/elektro/s-com.htm) (0-127).
* `0b 0000 000x`: digital outputs + servo outputs.
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

Configuration consists of 55 bytes.

1. 28 bytes of safe outputs state (outputs indexed in order 27 to 0).
2. 8 bytes of input keep delay.
   - Byte 0: `0bBBBBAAAA`. `A` = delay of input 0, `B` = delay of input 1.
   - Byte 1: delay of input 2, delay of input 3.
   - ...
   Each input has 16 values of input delay. `0`=0.0s, `1`=0.1s, `2`=0.2s, ...,
   `15`=1.5s.
3. 1 byte mask, which servo outputs are active
   - `0b00654321`, 1 = output active, 0 = output disabled
4. 12 bytes for servo positions
   - 1 byte value for servo 1 position 1
   - 1 byte value for servo 1 position 2
   - 1 byte value for servo 2 position 1
   - ...
   Valid range is 0 - 255.
   Value 0 means servo pulse 399 us.
   Value 255 means servo pulse 2613 us.
   Value 127 means servo pulse 1502 us - center position.
   Recomanded limits for pulse duration is 500 - 2500 us.
5. 6 bytes for servo speed
   - speed for servo 1
   - speed for servo 2
   - ...
   Speed 1 is slowest (1.56 positions/second). Speed 255 is fastest (797 positions/second).
   
When input goes to logical 0, it must remain in this state for *input keep
delay* to consider the input as logical 0. Only after the time input changed
event is reported to master board.

## Module-specific commands

Master → slave:

* *Set Configuration*: n.o. data bytes: 67. Whole configuration is sent.
* *Get Configuration*: n.o. data bytes: 0.
* *Get Input*: n.o. data bytes: 0.
* *Set Output*: n.o. data bytes: variable.
  - State of all outputs is always sent.
  - Data byte 0: full state mask for outputs `0bFEDCBA98`.
  - Data byte 1: full state mask for outputs `0b76543210`.
  - Data byte 2: binary state of outputs `0 0 0 0 s6p s6l s5p s5l`.
  - Data byte 3: binary state of outputs `s4p s4l s3p s3l s2p s2l s1p s1l`.
  - Data byte 4: binary state of outputs `0bFEDCBA98`.
  - Data byte 5: binary state of outputs `0b76543210`.
  - Data byte 6–n: state of full-state outputs in order 0–F.
  - Examples (only data bytes are written):
    - Set output 1 as active, other as inactive: `0x00 0x00 0x00 0x00 0x00 0x02`.
    - Set output 8 to S-COM code `0x0A`, output 10 as flickering with period
      2 Hz, output 15 as active, other as inactive:
      `0x05 0x00 0x00 0x00 0x80 0x00 0x42 0x8A`.
    - Set output 4,s1l,s2l active other inactive
      `0x00 0x00 0x00 0x05 0x00 0x10`.
  - Bits in *binary state output* which are masked by *full state mask* can
    contain any value. This value is ignored.
* *Firmware Write Flash*
  - Data byte 0: first byte flash address high.
  - Data byte 1: first byte flash address low.
  - Data byte 2–65: 64 bytes of memory data.
* *Module-specific command*
  - Data byte 0 = `0x01` = set servo position.
    - Data byte 1 = position identification `0b0000nnnp` where p = position, n = servo number
    - Data byte 2 = new position for servo (0-255)
    (p = position  - 0=1st position, 1=2nd position, n = servo number - possible values 1-6)
  - Data byte 0 = `0x02` = set servo speed.
    - Data byte 1 = position identification `0b0000nnnp` where p = position, n = servo number
    - Data byte 2: new speed for servo (valid range 1-255).
    (p = position  - 0=1st position, 1=2nd position, n = servo number - possible values 1-6)
  - Data byte 0 = `0x03` = manual servo positioning (changes will not be saved to eeprom).
    - Data byte 1 = position identification `0b0000nnnx` where n = servo number (1-6), x = ignored
    - Data byte 2: new position for servo (0-255).
    servo move to new position using speed from settings, ignore state of virtual outputs for servo
    after inactivity period (2 minutes), servo move to its original position - defined in eeprom and virtual outputs state
  - Data byte 0 = `0x03`.
    - Data byte 1 = 0 - end of manual position setting, all servos restore normal operation
  
  Manual servo positioning is for testing. No changes will be saved to internal eeprom.
  Control application can save eeprom values via standard command *Set Configuration*  

Slave → master:

* *Module Configuration*: n.o. data bytes: 67. Whole configuration is sent.
* *Input Changed*: n.o. data bytes: 2. Full state of inputs is sent.
  - Data byte 0: inputs `0bFEDCBA98`.
  - Data byte 1: inputs `0b76543210`.
* *Input State*: n.o. data bytes: 2. Full state of inputs is sent.
* *Output Set*: n.o. data bytes: variable. Same data bytes as in message *Set
  Output* is sent.

### Firmware upgrade

Data is sent in frames of 64 bytes.

* *Firmware Write Flash*
  - Data byte 0: page address.
  - Data byte 1: offset in page.
  - Data byte 2–65: memory data.

* *Firmware Write Flash Status*
  - Data byte 1: page address.
  - Data byte 2: offset in page.

Page size is 256 bytes.
Thus, for single page write 4 *Firmware Write Flash* commands must be
sent:

 1. `0x01 0x43 0xF1 0x00 0x00 [64 bytes of data] [checksum]`
 2. `0x01 0x43 0xF1 0x00 0x40 [64 bytes of data] [checksum]`
 3. `0x01 0x43 0xF1 0x00 0x80 [64 bytes of data] [checksum]`
 4. `0x01 0x43 0xF1 0x00 0xC0 [64 bytes of data] [checksum]`

Upgrade is done page-based. Frames in page need to be received in-order.
Page is written when last frame of page is received. It is impossible to write
just part of the page. In case when part of the page is supposed to be written,
rest of the page must be padded.

## Diagnostic information

Module reports no errors.

Module reports [common warnings](../diag.md) and some additional information:

`14`: servo voltage - output of power voltage regulator
 * Length: 2 bytes
 * Representation: left justified value from internal ADC
