# MTBbus Changelog

## v4.1

* Add module diagnostics.
* Module reports bootloader version.

## v4.0

Changes from [version 2.0](https://mtb.kmz-brno.cz/assets/pdf/mtb-protok20.pdf)
(available in czech only).

* Complete reimplementation of old protocol.
  - Hardware layer kept same (RS485).
  - Bus protocol designed from scratch – completely new.

### New features

* Do not hardcode module types in general protocol. Use 2-level abstraction:
  define general commands and their specialization for slave modules. This allows
  to smoothly add new module types in future.
* Bus detects new modules while maintaining normal operation.
* No scanning procedure nor starting & stopping of the bus is required. Bus
  runs always, always checks for module failures and always scans for new
  modules.  - Slave modules are hot-swappable.
* Firmware of slave modules could be upgraded directly over MTBbus.
* Each module has special LED which could be turned on/off from operator's
  computer. This allows operator to find module under the layout fast (*beacon
  function*).
* Bus is prepared for new MTB-RAILCOM, MTB-CROS, MTB-SPAX modules.
  - Bus allows to poll inputs instead of calling events when input changes.

### New features of modules

* Modules are expected to store their configuration in permanent memory.
* Safe state of outputs is set directly after slave module start (e.g. correct
  signal on railway signals is set etc.).
* All outputs of MTB-UNI module can be S-COM.
* Added more flickering frequencies of outputs of MTB-UNI.
* Dropped support for MTB-REG & MTB-POT modules.

### What does NOT change

* Hardware layer (compatibility with old wiring assured).
* Authoritative source of configuration of slave modules is computer.
* Bus can have multiple speeds.
