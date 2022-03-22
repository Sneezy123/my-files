#SingleInstance, Force
SetWorkingDir, %A_ScriptDir%
program:="notepad.exe"
w:=1000
h:=600
Run, %program%
WinWaitActive, ahk_exe %program%
WinMove, A_ScreenWidth/2-w/2, A_ScreenHeight/2-h/2
WinMove, , , , , %w%, %h%
i := 1
Loop, 100
{
    SendInput, Tim hat h a w a`n
}