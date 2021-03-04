MTBbus v4.0 Protocol Specification
==================================

---

**Content of this repository is under construction.**

---

MTBbus is RS485-based communication bus for controlling general-purpose IO
modules. It's original aim is to control model railroad accessories (e.g.
turnouts, signals etc.) however the bus is designed generally and extendably.

The bus consists of a single master module (MTB-USB module) and up to 255
IO modules. The bus is controlled from single device, usually a computer with
appropriate control software.

 1. [MTBbus Architecture](architecture.md)
 2. [Commands](commands.md)
    - [Module types](module-types.md)
    - [Commands overview](commands-overview.md)
 3. [Workflows](workflows.md)
 4. [Module-specific commands](module-commands.md)
