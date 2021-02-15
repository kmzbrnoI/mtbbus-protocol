Basic Bus Parameters
====================

* Hardware layer: RS485, 2-wire communication (+ common ground).
* Communication speed: variable. 38400 Bd, 57600 Bd, 115200 Bd.
* Data bytes: 9.
* Stop bytes: 1.
* Parity: None.
* Max bus length: 100 m.

Bus Structure
-------------

* Master-slave.
* Bus should meet all RS485 requiremets, straight bus topoloy is advised.
* Bus should be terminated on all ends via *terminator*.
  - 560 Ohm resistors advised for pull-down & pull-up.
  - 200 Ohm resistor advised between bus wires.
