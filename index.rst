MTBbus Protocol Documentation
=============================

MTBbus is RS485-based communication bus for controlling general-purpose IO
modules. It's original aim is to control model railroad accessories (e.g.
turnouts, signals etc.) however the bus is designed generally and extendably.

The bus consists of a single master module (MTB-USB module) and up to 255
IO modules. The bus is conrolled from single device, usually a computer with
appropriate control software.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   basics
   packet

   commands/mosi/01-inquiry



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
