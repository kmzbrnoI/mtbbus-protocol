MTB-RC Module
==============

This specification applies for module types listed below:

| Code   | Module type                                     |
|--------|-------------------------------------------------|
| `0x30` | MTB-RC                                          |


MTB-RailCom module consists of 8 separate RailCom detectors. RailCom allows to
read address of a mobile decoder present on the track as well as decoder's CVs.

## Inputs

For the purpose of this specification, DCC mobile decoder address is always
a 13-bit number (0–16383, allowed values: xxxx TODO).

Inputs-state is a message composed of following 2-byte chunks. Each chunk contains
one address of a present DCC decoder. Number of chunks depends on the number of
read addresses on the tracks. MTB-RC supports reading of multiple decoder
addresses in a single track circuit.

`0bDDDAAAAA AAAAAAAA` - A
* `D` – detector id (0–7)
* `A` – 13bit DCC address

Chunks are always sorted according to *detector id* in ascending order.

## Outputs

No outputs.

## Configuration

No configuration.

## Module-specific commands

Master → slave:

* *Set Configuration*: n.o. data bytes: 0.
* *Get Configuration*: n.o. data bytes: 0.
* *Get Input*: n.o. data bytes: 0.
* *Set Output*: n.o. data bytes: 0.
* *Firmware Write Flash*
  - TODO

Slave → master:

* *Module Configuration*: n.o. data bytes: 0.
* *Input Changed*: n.o. data bytes: variable. Full state of inputs is sent.
* *Input State*: n.o. data bytes: variable. Full state of inputs is sent.
* *Output Set*: n.o. data bytes: 0.

### Firmware upgrade

TODO

## Diagnostic information

Module reports no errors.

Module reports [common warnings](../diag.md) only.
