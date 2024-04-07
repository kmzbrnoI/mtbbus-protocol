Module diagnostics
==================

Each module may perform self-diagnostics and report state of the diagnostics to
the computer. Each module type can define up to 256 *Diagnostic Values* (**DV**).
Diagnostic value is usually a fixed-length sequence of bytes with defined
meaning, e.g. 2 bytes for current MCU power supply voltage.

There are some common DVs:

`0`: diagnostic values specification version
 * Length: 1 byte
 * Value: `0xJN`
   - `J` = DV major version
   - `N` = DV minor version
   - Current version: *1.0* (`0x10`)

`1`: module state
 * Length: 1 byte
 * Value: `0b000000we`
   - `w` = any warning present
   - `e` = any error present

`2`: uptime
 * Length: 4 bytes
 * Unit: seconds

`3–9`: *not used*

`10`: errors
 * Length: any
 * Value: each bit represents one module error type
 * Errors are specific for module types

`11`: warnings
 * Length: any
 * Value: each bit represents one warning type
 * First byte: *Common warnings vector*
 * Next bytes: specific for module types

`12`: CPU voltage
 * Length: specific for module type
 * Representation: specific for module type

`13`: CPU temperature
 * Length: specific for module type
 * Representation: specific for module type

`16`: MTBbus number of successfully received messages
 * Length: 4 bytes

`17`: MTBbus number of received messages with invalid CRC
 * Length: 4 bytes

`18`: MTBbus number of sent messages
 * Length: 4 bytes

`19–31`: *not used*

`32-255`: module-specific diagnostic values

## Common warnings vector

Common warnings vector contain only one byte: `0b00om0wbe`.

* `e`: Reset due to external signal.
* `b`: Reset due to brown-out.
* `w`: Reset due to watchdog overflow.
* `m`: Timer miss occurred.
* `o`: MCU VCC is oscillating.

## Notes

* If module is asked to return state of *unused* DV, it returns empty DV (length=0).
* Module must store all diagnostics to be ready to return value of any DV immediately.
* DVs are read-only from the point of view of PC.
* Only changes of *DV #1* are reported as events to the PC. All other DVs should
  be polled.
