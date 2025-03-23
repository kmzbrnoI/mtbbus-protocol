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
a 13-bit number (0–16383).

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
  - Not yet supported

Slave → master:

* *Module Configuration*: n.o. data bytes: 0.
* *Input Changed*: n.o. data bytes: variable. Full state of inputs is sent.
* *Input State*: n.o. data bytes: variable. Full state of inputs is sent.
* *Output Set*: n.o. data bytes: 0.

### Firmware upgrade

Not yet supported.

## Diagnostic information

Module reports no errors.

Module reports [common warnings](../diag.md) only.

### Module-specific diagnostic values

#### Railcom low-level

`32`: Cutouts started
 * Length: 4 bytes

`33`: Cutouts finished
 * Length: 4 bytes

`34`: Cutout timeouts
 * Length: 4 bytes

`35`: Cutouts with data in channel 1
 * Length: 4 bytes

`36`: Cutouts with data in channel 2
 * Length: 4 bytes

`37`: Cutouts without ready\_to\_parse
 * Length: 4 bytes


#### Railcom middleware

`40`: RailCom channel 1 control-sum invalid reads
 * Length: 4 bytes

`41`: RailCom channel 2 control-sum invalid reads
 * Length: 4 bytes

`42`: addr1\_received\_count resets
 * Length: 4 bytes

`43`: addr2\_received\_count resets
 * Length: 4 bytes

`44`: `APP_ID_ADR_LOW` received
 * Length: 4 bytes

`45`: `APP_ID_ADR_HIGH` received
 * Length: 4 bytes

`46`: ch1 address added/refreshed
 * Length: 4 bytes

`47`: ch2 address added/refreshed
 * Length: 4 bytes


`t` = track [0-7]

`50+10*t`: RailCom channel 1 control-sum invalid reads in track `t`
 * Length: 4 bytes

`51+10*t`: RailCom channel 2 control-sum invalid reads in track `t`
 * Length: 4 bytes

`52+10*t`: addr1\_received\_count resets in track `t`
 * Length: 4 bytes

`53+10*t`: addr2\_received\_count resets in track `t`
 * Length: 4 bytes

`54+10*t`: `APP_ID_ADR_LOW` received in track `t`
 * Length: 4 bytes

`55+10*t`: `APP_ID_ADR_HIGH` received in track `t`
 * Length: 4 bytes

`56+10*t`: ch1 address added/refreshed in track `t`
 * Length: 4 bytes

`57+10*t`: ch2 address added/refreshed in track `t`
 * Length: 4 bytes

#### DCC

`130`: DCC received packets
 * Length: 4 bytes

`131`: DCC received bad xor
 * Length: 4 bytes

`132`: logical 0 after <10 preamble bits
 * Length: 4 bytes

`133`: number of mobile decoders read addresses
 * Length: 4 bytes
