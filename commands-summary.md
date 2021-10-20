# Commands summary

## Master → Slave

<table>
<tr><th>Command</th><th>Code byte</th><th>Abbreviation</th><th>Response</th><th>Addressed</th></tr>
<tr>
 <td><a href="commands.md#mosi-module-inquiry">Module Inquiry</a></td>
 <td><code>0x1</code></td>
 <td><code>MOSI_MODULE_INQUIRY</code></td>
 <td><a href="commands.md#miso-ack">ACK</a>, <a href="commands.md#miso-input-changed">Input Changed</a>, <a href="commands.md#miso-diag-info">Module Diagnostic Info</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-info">Module Information Request</a></td>
 <td><code>0x2</code></td>
 <td><code>MOSI_MODULE_INFO_REQ</code></td>
 <td><a href="commands.md#miso-module-info">Module information</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-set-config">Set Configuration</a></td>
 <td><code>0x3</code></td>
 <td><code>MOSI_SET_CONFIG</code></td>
 <td><a href="commands.md#miso-ack">ACK</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-get-config">Get Configuration</a></td>
 <td><code>0x4</code></td>
 <td><code>MOSI_GET_CONFIG</code></td>
 <td><a href="commands.md#miso-config">Configuration</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-beacon">Beacon</a></td>
 <td><code>0x5</code></td>
 <td><code>MOSI_BEACON</code></td>
 <td><a href="commands.md#miso-ack">ACK</a></td>
 <td>address, broadcast</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-get-input">Get Input</a></td>
 <td><code>0x10</code></td>
 <td><code>MOSI_GET_INPUT</code></td>
 <td><a href="commands.md#miso-input-state">Input State</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-set-output">Set Output</a></td>
 <td><code>0x11</code></td>
 <td><code>MOSI_SET_OUTPUT</code></td>
 <td><a href="commands.md#miso-output-set">Output Set</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-reset-outputs">Reset Outputs</a></td>
 <td><code>0x12</code></td>
 <td><code>MOSI_RESET_OUTPUTS</code></td>
 <td><a href="commands.md#miso-ack">ACK</a></td>
 <td>address, broadcast</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-change-address">Change Address</a></td>
 <td><code>0x20</code></td>
 <td><code>MOSI_CHANGE_ADDR</code></td>
 <td><a href="commands.md#miso-ack">ACK</a>, <a href="commands.md#miso-error">Error</a></td>
 <td>address, broadcast</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-diag-info-req">Diagnostic Info Request</a></td>
 <td><code>0xd0</code></td>
 <td><code>MOSI_DIAG_INFO_REQ</code></td>
 <td><a href="commands.md#miso-diag-info">Module Diagnostic Info</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-speed-changed">Change Speed</a></td>
 <td><code>0xe0</code></td>
 <td><code>MOSI_CHANGE_SPEED</code></td>
 <td>–</td>
 <td>broadcast</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-reprog">Firmware Upgrade Request</a></td>
 <td><code>0xf0</code></td>
 <td><code>MOSI_FWUPGD_REQUEST</code></td>
 <td><a href="commands.md#miso-ack">ACK</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-write-flash">Firmware Write Flash</a></td>
 <td><code>0xf1</code></td>
 <td><code>MOSI_WRITE_FLASH</code></td>
 <td><a href="commands.md#miso-ack">ACK</a>, <a href="commands.md#miso-error">Error</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-write-flash-status-req">Firmware Write Flash Status Request</a></td>
 <td><code>0xf2</code></td>
 <td><code>MOSI_WRITE_FLASH_STATUS_REQ</code></td>
 <td><a href="commands.md#miso-write-flash-status">Firmware Write Flash Status</a></td>
 <td>address</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-modules-specific">Module-specific command</a></td>
 <td><code>0xfe</code></td>
 <td><code>MOSI_SPECIFIC</code></td>
 <td>–</td>
 <td>address, broadcast</td>
</tr>
<tr>
 <td><a href="commands.md#mosi-reboot">Reboot</a></td>
 <td><code>0xff</code></td>
 <td><code>MOSI_REBOOT</code></td>
 <td><a href="commands.md#miso-ack">ACK</a></td>
 <td>address, broadcast</td>
</tr>
</table>


## Slave → Master

<table>
<tr><th>Command</th><th>Code byte</th><th>Abbreviation</th></tr>
<tr>
 <td><a href="commands.md#miso-ack">Acknowledgement</a></td>
 <td><code>0x1</code></td>
 <td><code>MISO_ACK</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-error">Error</a></td>
 <td><code>0x2</code></td>
 <td><code>MISO_ERROR</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-module-info">Module information</a></td>
 <td><code>0x3</code></td>
 <td><code>MISO_MODULE_INFO</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-config">Module Configuration</a></td>
 <td><code>0x4</code></td>
 <td><code>MISO_MODULE_CONFIG</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-input-changed">Input Changed</a></td>
 <td><code>0x10</code></td>
 <td><code>MISO_INPUT_CHANGED</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-input-state">Input State</a></td>
 <td><code>0x11</code></td>
 <td><code>MISO_INPUT_STATE</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-output-set">Output Set</a></td>
 <td><code>0x12</code></td>
 <td><code>MISO_OUTPUT_SET</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-diag-info">Module Diagnostic Info</a></td>
 <td><code>0xd0</code></td>
 <td><code>MISO_DIAG_INFO</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-write-flash-status">Firmware Write Flash Status</a></td>
 <td><code>0xf2</code></td>
 <td><code>MISO_WRITE_FLASH_STATUS</code></td>
</tr>
<tr>
 <td><a href="commands.md#miso-modules-specific">Module-specific command</a></td>
 <td><code>0xfe</code></td>
 <td><code>MISO_SPECIFIC</code></td>
</tr>
</table>
