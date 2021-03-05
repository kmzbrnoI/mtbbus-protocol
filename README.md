MTBbus v4.0 Protocol Specification
==================================

---

**Content of this repository is under construction.**

---

MTBbus is RS485-based communication bus for controlling general-purpose IO
modules. It's original aim is to control model railroad accessories (e.g.
turnouts, signals etc.) however the bus is designed generally and extendably.

The bus consists of a single master module (MTB-USB module) and up to 254
IO modules. Master modules is in charge of whole bus. Master module is usually
connected to the computer too, thus MTBbus is basically controlled from the
computer. Master module takes care of proper timing of RS485.

This protocol describes protocol over RS485 MTBbus between master and slave
modules. Note that for connection of MTBbus to PC protocol between MTB-USB
module and PC must also be described. This protocol is described in another
document.

 1. [MTBbus goals](goals.md)
 2. [MTBbus Architecture](architecture.md)
 3. [Commands](commands.md)
    - [Module types](module-types.md)
    - [Commands overview](commands-overview.md)
 4. [Workflows](workflows.md)
 5. Module-specific commands
    - [MTB-UNI](modules/uni.md)
    - MTB-BOOST
    - MTB-RAILCOM
    - MTB-CROS
