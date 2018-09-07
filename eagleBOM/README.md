# Ealge BOM fixer

This script allows to fully automate the BOM creation using the native BOM generator from Eagle CAD. This script is based on the components used having those fields in the library:

[!alt-text](figs/settingsOfComponents.png)

This will also work if the components don't present any of those filds.

## How to obtain the BOM

First of all you need to run the ULP in Eagle Schematic. The ULP to be ran is the default BOM ULP as shown below.

[!alt-text](figs/ULP_handler.png)

Then you should export the BOM under the CSV format by selecting the option *CSV* and the option *Values*. **Disclaimer**: This script will not work with the *Parts* option

[!alt-text](figs/howto.png)

Then you can run the script by using the command line: 

```
./eagleBOM.py -file samples/sample1.csv
```


