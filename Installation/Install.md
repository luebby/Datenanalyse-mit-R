Installation von R und R Studio
================

Vorbereitungen und Hinweise
---------------------------

Während der gesamten Installation sollten Sie eine stabile Internetverbindung haben. Für die Installation müssen Sie ein wenig Zeit einplanen, der Aufwand ist aber nur einmalig nötig! Bitte beachten Sie diese Hinweise. Bei Problemen können Sie sich, bitte mit einer möglichst genauen Beschreibung (z. B. Fehlermeldung, Betriebssystem etc.), an <R@fom.de> wenden.

-   [**R**](https://www.r-project.org/) ist das Basisprogramm
-   [**R Studio**](https://www.rstudio.com/) ist eine komfortable Entwicklungsumgebung für R und bietet zusätzliche Tools, wie z. B. Dokumentenerstellung etc.
-   [**mosaic**](https://cran.r-project.org/web/packages/mosaic/) ist ein Zusatzpaket, welches u. a. eine vereinheitlichte R Syntax bietet
-   [**R Commander**](http://socserv.socsci.mcmaster.ca/jfox/Misc/Rcmdr/) ist ein Zusatzpaket für R, welches eine grafische Benutzeroberfläche für einen wichtigen Teil der Funktionalität von R zur Verfügung stellt

### Windows

Sie müssen *keine* Administrationsrechte besitzen um R und R Studio installieren zu können. Sie können in Ihr lokales Verzeichnis oder aber auch z. B. auf einen USB-Stick installieren.

### Mac OS X

Einige Zusatzpakete wie z. B.`Rcmdr` benötigen das X11 Windows System. Dies muss vorab - sofern noch nicht vorhanden - von der Seite <http://www.xquartz.org/> installiert werden. Nach der Installation muss der Computer neu gestartet werden.

1.  Installation [XQuartz](http://www.xquartz.org/)
2.  Neustart Computer
3.  Fortfahren mit der Installation von R und R Studio

Installation
------------

Installieren Sie zunächst R und anschließend R Studio.

### Installation von R

Installieren Sie die für Ihr System aktuelle Version von R von der Seite

<https://www.r-project.org/>.

Welchen Mirror Sie verwenden ist dabei egal, z. B. den Cloud Mirror von R Studio:

1.  Windows: <https://cran.rstudio.com/bin/windows/base/>
2.  Mac OS X: <https://cran.rstudio.com/bin/macosx/>

Sie können in der Regel die Standardeinstellungen innerhalb der Installation verwenden.

### Installation von R Studio

Sie können R Studio von der Seite

<https://www.rstudio.com/products/rstudio/download/>

entsprechend für Ihr Betriebssystem herunterladen und anschließend installieren.

### Installation von Zusatzpaketen

#### mosaic

Die Grundinstallation ist jetzt abgeschlossen. R Studio erkennt in der Regel automatisch R, und Sie können beides durch klicken auf das R Studio Logo starten. (Die ausführbare Datei finden Sie dabei im `bin` Ordner des Verzeichnisses, in dem Sie R Studio installiert haben.) Wenn Sie nur R starten wollen klicken Sie entsprechend auf das R Logo.

Auf ihren Bildschirm sollte folgendes Bild zu sehen sein: ![](RStudio-Screenshot.png)

Für die Vorlesung werden wir das Zusatzpaket mosaic verwenden. Installieren Sie dies, in dem Sie in der Console den Befehl

``` r
install.packages("mosaic")
```

eingeben und `Enter` oder `Return` drücken. Es werden noch weitere, abhängige Zusatzpakete installiert, der Vorgang kann also evtl. eine Weile dauern.

[Hier](https://cran.r-project.org/web/packages/mosaic/vignettes/MinimalR.pdf) gibt es eine englischsprachige Kurzübersicht über die Befehle in mosaic. Eine ausführlichere Beschreibung gibt es [hier](https://github.com/ProjectMOSAIC/LittleBooks/blob/master/StudentGuide/MOSAIC-StudentGuide.pdf).

#### R Commander

Optional: Zu Verwendung der grafischen Oberfläche R Commander bitte den Befehl eingeben:

``` r
install.packages("Rcmdr")
```

**Hinweis:** Bei der Verwendung von MAC OS X bitte unbedingt *vorher* die Hinweise zur [Vorbereitung der Installation](#anchor) beachten.

Auch hier werden einige weitere abhängige Pakete installiert, so dass es ein wenig dauern kann. Eventuell werden Sie beim erstmaligen Start des R Commanders über

``` r
library(Rcmdr)
```

gefragt, dass weitere Pakete installiert werden sollen. Dem können Sie zustimmen.

**Hinweis:** Um die Grafikfunktionalität des R Commanders innerhalb von R Studio nutzen zu können bitte *vor* dem Start des R Commanders einmal eine Grafik erzeugen, z. B. mit:

``` r
plot(airmiles) # Passenger Miles on Commercial US Airlines, 1937–1960
```

*Tipp:* Bei ausschließlicher Verwendung der grafischen Oberfläche des R Commanders diesen direkt aus R starten, ohne die Verwendung von R Studio.

Daten importieren
-----------------

Der Datenimport in R ist in vielen unterschiedlichen Dateiformaten möglich. Das`csv` Format eignet sich besonders zum Übertragen von Datendateien. Im deutschsprachigen Raum wird dabei als Dezimaltrennzeichen das Komma `,` und als Datentrennzeichen das Semikolon `;` verwendet. In der ersten Zeile müssen die Variablennamen stehen. Das Einlesen in einen R Data-Frame (hier `meineDaten`) kann dann über

``` r
meineDaten <- read.csv2(file.choose()) # Datei auswählen
```

erfolgen.

[Hier](https://www.fom.de/forschung/institute/ifes/studium-und-lehre.html#!acc=datenquellen) finden Sie eine Linksammlung zu verschiedenen Datenquellen. Das R Paket `datasets`, aber auch die optional zu installierenden Pakete `AER, mosaicData, Ecdat` enthalten ökonomisch interessante Beispieldaten.
