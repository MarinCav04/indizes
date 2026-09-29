 # Report: Indizes

## 1. Python-Skript
Für die Erstellung der Testdatenbank wurde ein Python-Skript geschrieben. Um die geforderten 500.000 Datensätze (Tabelle `person` mit `id`, `first_name`, `last_name`) schnell und performant zu generieren, habe ich die Bibliothek `mimesis` benutzt. Anstatt jeden Eintrag einzeln in die SQLite-Datenbank zu schreiben, wurden eine Liste von Tuple erstellt und per `executemany`-Befehl importiert, was die Ausführungszeit enorm verkürzt hat.

## 2. Analyse der Streuung
Da sich das mathematische Maß der Varianz (welches Distanzen zwischen Objekten voraussetzt) nicht auf Textfelder wie Namen anwenden lässt, wurde mit einem SQL-`WITH`-Statement der prozentuale Anteil der häufigsten Nachnamen an der Gesamtmenge berechnet: 
* Die Bibliothek `mimesis` streut die Daten sehr gleichmäßig.
* Die beiden häufigsten Nachnamen (Newman und Petty) kamen in 500.000 Datensätzen jeweils nur 568 Mal vor.
* Das entspricht einem extrem geringen Anteil von lediglich ca. 0,11 % an der Gesamtmenge.

## 3. Performance und Speicherbedarf durch Indizes
Um den Effekt eines Indexes zu testen, wurde die Datenbank vor und nach der Erstellung eines Indexes auf Nachnamen (`CREATE INDEX id_last_name ON person(last_name);`) verglichen.

**Auswirkung auf Geschwindigkeit:**
* **Laufzeit ohne Index:** 0,314 Sekunden
* **Laufzeit mit Index:** 0,060 Sekunden
* **Fazit:** Die Abfrage war mit Index mehr als fünfmal so schnell.

**Speicherbedarf:**
Dieser Geschwindigkeitsvorteil kostet allerdings Speicherplatz, da die Index-Struktur zusätzlich in der Datei abgelegt wird.
* **Dateigröße ohne Index:** ca. 10.820 KB
* **Dateigröße mit Index:** ca. 18.216 KB
* **Fazit:** Allein dieser eine Index hat die Datenbankdatei um fast 70 % vergrößert.