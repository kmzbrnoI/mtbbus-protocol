MTBbus commands
===============

## Master → Slave

### `0x01` Module Inquiry <a name="mosi-module-inquiry"></a>

* This commands instructs module to respond with any information it has to
  send.
* Command type: for specific module only.
* Command Code byte: `0x01`.
* Standard abbreviation: `MODULE_INQUIRY`.
* N.o. data bytes: 1.
* Data byte 0: `0b000000CO`
   - `O`: 1 iff master received data from slave module after last
     *Module Inquiry*. If slave module sent data in response to previous
     module inquiry and the `O` bit of next *Module Inquiry* is 0, slave module
     must assume previous data were not delivered. It is advised to resend
     previous data.
   - `C`: 1 iff master module wants to be notified about input changes.
     If this bit is 0, slave module should always respond only with
     [`ACK`](#miso-ack). In this case, modules are polled for their input
     status.
* Possible responses:
   - [*ACK*](#miso-ack) if module has no data to send.
   - [*Input Changed*](#miso-input-changed) if module wants to report input
     changed event.

### `0x02` Module Info Request <a name="mosi-info"></a>

* This commands instructs slave module to send information about the module.
* Command type: for specific module only.
* Command Code byte: `0x02`.
* Standard abbreviation: `MODULE_INFO_REQ`.
* N.o. data bytes: 0.
* Response: [*Module information*](#miso-module-info)

### `0x03` Set Configuration <a name="mosi-set-config"></a>

* Packet type: for specific module only.
* This command instructs slave module to permanently set it's configuration.
  - The configuration should persist even if module turns off.
  - However, in typical application master module will configure all modules
    when modules are discovered.
  - Authoritative source of configuration is PC.
* Command Code byte: `0x03`.
* Standard abbreviation: `SET_CONFIG`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
* Response: [*ACK*](#miso-ack).

### `0x04` Get Configuration <a name="mosi-get-config"></a>

* This command instructs slave module to send its current configuration to
  master board.
* Command type: for specific module only.
* Command Code byte: `0x03`.
* Standard abbreviation: `GET_CONFIG`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
* Response: [*Configuration*](#miso-config).

### `0x05` Beacon <a name="mosi-beacon"></a>

* Turn module beacon on/off.
  - Each slave module should have special blue LED installed for beacon purpose.
  - Operator at computer can turn on/off beacon on any module to locate the
    module physically on the bus.
  - Blue LED should be flashing in interval *300 ms on, 200 ms off* while
    beacon is on.
* Command type: for specific module or broadcast.
* Command Code byte: `0x05`.
* Standard abbreviation: `BEACON`.
* N.o. data bytes: 1.
* Data byte 0: `0x0000000B`
  - `B`: 1 iff beacon should be on.
* Response: [*ACK*](#miso-ack).
  - In case command is sent as broadcast, no response should be sent.

### `0x10` Get Input <a name="mosi-get-input"></a>

* In response to this command slave module should immediately send state of its
  inputs.
* Command type: for specific module only.
* Command Code byte: `0x10`.
* Standard abbreviation: `GET_INPUT`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
  - E.g. some modules can be instructed to send full inputs state, some modules
    may be requested for specific input state etc.
* Response: [*Input State*](#miso-input-state).

### `0x11` Set Output <a name="mosi-set-output"></a>

* Set output of slave module.
* Command type: for specific module only.
* Command Code byte: `0x11`.
* Standard abbreviation: `SET_OUTPUT`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
  - E.g. master module could send state of all outputs in this packet for some
    modules or just specific output/s.
* Response: [*ACK*](#miso-ack).

### `0x12` Reset Outputs <a name="mosi-reset-outputs"></a>

* Reset all outputs of slave module to default state.
* Command type: for specific module or broadcast.
* Command Code byte: `0x12`.
* Standard abbreviation: `RESET_OUTPUTS`.
* N.o. data bytes: 0.
* Response: [*ACK*](#miso-ack).

### `0x20` Change Address <a name="mosi-change-address"></a>

 * `CHANGE_ADDRESS` – změň adresu na zadanou; lze i jako broadcast a pak
   se změní jen u modulů se zmáčknutým tlačítkem
    - Odpověď: `ACK`

### `0xE0` Speed Changed <a name="mosi-speed-changed"></a>

 * [GENERAL] `SPEED_CHANGED`

### `0xF0` Reprogramming <a name="mosi-reprog"></a>

 * `REPROG` – restartuj se a připrav se na nahrání nového FW
    - Odpověď: již speciální odpověď protokolu pro nahrávání firmwaru


## Slave → Master

### `0x01` Acknowledgement <a name="miso-ack"></a>

### `0x02` Module information <a name="miso-module-info"></a>

 * `INFO` `INFODATA`
 * 1 byte: typ modulu
 * 1 byte: verze FW modulu (MAJ MAJ MAJ MAJ MIN MIN MIN MIN)

### `0x03` Output Set <a name="miso-output-set"></a>

 * `OUT_SET` – výstup nastaven, pošle aktuální stav výstupů

### `0x04` Input Changed <a name="miso-input-changed"></a>

 * `INPUT_CHANGED` – následující data jsou specifická pro konkrétní moduly
    (obsahuje např. stav všech vstupů)

### `0x05` Input State <a name="miso-input-state"></a>

 * `INPUT` – obsahuje stav vstupů
    - pozor: má být záměrně různé od `INPUT_CHANGED`, využito např. pro ADC

### `0x06` Configuration <a name="miso-config"></a>

 * `CONFIG` – pošle konfiguraci, odpověď na `GET_CONFIG`
