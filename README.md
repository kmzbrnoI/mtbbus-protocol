MTBbus v4.1 Protocol Specification
==================================

MTBbus is RS485-based communication bus for controlling general-purpose IO
modules. It's original aim is to control model railroad accessories (e.g.
turnouts, signals etc.) however the bus is designed generally and extendably.

The bus consists of a single master module (MTB-USB module) and up to 255
IO modules. Master module is in charge of whole bus. Master module is usually
connected to the computer too, thus MTBbus is basically controlled from the
computer. Master module takes care of proper timing of RS485.

This document describes RS485-based protocol between master and slave modules.
Note that for connection of MTBbus to PC protocol between MTB-USB module and PC
must also be described. This protocol is available [here](pc).

1. [MTBbus goals](goals.md)
2. [MTBbus Architecture](architecture.md)
   - [Module Diagnostics](diag.md)
3. [Commands](commands.md)
   - [Module types](module-types.md)
   - [Commands summary](commands-summary.md)
4. [Workflows](workflows.md)
5. Module-specific commands
   - [MTB-UNI](modules/uni.md)
   - MTB-BOOST
   - MTB-RAILCOM
   - MTB-CROS

## Changelog

Available [here](changelog.md).

## Authors

 * [Jan Horacek](mailto:jan.horacek@kmz-brno.cz)

## License

Content of the repository is provided under [Creative Commons
Attribution-ShareAlike 4.0
License](https://creativecommons.org/licenses/by-sa/4.0/). You may download see
the protocol, use it in your own modules and contribute to it.
