#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

^+!m::
    Send, ^x
    Send, <mark></mark>
    Loop, 7
    {
        Send, {Left}
    }
    Send, ^v

:*:]d:: 
    ;Ex.: 02.05.2022 13:09
    FormatTime, CurrentDateTime,, dd.MM.yyyy HH:mm
    SendInput %CurrentDateTime%
return