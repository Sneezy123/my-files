#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

Run, explorer.exe
WinWaitActive,Explorer, ,3
WinMove, 0, 0
WinMove, , , , , 100, 100