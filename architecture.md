MTBbus Architecture
===================

## Basic Bus Parameters

* Hardware layer: RS485, 2-wire communication (+ common ground).
* Communication speed: variable. 38400 Bd, 57600 Bd, 115200 Bd.
* Data bytes: 9.
* Stop bytes: 1.
* Parity: None.
* Max bus length: 100 m.
* Max modules: 254.

## Hardware Structure

* Single master, multiple slaves.
* Bus should meet all RS485 requirements, straight bus topology is advised.
* Bus should be terminated on all ends via *terminator*.
  - 560 Ohm resistors are advised for pull-down & pull-up.
  - 200 Ohm resistor is advised between bus wires.

## Packets

Data are sent in packets. MTBbus is single-master bus bus. This implies any
slave device is allowed to send data only when it is provided transmission
window via [Module Inquiry Command](commands.md#mosi-module-inquiery) by master
module. Master module periodically scans all slave addresses and ask them
whether the have any data to send. Slave module must always respond to this
request, even if it has no data to send. This mechanism ensures master module
can detect faulty or disconnected modules, which is critical for ensuring
safety.

Master module holds list of addresses of active modules and requests these
modules periodically in short interval. It also requests all other addresses
to detect new modules in longer intervals. This mechanism allows present modules
to communicate fast and to detect new modules too.

## Timing

Each slave module must start answering to any request addresses to the module
after ≤ 110 microseconds. After 120 microseconds master module is allowed to
consider addressed module as non-communicating.

## Packet structure

Packet consists of variable numbers of bytes.

1. **Address byte** contains slave 8-bit address. Only this byte has ninth
   bit = 1. This byte is present only in direction master → slave. Each slave
   module should receive data addressed only for the module and broadcast data.
   Broadcast commands have address = 0. Thus module address 0 is forbidden.
2. **Message length byte** contains number of data bytes following. This number
   excludes address byte, header byte, command type byte and checksum bytes.
3. **Command code byte**.
4. **Data bytes**. Up to 120 data bytes (128 bytes buffer).
5. **Checksum** CRC-16 (2 bytes).

Note that when slave module sends data to master, packet starts with *Header
Byte*. All bytes in packet from slave modules have 9. bit = 0.

### CRC-16

* Polynomial: x¹⁶ + x¹⁵ + x² + 1 (*CRC-16-ANSI* also known as *CRC-16-IBM*,
  normal hexadecimal algebraic polynomial being `0x8005` and reversed `0xA001`).
* Initial value: `65536`, `0xFFFF`.
* CRC-bytes: least significant byte is transmitted first.
* Checksum includes whole packet: starting from *address byte* to last byte of
  *data bytes*.
* Example of packet: TODO.

## Modules addressing

Each MTBbus slave module has its address in range 1-255. Address could be
determined by hardware switches/jumpers on module or just programmed in
volatile memory. MTBbus supports mechanism for readdressing modules from master
module/PC.

## Errors

If slave module receives bad checksum, it must not respond.
