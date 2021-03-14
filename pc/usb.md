MTB-USB to PC Protocol
======================

This document describes MTB-USB module communication with PC. MTB-USB module
is designed as thin module: it periodically scans MTBbus and forwards packets
between USB and MTBbus. Communication with PC takes place over USB CDC serial
port.

## Packet structure

Packet consists of variable numbers of bytes. Packet structure is same in
both directions.

1. **Magic byte** `0x2A`.
2. **Magic byte** `0x42`.
3. **Command length byte** contains number of data bytes following.
4. **Command code byte**.
5. **Data bytes**. Up to 122 data bytes (128 bytes buffer).

Message does not contain any checksum as checksum is handled by USB bus
natively.

## PC → MTB-USB <a name="pctomtb"></a>

### `0x10` Forward packet to MTBbus <a name="pm-forward"></a>

* Forward any packet to MTBbus.
  - The most used command.
* Command Code byte: `0x10`.
* Standard abbreviation: `MTBUSB_PM_FORWARD`.
* N.o. data bytes: any.
  - Data byte 0: MTBbus slave device address (`0` for broadcast).
  - Data byte 1: MTBbus MTBbus *Command Code Byte*.
  - Data byte 2–n: MTBbus *Data bytes*.
* Checksum for MTBbus packet as well as *Command length byte* is calculated in
  MTB-USB automatically.
* Response:
  - When slave device address is nonzero, MTB-USB does not send any direct
    response to this packet. However, response from slave module in forwarded to
    PC via [*Packet from MTBbus command*](#mp-forward).
  - When slave device address is `0` (broadcast), MTB-USB responds with
    [*ACK*](#mp-ack).
* PC should not send these MTBbus packets:
  - *Module inquiry*. Module inquiries are handled by MTB-USB automatically.

### `0x20` MTB-USB Information Request <a name="pm-info"></a>

* Send general info about MTB-USB module.
* Command Code byte: `0x20`.
* Standard abbreviation: `MTBUSB_PM_INFO_REQ`.
* N.o. data bytes: 0.
* Response: [*MTB-USB Information*](#mp-info).

### `0x21` Change Speed <a name="pm-change-speed"></a>

* Change speed of RS485 interface if MTB-USB module.
  - **Speed of slave modules is not changed!**
  - To change speed of whole bus, PC software must first change speed of
    modules (forward broadcast, recommended to send 3 times) and then change
    speed of MTB-USB module.
* Command Code byte: `0x21`.
* Standard abbreviation: `MTBUSB_PM_CHANGE_SPEED`.
* N.o. data bytes: 1.
* Data byte 0:
  - `0x01` = 38400 Bd
  - `0x02` = 57600 Bd
  - `0x03` = 115200 Bd
* Response: [*ACK*](#mp-ack).

### `0x22` Active modules request <a name="pm-actives-modules-req"></a>

* This command asks MTB-USB to send list of currently active modules on MTBbus.
* Command Code byte: `0x22`.
* Standard abbreviation: `MTBUSB_PM_ACTIVE_MODULES_REQ`.
* N.o. data bytes: 0.
* Response: [*Active modules list*](#mp-active-modules-list).


## MTB-USB → PC <a name="mtbtopc"></a>

### `0x01` Acknowledgement <a name="mp-ack"></a>

* Tell PC that MTB-USB module processed the command correctly.
* Command Code byte: `0x01`.
* Standard abbreviation: `MTBUSB_MP_ACK`.
* N.o. data bytes: 0.
* In response to:
  - [*Forward packet to MTBbus – broacast*](#pm-forward)
  - [*Change Speed*](#pm-change-speed)

### `0x02` Error <a name="mp-error"></a>

* Tell PC that error occurred while processing command for MTB-USB module.
* Command Code byte: `0x02`.
* Standard abbreviation: `MTBUSB_MP_ERROR`.
* N.o. data bytes: 0.
* In response to: nothing yet.

### `0x10` Packet from MTBbus <a name="mp-forward"></a>

* This command is sent when any slave device sends data to MTB-USB module.
  - MTB-USB periodically scans MTBbus.
* Command Code byte: `0x10`.
* Standard abbreviation: `MTBUSB_MP_FORWARD`.
* N.o. data bytes: any.
  - Data byte 0: MTBbus slave device address.
  - Data byte 1: MTBbus MTBbus *Command Code Byte*.
  - Data byte 2–n: MTBbus *Data bytes*.
* Checksum of MTBbus packet is omitted (USB calculates checksums automatically).
* In response to: nothing, could be sent anytime.

### `0x20` MTB-USB Information <a name="mp-info"></a>

* Report general information about MTB-USB.
* Command Code byte: `0x20`.
* Standard abbreviation: `MTBUSB_MP_INFO`.
* N.o. data bytes: TODO.
* In response to: [*MTB-USB Information Request*](#pm-info).

#### Module information packet bytes

 0. Module type
    - `0x01` MTB-USB module designed by Jan Horacek
 1. Module flags TODO
 2. Firmware version major
 3. Firmware version minor
 4. Supported protocol version major
 5. Supported protocol version minor

### `0x22` Active modules list <a name="mp-active-modules-list"></a>

* Send list of active modules to PC.
* Command Code byte: `0x22`.
* Standard abbreviation: `MTBUSB_MP_ACTIVE_MODULES_LIST`.
* N.o. data bytes: 32.
  - Data byte 0: `0b76543210`. Bit `0` says that module `0` is present of not etc.
  - Data byte 1: `0bFEDCBA98`: modules 8–15.
  - ...
  - Data byte 31: modules 248–255.
* In response to: [*Active modules request*](#pn-active-moduoles-req).
