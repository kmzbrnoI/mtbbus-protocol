# Commands summary

## Master → Slave

<table>
<tr><th>Command</th><th>Code byte</th><th>Abbreviation</th></tr>
<tr>
 <td>[Module Inquiry](commands.md#mosi-module-inquiry)</td>
 <td>`0x1`</td>
 <td>`MOSI_MODULE_INQUIRY`</td>
</tr>
<tr>
 <td>[Module Information Request](commands.md#mosi-info)</td>
 <td>`0x2`</td>
 <td>`MOSI_MODULE_INFO_REQ`</td>
</tr>
<tr>
 <td>[Set Configuration](commands.md#mosi-set-config)</td>
 <td>`0x3`</td>
 <td>`MOSI_SET_CONFIG`</td>
</tr>
<tr>
 <td>[Get Configuration](commands.md#mosi-get-config)</td>
 <td>`0x4`</td>
 <td>`MOSI_GET_CONFIG`</td>
</tr>
<tr>
 <td>[Beacon](commands.md#mosi-beacon)</td>
 <td>`0x5`</td>
 <td>`MOSI_BEACON`</td>
</tr>
<tr>
 <td>[Get Input](commands.md#mosi-get-input)</td>
 <td>`0x10`</td>
 <td>`MOSI_GET_INPUT`</td>
</tr>
<tr>
 <td>[Set Output](commands.md#mosi-set-output)</td>
 <td>`0x11`</td>
 <td>`MOSI_SET_OUTPUT`</td>
</tr>
<tr>
 <td>[Reset Outputs](commands.md#mosi-reset-outputs)</td>
 <td>`0x12`</td>
 <td>`MOSI_RESET_OUTPUTS`</td>
</tr>
<tr>
 <td>[Change Address](commands.md#mosi-change-address)</td>
 <td>`0x20`</td>
 <td>`MOSI_FWUPGD_REQUEST`</td>
</tr>
</table>


## Slave → Master

<table>
<tr><th>Command</th><th>Code byte</th><th>Abbreviation</th></tr>
<tr>
 <td>[Acknowledgement](commands.md#miso-ack)</td>
 <td>`0x1`</td>
 <td>`MISO_ACK`</td>
</tr>
<tr>
 <td>[Error](commands.md#miso-error)</td>
 <td>`0x2`</td>
 <td>`MISO_ERROR`</td>
</tr>
<tr>
 <td>[Module information](commands.md#miso-module-info)</td>
 <td>`0x3`</td>
 <td>`MISO_MODULE_INFO`</td>
</tr>
<tr>
 <td>[Module Configuration](commands.md#miso-config)</td>
 <td>`0x4`</td>
 <td>`MISO_MODULE_CONFIG`</td>
</tr>
<tr>
 <td>[Input Changed](commands.md#miso-input-changed)</td>
 <td>`0x10`</td>
 <td>`MISO_INPUT_CHANGED`</td>
</tr>
<tr>
 <td>[Input State](commands.md#miso-input-state)</td>
 <td>`0x11`</td>
 <td>`MISO_INPUT_STATE`</td>
</tr>
</table>
