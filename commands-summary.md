# Commands summary

## Master → Slave

<table>
<tr><th>Command</th><th>Code byte</th><th>Abbreviation</th></tr>
<tr>
 <td><a href="commands.md#mosi-module-inquiry">Module Inquiry</a></td>
 <td><code>0x1</code></td>
 <td><code>MOSI_MODULE_INQUIRY</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-info">Module Information Request</a></td>
 <td><code>0x2</code></td>
 <td><code>MOSI_MODULE_INFO_REQ</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-set-config">Set Configuration</a></td>
 <td><code>0x3</code></td>
 <td><code>MOSI_SET_CONFIG</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-get-config">Get Configuration</a></td>
 <td><code>0x4</code></td>
 <td><code>MOSI_GET_CONFIG</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-beacon">Beacon</a></td>
 <td><code>0x5</code></td>
 <td><code>MOSI_BEACON</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-get-input">Get Input</a></td>
 <td><code>0x10</code></td>
 <td><code>MOSI_GET_INPUT</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-set-output">Set Output</a></td>
 <td><code>0x11</code></td>
 <td><code>MOSI_SET_OUTPUT</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-reset-outputs">Reset Outputs</a></td>
 <td><code>0x12</code></td>
 <td><code>MOSI_RESET_OUTPUTS</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-change-address">Change Address</a></td>
 <td><code>0x20</code></td>
 <td><code>MOSI_CHANGE_ADDR</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-speed-changed">Change Speed</a></td>
 <td><code>0xe0</code></td>
 <td><code>MOSI_CHANGE_SPEED</code></td>
</tr>
<tr>
 <td><a href="commands.md#mosi-reprog">Firmware Upgrade Request</a></td>
 <td><code>0xf0</code></td>
 <td><code>MOSI_FWUPGD_REQUEST</code></td>
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
</table>
