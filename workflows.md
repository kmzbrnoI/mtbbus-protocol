MTBbus workflows
================

## Typical bus workflow

1. Computer connected to MTB-USB is turned on. MTB-USB module is turned on,
   because it is powered from computer's USB. MTB-USB module starts scanning bus.
2. Slave modules are powered on. MTB-USB modules detects them. Slave modules
   load their configuration from EEPROM, thus they communicate in right bus
   speed. Slave modules put their outputs to *save state* (*save state* is
   part of modules configuration and thus loaded from volatile memory).
3. MTB daemon on PC starts. It connects to MTB-USB, reads its firmware and
   protocol version etc.
4. MTB daemon asks MTB-USB for list of active modules. MTB-USB sends the list
   to the daemon.
5. Demon configures modules based on its configuration stored in PC.
6. Model railway control SW connects to daemon, asks for state of inputs, starts
   settings output.
7. Input changed are reported to MTB-USB, MTB daemon and railway control
   software.
8. Railway control software disconnects, MTB daemon sends *Reset Outputs*
   for modules controlled by the railway control software.

## Different order of power on

It does not matter on order of computer, MTB-USB and slave-modules powering on.
Each time MTB daemon finally detects all modules.

## Module failure / cutout

When some slave modules stop responding, MTB-USB notices this situation and
informs MTB daemon about it.

## New modules

MTB-USB periodically scans all (even non-present) bus addresses. Thus it finds
new modules. new module is reported to MTB daemon. MTB daemon configures the
new module and reports information about new module to railroad control
software.

## Slave module replacement

Any slave module could be hot-swapped when bus is fully running.

## Module readdressing

Modules could be readdressed while bus is running. MTB-USB simply detects
old address missing and new address appearing.

## New installed module has bad speed saved

Speed must be changed either directly on slave module (reprogramming, button
press etc.) or MTB daemon must set communication to different speed, find
misconfigured module, instruct it to change speed and change bus speed back.

## Firmware upgrade

All slave modules could be upgraded directly over MTBbus. While upgrading,
other communication over bus is advised to be stopped.
