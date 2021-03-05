# coding: utf-8
data = '''

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░____▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓____________________________________________________________░░____________________________________░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓____░░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓____________________________________________________________░░____________________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓____░░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓__________________░░░░____________________________________________░░______________________________▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓____░░▓▓▓▓▓▓▓▓▓▓████▓▓▓▓________░░░░░░______░░______░░░░░░________________________________░░______________________________░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░____░░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓__░░________________░░░░____________░░░░__________________________________________________________░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓________▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░________░░▓▓▓▓▒▒░░░░▒▒▓▓▓▓▓▓__________░░__________________________░░____________________________░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒________▓▓▓▓▓▓▓▓▓▓████▒▒__________▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒__________░░____________░░________░░____________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░________▓▓▓▓▓▓▓▓▓▓██▒▒________▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░____▓▓▓▓▓▓▓▓▓▓▓▓▒▒________░░__________░░______________________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓__________░░▓▓▓▓▓▓▓▓▒▒______▒▒▓▓▒▒__▒▒▓▓▓▓▒▒░░________▒▒▓▓▓▓░░░░▓▓▓▓░░______░░____________________░░__________________________░░▓▓▒▒░░▒▒▒▒░░▒▒░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░____________▓▓▓▓▓▓▓▓______▓▓▓▓░░____░░░░________________░░▒▒______▒▒▓▓________░░____░░____________░░__________________________░░▓▓▒▒░░▒▒░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓______________░░▓▓▓▓______▒▒▒▒________________________________________░░▓▓______░░__░░______________░░__________________________░░▓▓░░░░▒▒░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓________________░░░░____▒▒░░____________________________________________░░▒▒____░░░░________________░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓__________________░░░░░░░░________________________________________________░░▒▒░░░░__________________░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓________________░░░░░░______░░______░░____________________________░░__________░░░░__________________░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░______________░░░░░░____░░______░░______░░______________________░░____░░____░░░░░░________________░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓______________░░░░░░____░░______░░______░░______________░░______________░░____░░░░______________░░____________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░__________░░░░░░____░░________________░░______________░░________░░____░░____░░░░░░____________░░____________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓__________░░░░░░____░░______░░________░░______________░░______________________░░░░__________░░░░____________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░______░░░░░░░░____░░______░░________░░__________░░__░░________________░░____░░░░░░________░░░░░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░____░░▒▒▒▒______________░░______░░░░__░░______░░__░░░░______________░░____░░░░░░░░____░░░░░░░░__________________________░░▓▓░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░____░░______░░░░______▒▒░░__░░______░░____░░________░░____░░____░░░░░░░░░░░░▒▒░░░░░░__________________________░░▓▓░░░░░░░░░░▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓____░░░░▒▒▒▒____░░______░░________▒▒░░__░░______░░____░░________░░____________▒▒▒▒░░░░__░░░░░░░░__________________________░░▓▓▒▒░░░░░░░░▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓____░░░░░░░░____░░______░░________░░░░__░░______░░____▒▒________░░____________▒▒░░░░░░__░░▒▒▒▒░░__________________________░░▓▓▒▒░░░░░░░░▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒____░░░░░░░░____░░░░____░░________░░░░__________░░____▒▒________░░____________▒▒░░░░____░░░░______________________________░░▓▓▒▒░░░░░░░░▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░______░░▒▒________░░__░░░░________░░░░__░░______░░____░░░░__░░__░░____________▒▒░░________░░______________________________░░▓▓░░░░░░░░░░▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░________░░________░░__░░▒▒__░░░░░░░░░░__░░______░░__░░░░░░░░░░________________░░░░________░░______________________________░░▓▓░░░░▒▒▒▒▒▒▒▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓__________░░________░░__░░▓▓__░░__░░░░░░__░░______░░____░░░░__░░________________░░░░________░░______________________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓________░░░░________░░__░░▒▒__░░__░░░░░░__░░______░░____░░▒▒__░░░░____░░________░░░░__________░░____________________________░░▓▓░░░░▒▒▒▒▒▒▒▒▒▒
████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒____________░░________░░__░░▒▒__░░__░░░░░░__▒▒______░░____░░▒▒____░░__░░__________░░________________░░________________________▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓________________░░________░░__░░▒▒__░░__░░__░░__▒▒__________░░__░░____░░__░░░░________░░░░____________░░__________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░________░░░░__░░░░__░░__░░__░░__▒▒__________░░__░░░░__▒▒__▒▒░░________░░____░░░░░░░░░░░░__________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓__________░░____░░░░__░░__▒▒░░░░░░░░__________░░__░░░░__▒▒__▒▒░░░░______░░____░░░░░░░░░░░░__________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓__________░░____▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░__▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░______░░____░░░░░░░░░░░░__________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓__________░░▒▒░░▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░____________▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░______░░____░░░░░░░░░░░░__________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒____________▒▒__░░__░░▓▓▓▓▓▓▓▓░░________________▒▒▓▓▒▒▓▓▓▓░░░░__░░______░░____░░░░░░░░░░░░__________________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░____░░______░░__░░__▓▓▓▓▒▒▓▓▓▓░░________________▓▓▓▓▒▒▓▓▓▓░░░░__░░____________░░░░░░░░░░░░░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░__░░______░░______▒▒▒▒▓▓░░▒▒__________________▒▒▓▓▓▓__▒▒____░░░░____________░░░░░░░░░░░░░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████▓▓▓▓▓▓████████▓▓______░░______░░______░░▒▒░░__▒▒__________________░░░░░░__░░____░░______░░______░░▒▒▒▒▒▒░░▒▒░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████______░░________░░__░░____░░░░________________________░░░░______░░______░░________▓▓▒▒▒▒▒▒▒▒░░________________________▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████▓▓______________░░░░__░░__________________________________________░░____░░__________░░░░░░░░▒▒░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████▓▓░░__░░____░░░░░░░░░░__░░░░░░____________________________░░__░░____░░░░░░░░____________░░▒▒▒▒▒▒░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████____░░____░░░░░░░░░░____________________________________________░░░░░░░░░░__░░____░░__▒▒▒▒▒▒▒▒░░________________________░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████▓▓____░░____░░░░░░░░░░░░__________________________________________▒▒░░░░░░▒▒__░░________░░▒▒▒▒▒▒░░________________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████░░__░░____░░░░░░░░░░░░________________________________________░░▒▒░░░░░░▒▒░░░░________▒▒▒▒▒▒▒▒░░________________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████▓▓______░░▒▒▒▒░░░░░░░░▒▒____________________________________░░░░▒▒░░░░░░░░░░░░__░░__░░▒▒▒▒▒▒▒▒░░__░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████▒▒░░░░▒▒░░░░░░░░▒▒░░░░░░______________________________░░░░░░░░░░░░░░░░░░░░░░░░░░________░░░░__░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████████████████████████▓▓▓▓▒▒▒▒░░▒▒░░░░▒▒░░░░░░░░░░______________________░░__░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒______░░░░____░░░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████████████████████████████████████████████▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░__░░░░░░__________░░░░░░░░____░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓________░░__░░░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████████████████████████████████▓▓▓▓████████▓▓▓▓▓▓▓▓░░▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░__░░____░░░░░░▒▒░░▒▒░░░░░░░░________▒▒░░░░░░▓▓▓▓▓▓▓▓▒▒░░▓▓▒▒________░░__░░____________________▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒____░░______░░░░░░░░░░░░░░░░____░░____▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░__░░░░__░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░______░░__________░░░░░░______________▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░____░░____________________▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░______░░____________________░░____░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░____░░____________________░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒░░________░░______________░░________░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░______░░░░__░░____________________▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████▓▓▓▓░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓__░░▒▒▒▒▒▒____________░░░░__░░░░░░__________░░░░▒▒▒▒__▒▒▓▓▓▓▓▓▓▓▓▓▓▓__________░░░░░░____________________▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░________________________________▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░______▒▒▒▒▒▒____________░░______░░░░__________░░▒▒░░▒▒____░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░__░░__░░__░░__░░__░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒________________________________________░░▓▓░░▓▓▓▓▓▓▓▓▓▓░░______▒▒░░▒▒____________░░__░░░░__░░__________░░▒▒░░░░____░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░__░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''

print (data)
