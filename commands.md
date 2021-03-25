MTBbus commands
===============

## Master → Slave <a name="mosi"></a>

### `0x01` Module Inquiry <a name="mosi-module-inquiry"></a>

* This commands instructs module to respond with any information it has to
  send.
* Command type: for specific module only.
* Command Code byte: `0x01`.
* Standard abbreviation: `MOSI_MODULE_INQUIRY`.
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
* Response: [*ACK*](#miso-ack) or [*Input Changed*](#miso-input-changed).
   - [*ACK*](#miso-ack) if module has no data to send.
   - [*Input Changed*](#miso-input-changed) if module wants to report input
     changed event.

### `0x02` Module Information Request <a name="mosi-info"></a>

* This commands instructs slave module to send information about the module.
* Command type: for specific module only.
* Command Code byte: `0x02`.
* Standard abbreviation: `MOSI_MODULE_INFO_REQ`.
* N.o. data bytes: 0.
* Response: [*Module information*](#miso-module-info)

### `0x03` Set Configuration <a name="mosi-set-config"></a>

* Command type: for specific module only.
* This command instructs slave module to permanently set it's configuration.
  - The configuration should persist even if module turns off.
  - However, in typical application master module will configure all modules
    when modules are discovered.
  - Authoritative source of configuration is PC.
* Command Code byte: `0x03`.
* Standard abbreviation: `MOSI_SET_CONFIG`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
* Response: [*ACK*](#miso-ack).

### `0x04` Get Configuration <a name="mosi-get-config"></a>

* This command instructs slave module to send its current configuration to
  master board.
* Command type: for specific module only.
* Command Code byte: `0x04`.
* Standard abbreviation: `MOSI_GET_CONFIG`.
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
* Standard abbreviation: `MOSI_BEACON`.
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
* Standard abbreviation: `MOSI_GET_INPUT`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
  - E.g. some modules can be instructed to send full inputs state, some modules
    may be requested for specific input state etc.
* Response: [*Input State*](#miso-input-state).

### `0x11` Set Output <a name="mosi-set-output"></a>

* Set output of slave module.
* Command type: for specific module only.
* Command Code byte: `0x11`.
* Standard abbreviation: `MOSI_SET_OUTPUT`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
  - E.g. master module could send state of all outputs in this packet for some
    modules or just specific output/s.
* Response: [*Output Set*](#miso-output-set).

### `0x12` Reset Outputs <a name="mosi-reset-outputs"></a>

* Reset all outputs of slave module to default state.
* Command type: for specific module or broadcast.
* Command Code byte: `0x12`.
* Standard abbreviation: `MOSI_RESET_OUTPUTS`.
* N.o. data bytes: 0.
* Response: [*ACK*](#miso-ack).
  - When command is sent as broadcast, no response should be sent.

### `0x20` Change Address <a name="mosi-change-address"></a>

* Change module address.
  - This feature is implemented only by modules, which address is not determined
    by hadrware.
  - When module does not support this feature, it should respond
    [*Error*](#miso-error) *Unsupported command*.
* Command type: for specific module or broadcast.
  - When this command is sent as broadcast, only modules which were activated
    by on-board button press should change address.
* Command Code byte: `0x20`.
* N.o. data bytes: 1.
* Standard abbreviation: `MOSI_CHANGE_ADDR`.
* Data byte 0: new module address.
* Response: [*ACK*](#miso-ack) or [*Error*](#miso-error) *Unsupported command*.
  - When command is sent as broadcast, no response should be sent.

### `0xE0` Change Speed <a name="mosi-speed-changed"></a>

* Bus speed change announcement.
  - When this command is received, slave module must immediately change bus
    speed to bus speed specified in the command. Module must store new speed
    in it's permanent memory and use it from now on even after reset or cutoff.
  - This packet is usually sent multiple times by master module to assure all
    modules really change their speed.
* Command type: broadcast only.
* Command Code byte: `0xE0`.
* N.o. data bytes: 1.
* Data byte 0:
  - `0x01` = 38400 Bd
  - `0x02` = 57600 Bd
  - `0x03` = 115200 Bd
* Standard abbreviation: `MOSI_CHANGE_SPEED`.
* Response: no response.

### `0xF0` Firmware Upgrade Request <a name="mosi-reprog"></a>

* This command instructs slave module to restart into bootloader and wait
  for firmware upgrade.
* Command type: for specific module only.
* Command Code byte: `0xF0`.
* N.o. data bytes: 1.
  - Data byte 0: upgrade type:
    - `0x00` for main firmware upgrade.
* Standard abbreviation: `MOSI_FWUPGD_REQUEST`.
* Response: [*ACK*](#miso-ack).
  - Response should be sent immediately (before reboot to bootloader)!

### `0xF1` Firmware Write Flash <a name="mosi-write-flash"></a>

* This command contains part of new firmware to write to slave's device flash.
* Command type: for specific module only.
* Command Code byte: `0xF1`.
* N.o. data bytes: *any*.
* Data bytes are specific for specific module types.
  - Typical content: address & 64 bytes of data.
* Standard abbreviation: `MOSI_WRITE_FLASH`.
* Response: [*ACK*](#miso-ack) or [*Error*](#miso-error) *Bad Address*.

### `0xF2` Firmware Write Flash Status Request <a name="mosi-write-flash-status-req"></a>

* This command contains part of new firmware to write to slave's device flash.
* Command type: for specific module only.
  - Advised behavior: send 64 bytes of flash memory & memory address.
* Command Code byte: `0xF2`.
* N.o. data bytes: 0.
* Standard abbreviation: `MOSI_WRITE_FLASH_STATUS_REQ`.
* Response: [*Firmware Write Flash Status*](#miso-write-flash-status).

### `0xFF` Reboot <a name="mosi-reboot"></a>

* This command instructs slave module to reboot.
* Command type: for specific module only or broadcast.
* Command Code byte: `0xFF`.
* N.o. data bytes: 0.
* Standard abbreviation: `MOSI_REBOOT`.
* Response: [*ACK*](#miso-ack).
  - When command is sent as broadcast, no response should be sent.

## Slave → Master <a name="miso"></a>

### `0x01` Acknowledgement <a name="miso-ack"></a>

* Tell master module that slave module has no other data to send.
* Command Code byte: `0x01`.
* Standard abbreviation: `MISO_ACK`.
* N.o. data bytes: 0.
* In response to:
  - [*Module Inquiry*](#mosi-module-inquiry)
  - [*Set Configuration*](#mosi-set-config)
  - [*Beacon*](#mosi-beacon)
  - [*Reset Outputs*](#mosi-reset-outputs)
  - [*Change Address*](#mosi-change-address)

### `0x02` Error <a name="miso-error"></a>

* Tell master module that error occured.
* Command Code byte: `0x02`.
* Standard abbreviation: `MISO_ERROR`.
* N.o. data bytes: 1.
* Data byte 0 = error code:
  - `0x01` = unknown command (`ERR_UNKNOWN_COMMAND`).
  - `0x02` = unsupported command (`ERR_UNSUPPORTED_COMMAND`).
  - `0x03` = bad address (`ERR_BAD_ADDRESS`).

### `0x03` Module information <a name="miso-module-info"></a>

* Report information about module.
* Command Code byte: `0x03`.
* Standard abbreviation: `MISO_MODULE_INFO`.
* N.o. data bytes: 6.
* In response to: [*Module Information Request*](#mosi-info)

#### Module information packet bytes

 0. [Module type](module-types.md)
 1. Module flags
    - bit 0: module is intentionally in bootloader ready for firmware upgrade
    - bit 1: module is unintentionally in bootloader, memory checksum failed
 2. Firmware version major
 3. Firmware version minor
 4. Supported protocol version major
 5. Supported protocol version minor

### `0x04` Module Configuration <a name="miso-config"></a>

* Report module current configuration.
  - Content of the packet is specific for specific module types.
* Command Code byte: `0x04`.
* Standard abbreviation: `MISO_MODULE_CONFIG`.
* N.o. data bytes: *any*.
* In response to: [*Get Configuration*](#mosi-get-config)

### `0x10` Input Changed <a name="miso-input-changed"></a>

* Report input change event.
  - Content of the packet is specific for specific module types.
* Command Code byte: `0x10`.
* Standard abbreviation: `MISO_INPUT_CHANGED`.
* N.o. data bytes: *any*.
* In response to: [*Module Inquiry*](#mosi-module-inquiry)

### `0x11` Input State <a name="miso-input-state"></a>

* Report input state.
  - Content of the packet is specific for specific module types.
* Command Code byte: `0x11`.
* Standard abbreviation: `MISO_INPUT_STATE`.
* N.o. data bytes: *any*.
* In response to: [*Get Input*](#mosi-get-input)

### `0x12` Output Set <a name="miso-output-set"></a>

* Report state of outputs after setting it from master module.
  - Content of the packet is specific for specific module types.
* Command Code byte: `0x12`.
* Standard abbreviation: `MISO_OUTPUT_SET`.
* N.o. data bytes: *any*.
* In response to: [*Set Output*](#mosi-set-output)

### `0xF2` Firmware Write Flash Status <a name="miso-write-flash-status"></a>

* Report state of writing new firmware to flash.
* Command Code byte: `0xF2`.
* Standard abbreviation: `MISO_WRITE_FLASH_STATUS`.
* N.o. data bytes: *any*.
* Data byte 0:
  - `0x00` Flash Written (master can send next [Firmware Write Flash](#mosi-write-flash) command).
  - `0x01` Writing flash (master can not send next [Firmware Write Flash](#mosi-write-flash) command).
* Next data bytes contains address of written flash. Address format is specific
  for specific modules.
  - Typically 2 data bytes.
* In response to: [*Firmware Write Flash Status Request*](#mosi-write-flash-status-req)
