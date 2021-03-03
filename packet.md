Packet structure
================

Packet consists of variable numbers of bytes.

1. **Address byte** contains slave 8-bit address. Only this byte has ninth
   bit = 1.
2. **Header byte** contains number of data bytes following. This number
   excludes address byte, header byte, command type byte and xor byte.
3. **Command code byte**.
4. **Data bytes**. Up to 255 data bytes.
5. **xor** todo::CRC16?
