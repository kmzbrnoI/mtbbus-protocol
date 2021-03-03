Požadavky na nový MTB protokol
==============================

* Možnost zapnout/vypnout beacon modulu.
* Možnost najít moduly po nastartování komunikace.
* Zuniverzálnit protokol: oddělit společné příkazy a příkazy více modulů.
* Podpora nových modulů:
  - MTB-UNI: žádná konfigurace vstupů, konfigurace S-COM na libovolném výstupu,
    více frekvencí kmitání výstupu.
  - MTB-SPAX
  - MTB-přejezd
  - MTB-POT nový: pozor: velký rozsah ADC, nemůže posílat `changed`.
  - MTB-RAILCOM
* Vice bezdrátové komunikace?
  - Retranslační jednotka
* Zrušení podpory:
  - MTB-REG

## Koncepce sběrnice

* Hardwarově zachována: RS485.
* Sběrnice se nezapíná/nevypíná, skenování probíhá pořád.
* Konfigurace se neudržuje v MTB-USB desce, ale v pořítači.
   - Když se ohlásí nová deska, zkonfiguruje ji počítač.
* MTB-USB deska je "tenká" – pouze přeposílá data RS485–USB.
   - Pravidelně skenuje moduly.
     * Když modul pošle něco jiného, než IDLE, data se přepošlou rovnou do PC.
   - MTB-USB deska dále posílá:
     - Informaci, že modul vypadl
     - Informaci, že byl nalezen nový modul
   - Data z PC jdou:
     1. Pro konkrétní modul – rovnou se pošlou na sběrnici
     2. Pro všechny moduly – např. změna rychlosti sběrnice
     3. Pro MTB-USB desku – je tohle potřeba?
        - Asi jo: čtení verze FW apod.
* Desky si mohou pamatovat konfiguraci: např. S-COM výstupy, aby je po startu
  resetovaly, rychlost sběrnice.
* Na začátku zprávy musí být délka nezávisle na typu zprávy, aby MTB-USB
  modul mohl parsovat zprávy bez znalosti typů.

## Univerzálnost

* Počet a význam vstupů a výstupů není součástí obecného protokolu. Specifikují
  ho až konkrétní moduly.
* Konfigurace není součástí obecného protokolu, specifikují ji až konkrétní
  moduly. Předpokládá se, že je možné konfiguraci číst/nastavovat najednou nebo
  po bytech ("CV"). Každý typ modulu může použít jiný přístup.
* Když se změní stav vstupů modul ho nemusí posílat celý. Užitečné např. pro
  ADC moduly, kde se hdonota vstupů mění každou chvíli. Čtení stavu takových
  modulů bude pravděpodobně metodou "polling", nikoliv "event".

## Protokol

 * 0. byte: adresa
 * 1. byte: délka
 * 2. byte: typ
 * 3.–n. byte: data
 * n+1. byte: XOR

## Požadavky na MTB-USB desku

 * Co si musí pamatovat
   - Aktuální seznam aktivních modulů.
   - Jestli má získávat stav všech vstupních modulů nebo si jen nechat posílat
     IDLE.
 * Pozor: neskenovat sběrnici moc rychle, aby se moduly moc nezabývaly jen
   stavem sběrnice.

### Scénáře

 * Připojení počítače: vyčtu si aktuální seznam modulů, do každého nahrnu
   konfiguraci, resetuji výstupy, vyčtu si stav vstupů.

## Moduly

### MTB-UNI

 * Konfigurace:
   - 16 bytů: typ výstupů + bezpečný stav
   - 8 bytů: 16×4 bity: zpoždění vstupů per vstup po 0.1 s
 * Stav vstupů se vždy posílá celý (2 bytes)
 * Stav výstupů: 1 byte:
     a. S-COM 0b 1xxx xxxx
     b. úroveň: 0b 0000 000x
     c. kmitání: 0b 0100 xxxx

### MTB-SPAX

 * Vstupy:
   - D: DCC na vstupu
   - D: přetížení
   - D: napájení ~16 V na vstupu
   - A: napětí po stabilizaci (8 bit)
   - A: proud (8 bit)
   - A: teplota chladiče (8 bit)
 * Výstupy:
   - D: generování DCC zapnuto (lze vypnout jeden SPAX!)
 * Konfigurace:
   - A: napětí na výstupu (8 bit?)
   - A: maximální proud
   - Zapnout/vypnout railcom?
 * Stav vstupů: vše se posílá rovnou, volat `CHANGED` jen při změně digitálních
   vstupů nebo změně o > 20 % nebo uplynutí 500 ms (a změně). Jde o to, aby se
   sběrnice zbytečně nezatěžovala.
 * Stav výstupů: posílat rovnou. Umožnit poslat jen generování DCC.
 * Modul si ukládá celý stav výstupů a po zapnutí ho obnoví.
 * Příkaz resetu sběrnice neresetuje výstupy modulu.

### MTB-ZDROJ

 * 4 8bit vstupy proudy, 4 8bit vstupy teploty, 4 8bit vstupy napětí.
 * Stav vstupů se může posílat najednou.
 * Výstupy: zapnout/vypnout.
 * Konfigurace:
   - rychlost kmitače?

### MTB-přejezd

 * Vstupy:
   - D: 6 úseků
   - D: otevřeno
   - D: uzavřeno
   - D: výstraha
   - D: anulace
 * Výstupy:
   - D: UZ
   - D: NOT
 * Konfigurace:
   - kolik kolejí brát v potaz (lze i 0 jen pro čtení detektoru)
   - blokovat pozitivu
   - zpoždění vstupů 4 bity / vstup
 * Stav vstupů posílat najednou.
 * Stav výstupů posílat najednou.

### MTB-RAILCOM

 * 8 RailCom úseků
 * Zahrnuje v sobě detektor obsazení?
 * Vstupy:
   - 8×10 bit, asi 16 bytes
   - Do zbylých bitů se kóduje číslo vstupu, aby šlo posílat jen nějaké vstupy.
   - TODO D: 8 obsazení
 * Výstupy: žádné
 * Konfigurace:
   - Zpoždění vstupů (detektorů + RailCom)
 * Musí mít relativně velké prodlevy při ztrátě adres na vstupech.
 * Při změně posílá jen změněné adresy.

## MTB-DISPLAY

 * Např. display v pultu
 * Pult: bezdrátový modul?

## TODO

 * Popsat typický chod sběrnice
   - Firmware Upgrade Procedure
 * Popsat příkazy pro moduly:
   - Set Configuration
 * Má smysl mít nějaký výchozí stav výstupů jiný než 0?
   - Ano, SPAXy.
   - Co další typy modulů?
 * Remote programming, podpora v řídícím SW https://github.com/jgillick/avr-multidrop-bootloader
 * Baudrate autodetect
 * MQTT
 * Jak psát dokumentaci: sfinx
