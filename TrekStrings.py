﻿import gettext

# _ = gettext.gettext

fr = gettext.translation('startrek2020', localedir='locale', languages=['fr'])
fr.install()

LOGO_TREKER = r"""
               ______ _______ ______ ______    _______ ______  ______ __  __ 
              / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /
             / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / // /
             _\ \     / /  / __  //   __/      / /  /   __/ / __ / /   / 
           / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \
          /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\

                                     1971 - 2020     
                           ________________        _
                           \__(=======/_=_/____.--'-`--.___
                                      \ \   `,--,-.___.----'
                                    .--`\\--'../
                                   '---._____.|]""".split('\n')
    

AREA_NAMES = [
    "Aaamazzara",
    "Altair IV",
    "Aurelia",
    "Bajor",
    "Benthos",
    "Borg Prime",
    "Cait",
    "Cardassia Prime",
    "Cygnia Minor",
    "Daran V",
    "Duronom",
    "Dytallix B",
    "Efros",
    "El-Adrel IV",
    "Epsilon Caneris III",
    "Ferenginar",
    "Finnea Prime",
    "Freehaven",
    "Gagarin IV",
    "Gamma Trianguli VI",
    "Genesis",
    "H'atoria",
    "Holberg 917-G",
    "Hurkos III",
    "Iconia",
    "Ivor Prime",
    "Iyaar",
    "Janus VI",
    "Jouret IV",
    "Juhraya",
    "Kabrel I",
    "Kelva",
    "Ktaris",
    "Ligillium",
    "Loval",
    "Lyshan",
    "Magus III",
    "Matalas",
    "Mudd",
    "Nausicaa",
    "New Bajor",
    "Nova Kron",
    "Ogat",
    "Orion III",
    "Oshionion Prime",
    "Pegos Minor",
    "P'Jem",
    "Praxillus",
    "Qo'noS",
    "Quadra Sigma III",
    "Quazulu VIII",
    "Rakosa V",
    "Rigel VII",
    "Risa",
    "Romulus",
    "Rura Penthe",
    "Sauria",
    "Sigma Draconis",
    "Spica",
    "Talos IV",
    "Tau Alpha C",
    "Ti'Acor",
    "Udala Prime",
    "Ultima Thule",
    "Uxal",
    "Vacca VI",
    "Volan II",
    "Vulcan",
    "Wadi",
    "Wolf 359",
    "Wysanti",
    "Xanthras III",
    "Xendi Sabu",
    "Xindus",
    "Yadalla Prime",
    "Yadera II",
    "Yridian",
    "Zalkon",
    "Zeta Alpha II",
    "Zytchin III",
    ]

HELM_CMDS = [
    _("--- Commands -----------------"),
    _("nav = Warp Speed      srs = Short Range Scan  tor = Photon Torpedos"),
    _("sub = Sublight Speed  lrs = Long Range Scan   pha = Phasers"),
    _("qui = Quit            com = Access Computer   she = Shields"),
    ]

CPU_CMDS = [
    _("--- Main Computer --------------"),
    _("rec = Cumulative Galatic Record"),
    _("sta = Status Report"),
    _("tor = Photon Torpedo Targets"),
    _("bas = Starbase Locations"),
    ]