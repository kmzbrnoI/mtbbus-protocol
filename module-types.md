MTBbus module types
===================

MTBbus module type is determined by its 1-byte *code*.

| Code   | Module type                                     |
|--------|-------------------------------------------------|
| `0x10` | MTB-UNI v2 with ATmega328p                      |
| `0x15` | MTB-UNI v4.0 with ATmega128 (without blue LED)  |
| `0x16` | MTB-UNI v4.2 with ATmega128 (with blue LED)     |
| `0x20` | MTB-BOOST                                       |
| `0x30` | MTB-RAILCOM                                     |
| `0x40` | MTB-CROS                                        |

Note: this table must contain entry for each hardware revision of single module
type if this revision affects uploaded firmware. Module type must fully qualify
firmware to choose for upgrade.
