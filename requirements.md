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
  - MTB-RACILCOM
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

## Univerzálnost

* Počet a význam vstupů a výstupů není součástí obecného protokolu. Specifikují
  ho až konkrétní moduly.
* Konfigurace není součástí obecného protokolu, specifikují ji až konkrétní
  moduly. Předpokládá se, že je možné konfiguraci číst/nastavovat najednou nebo
  po bytech ("CV"). Každý typ modulu může použít jiný přístup.
* Když se změní stav vstupů modul ho nemusí posílat celý. Užitečné např. pro
  ADC moduly, kde se hdonota vstupů mění každou chvíli. Čtení stavu takových
  modulů bude pravděpodobně metodou "polling", nikoliv "event".

## Příkazy MTBbus

### master → slave

 * `INQUIRY` – žádost o odpovězení modulu
   - Lze si říct, jestli chci vždy jen IDLE nebo i info o změně stavu.
     Užití: např. v RailCom modulu.
   - Tohle musí být konfigurace MTB-USB desky.
 * `INFO` – žádost o zaslání informací o modulu
 * `SET_CONFIG` – sémantika specifická pro konkrétní modul
 * `GET_CONFIG`
 * `BEACON_ON`
 * `BEACON_OFF`
 * `GET_INPUT` – sémantika specifická pro konkrétní modul
 * `SET_OUTPUT` – sémantika specifická pro konkrétní modul
    - Zahrnuje kmitání, nastavení návěstí, ...
 * [GENERAL] `SPEED_CHANGED`
 * [GENERAL] `RESET_OUTPUTS` – požadavek na resetování stavu výstupů do výchozího
   stavu.

### slave → master

 * `OUT_SET` – výstup nastaven, pošle aktuální stav výstupů
 * `IDLE`
 * `INFO` `INFODATA`
 * `INPUT_CHANGED` – následující data jsou specifická pro konkrétní moduly
    (obsahuje např. stav všech vstupů)
 * `INPUT` – obsahuje stav vstupů
    - pozor: má být záměrně různé od `INPUT_CHANGED`, využito např. pro ADC
 * `CONFIG` – pošle konfiguraci, odpověď na `GET_CONFIG`

### `INFODATA`

 * 1 byte: typ modulu
 * 1 byte: verze FW modulu (MAJ MAJ MAJ MAJ MIN MIN MIN MIN)

## Požadavky na MTB-USB desku

 * Co si musí pamatovat
   - Aktuální seznam aktivních modulů.
   - Jestli má získávat stav všech vstupních modulů nebo si jen nechat posílat
     IDLE.

### Scénáře

 * Připojení počítače: vyčtu si aktuální seznam modulů, do každého nahrnu
   konfiguraci, resetuji výstupy, vyčtu si stav vstupů.

## Moduly

### MTB-UNI

 * Konfigurace:
   - Typ výstupů: TODO má smysl i něco jiného než S-COM?
   - Zpoždění vstupů: TODO pro každý vstup? najednou?
   - TODO něco dalšího?
   - Posílá se vždy celá.
 * Stav vstupů se vždy posílá celý (2 bytes)
 * Stav výstupů TODO (S-COM kódy 7 bit; kmitání)

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
   - A: napětí na výstupu (8 bit?)
   - A: maximální proud
 * Konfigurace: asi nic? TODO
 * Stav vstupů: vše se posílá rovnou, volat `CHANGED` jen při změně digitálních
   vstupů nebo změně o > 20 % nebo uplynutí 500 ms (a změně). Jde o to, aby se
   sběrnice zbytečně nezatěžovala.
 * Stav výstupů: posílat rovnou. Umožnit poslat jen generování DCC.
 * Modul si ukládá celý stav výstupů a po zapnutí ho obnoví.
 * Příkaz resetu sběrnice neresetuje výstupy modulu.

### MTB-POT

 * 8 8bit vstupů.
 * Stav vstupů se může posílat najednou.
 * Výstupy: žádné.

### MTB-ZDROJ

 * 4 8bit vstupy proudy, 4 8bit vstupy teploty.
 * Stav vstupů se může posílat najednou.
 * TODO nějaké další vstupy a výstupy?

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
   - Zpoždění vstupů detektoru? Ano, může ho brát v potaz i samotný přejezd.
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

## TODO

 * Má smysl mít nějaký výchozí stav výstupů jiný než 0?
   - Ano, SPAXy.
   - Co další typy modulů?
