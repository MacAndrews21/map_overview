# map_overview

Das Kartenwerk gliedert sich in __4 Sektoren__ die gegen den Uhrzeigersinn um den Nullpunkt verlaufen. Das Beispiel beschreibt den Ablauf für die Karten 101.  
Der Kartenschlüssel deutet sich wie folgt:  
1 -> Sektor  
0 -> Zeile  
1 -> Spalte  
Innerhalb einer __Spalte__ und __Zeile__ wird wiederum in die Kartenblätter __A__, __B__, __C__ und __D__ aufgeteilt.  
Das Pythonskript verfährt folgendermaßen:

--------------------------------------------------------------
* Vom Nullpunkt ausgehend wird das Zentrum der ersten Zeile der ersten Spalte im ersten Sektor anvisiert. Um dieses werden dann die Kartenblätter erstellt.

```
Nullpunkt = 	X: 40.000
		Y: 10.000
Sektor: 1, Zeile: 0, Spalte: 1
Zentrum = 	X: Nullpunkt_X + 3200; 
		Y: Nullpunkt_Y + 2400;
Kartenblatt 101_A = 	left: Zentrum_X - 3200;
			right: Zentrum_X;
			top: Zentrum_Y + 2400;			
			bottom:Zentrum_Y;
Kartenblatt 101_B = 	left: Zentrum_X + 3200;
			right: Zentrum_X;
			top: Zentrum_Y + 2400;			
			bottom:Zentrum_Y; 
Kartenblatt 101_C = 	left: Zentrum_X - 3200;
			right: Zentrum_X;
			top: Zentrum_Y;
			bottom: Zentrum_Y - 2400;
Kartenblatt 101_D = 	left: Zentrum_X;
			right: Zentrum_X + 3200;
			top: Zentrum_Y;
			bottom: Zentrum - 2400;
```
--------------------------------------------------------------
* Die X-Koordinaten für das Zentrum werden mittels einer Schleife hochgezählt. Die Spalten lassen sich über min/max-Variablen definieren. Bsp.: min = 101; max = 102; Die Schleife läuft also für Spalte1 und 2 des ersten Sektors durch.
```
Sektor: 1, Zeile: 0, Spalte: 2
Zentrum = 	X: Nullpunkt + 3200 + (3200 * 2); 
		Y: Nullpunkt + 2400;
	...
```
--------------------------------------------------------------
* Nach durchlaufen der Spalten (min/max) wird die Y-Koordinaten hochgezählt. Gleichzeitig wird die X-Koordinate zurückgesetzt.
```
Sektor: 1, Zeile: 1, Spalte: 1
Zentrum = 	X: Nullpunkt + 3200; 
		Y: Nullpunkt + 2400 + (2400 * 2);
	...	
```
--------------------------------------------------------------
* Ab hier wiederholt sich dann alles. Für jeden Sektor gibt es ein angepasstes vorgehen, da X- bzw. Y-Koordinate entweder hochgezählt oder runtergezählt werden müssen.

