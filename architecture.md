MTBbus Architecture
===================

## Basic Bus Parameters

* Hardware layer: RS485, 2-wire communication (+ common ground).
* Communication speed: variable. 38400 Bd, 57600 Bd, 115200 Bd.
* Data bytes: 9.
* Stop bytes: 1.
* Parity: None.
* Max bus length: 100 m.

## Bus Structure

* Master-slave.
* Bus should meet all RS485 requirements, straight bus topology is advised.
* Bus should be terminated on all ends via *terminator*.
  - 560 Ohm resistors advised for pull-down & pull-up.
  - 200 Ohm resistor advised between bus wires.

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
   bit = 1. This byte is present only in direction master → slave.
2. **Header byte** contains number of data bytes following. This number
   excludes address byte, header byte, command type byte and xor byte.
3. **Command code byte**.
4. **Data bytes**. Up to 255 data bytes.
5. **xor** todo::CRC16?

Note that when slave module sends data to master, packet starts with *Header
Byte*. All bytes in packet from slave modules have 9. bit = 0.
