MTBbus goals
============

The aim of the bus is to control model railway accessories (turnouts etc.) as
well as fetch signals from model railway (occupancy detectors, turnouts
positions etc.).

## High-level goals

* MTBbus should be simple (it should rely on existing hardware archtecture).
* Development of MTBbus as well as MTBbus modules should be open, so anyone can
  use the bus.
* Bus does NOT have to be compatible with commercial model railroad buses.
  - If someone wants to connected MTBbus with commercial model railroad control
    software, he/she should write alternative firmware for MTB-USB module, which
    implements commercial protocol on the PC side.

## Middle-level goals

* Bus should be designed extendably to allow **new module types in future**.
  - There are general command templates and their specialization for specific
    module types.
* Modules on bus should be scanned automatically.
* Modules on bus should be **hot-swappable**. Master module should detect
  missing modules as well as discover new modules.
* Each module has configuration.
  - Configuration is saved to permanent memory.
  - This is especially needed for safe-outputs state and bus speed.
* **Authoritative source of configuration is computer**. Computer can ask for
  module's configuration and/or replace it with anything it wants.
* Bus should be easily extendable to wireless (via retranslation unit).
* When master module starts, it should start scanning bus. No bus off/bus on
  states exist. Bus is always active.
* MTB-USB module should be thin: it should only resend packets between MTBbus
  and PC. It should not do heavy work.

## Low-level goals

* Operator can turn on/off beacon (flashing LED on module) on any module from
  PC.
* Module can report inputs changes as event or changes could be only polled.
  This allows digital inputs as well as analog inputs on the bus.
* Number of inputs / outputs of slave modules is not part of general protocol.
  It is defined for each module type specifically.
* Configuration is slave modules is not part of general protocol. Is is defined
  for each module type specifically.
* Firmware of slave modules could be upgraded directly over MTBbus.
