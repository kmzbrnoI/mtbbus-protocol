MTB-USB to PC Protocol
======================

Communication with PC takes place over USB CDC serial port. This allows to use
native drivers in computer. Because communication takes place in 8bits and USB
splits data in 64-byte frames, own synchronization and own concept of *message*
in required.

## Packet structure

Packet consists of variable numbers of bytes. Packet structure is same in
both directions.

1. **Magic byte** `0x2A`.
2. **Magic byte** `0x42`.
3. **Command length byte** contains number of data bytes following (excluding
   this packet).
4. **Command code byte**.
5. **Data bytes**. Up to 122 data bytes (128 bytes buffer).

Message does not contain any checksum as checksum is handled by USB bus
natively.
