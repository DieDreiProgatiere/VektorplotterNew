## Vektorplotter ReadMe
##### Version
v2.0 (Pre-Alpha)

###  Beschreibung

Vektorplotter ist eine Software zur Berechnung von geometrischer Probleme, sowie zur Visualiserung von 2D und 3D Objekten innerhalb eines kartesischen Koordinatensystems.

### Starten von Vektorplotter (Mac & Linux)

1. Python (Version 3.8.7+) installieren
1. Zip Datei entpacken
1. Terminal öffnen
1. "python3 Verzeichnis von Vektorplotter/main.py" eingeben

### Starten von Vektorplotter (Windows)

1. Python (Version 3.8.7+) installieren
1. Zip Datei entpacken
1. Terminal öffnen
1. "python3 Verzeichnis von Vektorplotter/main.py" eingeben

### Benutzung 

1. ID´s:

	* poi = Punkt
	* vec = Vektor
	* lin = Gerade
	* pla = Ebene

2. Erstellen/Hinzufügen:

	* Wenn eine ungültige Eingabe erfolgt, könnte ein unerklärter Programmabsturz pas-sieren.
	* Objekte in < > durch entsprechendes Objekt (nicht ID) ersetzen
	* Punkt: Point(xKoordinate, yKoordinate, zKoordinate)
	* Vektor: Vector3D(xKoordinate, yKoordinate, zKoordinate)
	* Gerade: Line(<Stützvektor>, <Richtungsvektor>)


	* Ebene:
	* Normalform: Plane.normalForm(<Stützvektor>, <Normalvektor>)
	* Parameterform: Pla-ne.parameterForm(<Stützvektor>,<Richtungsvektor1>,<RV2>)
	* Koordinatenform: Plane.coordinateForm(<Normalvektor>, skalarParameter)
	* 	Zusätzlich zu den angegeben minimalen Eingaben möglich (in den Klammern) sind:
	* color=(rot,gelb,grün); Farbe; rot, gelb und grün ganzzahlig zw. 0 und 255
	* show=False; Objekt wird nur in Liste, nicht aber im Plot angezeigt
	* append=True; Bei Objekten in < > die auch einzeln angezeigt werden sollen
	
1. Rechnen:


	* Zum Rechnen müssen die Gewollten Objekte bereits existieren. Dann wird mit ihren IDs gearbeitet.
	* Wenn die Rechnung nicht möglich ist könnte das Programm unerklärt abstürzen
	* Addition von Vektoren: vec1 + vec2
	* Subtraktion von Vektoren: vec1 - vec2
	* Skalarprodukt: vec1 * vec2
	* Skalarmultiplikation: vec1 * Zahl
	* Skalardivision: vec1 : Zahl oder vec1 / Zahl
	* Kreuzprodukt: vec1 x vec2
	* Schneiden von Objekten: schneiden(obj1, obj2); obj1 und obj2 beliebig aus lin und/oder pla
	* Abstand von Objekten: d(obj1, ob2); obj1 und obj2 beliebig aus poi, lin und/oder pla
	* Schnittwinkel zw. Objekten: winkel(obj1, obj2); obj1 und obj2 beliebig aus lin und/oder pla


### Support
Bei Problemen und Nachfragen erreichen sie den Support unter:

bru1093517@phormsstudent.de
bru1093982@phormsstudent.net
kag1093737@phormsstudent.net

### Zukünftige Releases 

In der Zukunft wird eine vollfunktionsfähige grafische Oberfläche releast. 

### Autoren

Die Software wird entwickelt von:

Benjamin Brumm, Finn Brunke und Julian Kagermann

### Lizenz 

Die Lizenz berechtigt den Kunden zur Einzelnutzung des Vektorplotters im Rahmen eines normalen Gebrauchs. Dieser umfaßt die SOFTWARE-Installation und die Anfertigung einer Sicherungskopie, das Laden der SOFTWARE in den Arbeitsspeicher und seinen Ablauf. Auf andere Nutzungsarten erstreckt sich die Lizenz nicht. Der Kunde darf insbesondere keinerlei Änderungen und Übersetzungen oder weitere Vervielfältigungen des Vektorplotters vornehmen, auch nicht teilweise oder vorübergehend, gleich welcher Art und mit welchen Mitteln. Eine unzulässige Vervielfältigung stellt auch der Ausdruck des Programmcodes dar. Änderungen, zu denen FIRMA nach Treu und Glauben die Zustimmung nicht verweigert werden kann (§ 39 Abs. 2 UrhG), sind statthaft.
(Quelle: http://www.ra-juelich.com/printable/534128972a09bec02/53412898b50b5bf01/index.php Stand: 17.02.2021)
