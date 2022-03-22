#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%
program:="notepad.exe"
w:=1000
h:=600
Run, %program%
WinWaitActive, ahk_exe %program%
WinMove, A_ScreenWidth/2-w/2, A_ScreenHeight/2-h/2
WinMove, , , , , %w%, %h%

fibonacci(a)
{
    if (a <= 1)
    {
        Send, a
    }
    Send, %a%
    a:=fibonacci(a-1)+fibonacci(a-2)
}

