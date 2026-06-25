MTB-LED Module
==============

This specification applies for module types listed below:

| Code   | Module type                                     |
|--------|-------------------------------------------------|
| `0x40` | MTB-LED                                         |

MTB-LED module contains 32 constant-current PWM outputs 0-20 mA
intended to drive LEDs. It contains no physical inputs. Logically,
module presents 32 inputs which indicate whether LED is connected
to the output or not.

## Configuration

Configuration consists of 36 bytes.

1. 4 bytes of safe outputs state little-endian:
   - byte 0: outputs 0-7,
   - byte 1: outputs 8-15,
   - byte 2: outputs 16-23,
   - byte 3: outputs 24-31.
2. 32 bytes of brightness.
   - One byte for each output.
   - Range: 0-255 for each output.
   - When value `0` is used, output is actually set to value `1`.

## Module-specific commands

Master → slave:

* *Set Configuration*: n.o. data bytes: 36. Whole configuration is sent.
* *Get Configuration*: n.o. data bytes: 0.
* *Get Input*: n.o. data bytes: 0.
* *Set Output*: n.o. data bytes: 4.
  - Full state of all outputs is always sent.
* *Firmware Write Flash*
  - Data byte 0: first byte flash address high.
  - Data byte 1: first byte flash address low.
  - Data byte 2–65: 64 bytes of memory data.

Slave → master:

* *Module Configuration*: n.o. data bytes: 36. Whole configuration is sent.
* *Input Changed*: n.o. data bytes: 4. Full state of inputs is sent.
   - byte 0: connected state of outputs 0-7,
   - byte 1: connected state of outputs 8-15,
   - byte 2: connected state of outputs 16-23,
   - byte 3: connected state of outputs 24-31.
* *Input State*: n.o. data bytes: 4. Full state of inputs is sent.
* *Output Set*: n.o. data bytes: 4. Same data bytes as in message *Set
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

Page size is 128 bytes. Thus, for single page write 2 *Firmware Write Flash* commands must be sent:

 1. `0x01 0x43 0xF1 0x00 0x00 [64 bytes of data]`
 2. `0x01 0x43 0xF1 0x00 0x40 [64 bytes of data]`

Upgrade is done page-based. Frames in page need to be received in-order.
Page is written when last frame of page is received. It is impossible to write
just part of the page. In case when part of the page is supposed to be written,
rest of the page must be padded.

## Diagnostic information

**TODO TEF**

Module reports [common warnings](../diag.md) only.
