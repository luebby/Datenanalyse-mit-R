#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  style.py (Release: 0.4.5)
  ========-----------------
  A Quick-Typographie-Pandoc-Panflute-Filter.

  (C)opyleft in 2018/19 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 21.03.2018 (nm) - Erste Version
  0.2   - 25.03.2018 (nm) - Code (angebelich) "wartbarer" gemacht.
  0.3   - 08.04.2018 (nm) - Umgestellt auf Decorator Klasse
  0.3.1 - 14.06.2018 (nm) - Code noch "wartbarer" gemacht.
  0.4.0 - 27.12.2018 (nm) - Kleinere Erweiterungen.
  0.4.1 - 27.12.2018 (nm) - Umstellung auf autofilter.
  0.4.2 - 03.01.2019 (nm) - Bugfixe
  0.4.3 - 05.02.2019 (nm) - Fehler behoben.
  0.4.4 - 26.02.2019 (nm) - Kleinere Schönheitsupdates
  0.4.5 - 21.03.2019 (nm) - Unterstürtzung für "cemph" und "cstrong".


  WICHTIG:
  ========
    Benoetigt python3 !
    -> https://www.howtogeek.com/197947/how-to-install-python-on-windows/
    oder
    -> https://www.youtube.com/watch?v=dX2-V2BocqQ
    Bei *nix und macOS Systemen muss diese Datei als "executable" markiert
    sein!
    Also bitte ein
      > chmod a+x style.py
   ausfuehren!


  Lizenz:
  =======
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


import panflute as pf  # panflute fuer den pandoc AST
import logging  # logging fuer die 'typography.log'-Datei
import os as os  # check if file exists.
from decorator import *

"""
 Eine Log-Datei "style.log" erzeugen um einfacher zu debuggen
 Durch eine Datei "style.loglevel.<level>" kann mit den

    <level>=debug|info|error
 
 der level für das logging extern ausgewählt werden.
"""
if os.path.exists("style.loglevel.debug"): 
    DEBUGLEVEL = logging.DEBUG
elif os.path.exists("style.loglevel.info"):
    DEBUGLEVEL = logging.INFO
elif os.path.exists("style.loglevel.warning"):
    DEBUGLEVEL = logging.WARNING
elif os.path.exists("style.loglevel.error"):
    DEBUGLEVEL = logging.ERROR
else:
    DEBUGLEVEL = logging.ERROR  # .ERROR or .DEBUG  or .INFO
    
logging.basicConfig(filename='style.log', level=DEBUGLEVEL)

"""
 LaTeX Fontsize commands in beamer:
 \tiny, \scriptsize, \footnotesize, \small, \normalsize (default),
 \large, \Large, \LARGE, \huge and \Huge.

 Handle Classes ".tiny", ".scriptsize", ".footnotesize", ".small",
                ".normalsize" (default), "large", ".Large",
                ".LARGE", ".huge"" and ".Huge".
"""
FONTSIZECLASSES = (
    "tiny", "scriptsize", "footnotesize", "small",
    "normalsize", "large", "Large",
    "LARGE", "huge", "Huge")

BLOCKCLASSES = {
    "theorem",
    "example",
    "examples",
    "definition",
    "proof",
    "remark",
    "remarks",
    "exercise",
    "fact",
    "facts"
}

TEX_BLOCKCLASSES_TAG = {
    "theorem": "Satz",
    "example": "Beispiel",
    "examples": "Beispiele",
    "definition": "definition",
    "proof": "Beweis",
    "remark": "Bemerkung",
    "remarks": "Bemerkungen",
    "exercise": "Uebung",
    "fact": "Fakt",
    "facts": "Fakten"
}


dec = Decorator()

blocktag = None


def setDecorator(doc):
    global dec

    if doc.format in ["latex", "beamer"]:
        dec = LaTeXDecorator()

    if doc.format == "html":
        dec = HTMLDecorator()


def handleDiv(e):
    """
    Handle DIV Blocks only
    """


def handleDivAndSpan(e, doc):
    """
     Handle DIV and SPAN Blocks in gerneral
    """

    global dec

    setDecorator(doc)

    dec.handleDiv(e)
    dec.handleSpan(e)
    dec.handleDivAndSpan(e)

    if dec.hasPrePost():
        before = after = ""
        if isinstance(e, pf.Div):
            before = dec.getBeforeBlock()
            after = dec.getAfterBlock()

        if isinstance(e, pf.Span):
            before = dec.getBeforeInline()
            after = dec.getAfterInline()

        e.content = [before] + list(e.content) + [after]
        return e


def handleHeaderLevelOne(e, doc):
    """Future work!
    """
    if isinstance(e.next, pf.Div) and ("Sinnspruch" in e.next.classes):
        logging.debug("We have work to do!")


def handleHeaderBlockLevel(e, doc):
    """

    :param e:
    :param doc:
    :return:
    """
    global blocktag
    tag = blocktag
    blocktag = None
    before = None
    if tag:
        before = pf.RawBlock("\\end{"+tag+"}\n", "latex")
        if "endblock" in e.classes:
            return before

    for blocktype in BLOCKCLASSES:
        if blocktype in e.classes: 
            logging.debug("BLOCKTYPE:" + blocktype)
            if not isinstance(e.content, pf.ListContainer):
                logging.debug("CONTENT:" + pf.stringify(e.content))
                tag = TEX_BLOCKCLASSES_TAG[blocktype]
                elem = pf.Div()
                elem.content = [
                    pf.Plain(
                        pf.RawInline("\n\\begin{"+tag+"}[", "latex"),
                        e.content,
                        pf.RawInline("]\n", "latex")
                        )
                ]

                blocktag = tag

                if before:
                    return [before, elem]
                return elem
            else:
                logging.debug("CONTENT: Listcontainer")


def handleHeader(e, doc):
    """

    :param e:
    :param doc:
    :return:
    """
    global blocktag
    tag = blocktag
    blocktag = None
    if "endblock" in e.classes:
        return pf.RawBlock("\\end{"+tag+"}\n")
    if tag:
        return [pf.RawBlock("\\end{"+tag+"}\n", "latex"), e]

def action(e, doc):
    """Main action function for panflute.
    """
    if isinstance(e, pf.Header) and e.level < 4:
        return handleHeader(e, doc)

    if isinstance(e, (pf.Div, pf.Span)):
        return handleDivAndSpan(e, doc)

    if isinstance(e, pf.Header) and e.level == 4:
        return handleHeaderBlockLevel(e, doc)


def prepare(doc):
    """Do nothing before action, but it is necessary for 'autofilter'.

    :param doc: current document
    :return: current document
    """
    pass


def finalize(doc):
    """Do nothing after action, but it is necessary for 'autofilter'.

    :param doc: current document
    :return: current document
    """
    pass


def main(doc=None):
    """Main function.

    start logging, do work and close logging.

    :param doc: document to parse
    :return: parsed document
    """
    logging.debug("Start pandoc filter 'style.py'")
    ret = pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc) 
    logging.debug("End pandoc filter 'style.py'")
    return ret


"""
 as always
"""
if __name__ == "__main__":
    main()
