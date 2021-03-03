MTBbus commands
===============

## Master → Slave

### `0x01` Module Inquiry {#mosi-module-inquiry}

 * This commands instructs module to respond with any information it has to
   send.
 * Command code byte: `0x01`
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

### `0x02` Module Info Request {#miso-info}

 * `INFO` – žádost o zaslání informací o modulu
    - Odpověď: `INFO`

### `0x03` Set Config {#miso-set-config}

 * `SET_CONFIG` – sémantika specifická pro konkrétní modul
    - Odpověď: `ACK`

### `0x04` Get Config {#miso-get-config}

 * `GET_CONFIG`
    - Odpověď: `ACK`

### `0x05` Beacon {#miso-beacon}

 * `BEACON_ON`
    - Odpověď: `ACK`
 * `BEACON_OFF`
    - Odpověď: `ACK`

### `0x06` Get Input {#miso-get-input}

 * `GET_INPUT` – sémantika specifická pro konkrétní modul
    - Odpověď: `INPUT`

### `0x07` Set Output {#miso-set-output}

 * `SET_OUTPUT` – sémantika specifická pro konkrétní modul
    - Zahrnuje kmitání, nastavení návěstí, ...
    - Odpověď: `ACK`

### `0x10` Reset Output {#miso-reset-outputs}

 * [GENERAL] `RESET_OUTPUTS` – požadavek na resetování stavu výstupů do výchozího
   stavu.

### `0x11` Change Address {#miso-change-address}

 * `CHANGE_ADDRESS` – změň adresu na zadanou; lze i jako broadcast a pak
   se změní jen u modulů se zmáčknutým tlačítkem
    - Odpověď: `ACK`

### `0xE0` Speed Changed {#miso-speed-changed}

 * [GENERAL] `SPEED_CHANGED`

### `0xF0` Reprogramming {#miso-reprog}

 * `REPROG` – restartuj se a připrav se na nahrání nového FW
    - Odpověď: již speciální odpověď protokolu pro nahrávání firmwaru


## Slave → Master

 * `OUT_SET` – výstup nastaven, pošle aktuální stav výstupů
 * `IDLE`
 * `INFO` `INFODATA`
 * `INPUT_CHANGED` – následující data jsou specifická pro konkrétní moduly
    (obsahuje např. stav všech vstupů)
 * `INPUT` – obsahuje stav vstupů
    - pozor: má být záměrně různé od `INPUT_CHANGED`, využito např. pro ADC
 * `CONFIG` – pošle konfiguraci, odpověď na `GET_CONFIG`
 * `ACK`

### `INFODATA`

 * 1 byte: typ modulu
 * 1 byte: verze FW modulu (MAJ MAJ MAJ MAJ MIN MIN MIN MIN)
