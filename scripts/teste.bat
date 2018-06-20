@echo off
For /F "tokens=1,2,3 delims=/ " %%A in ('Date /t') do @( 
    Set Day=%%A
    Set Month=%%B
    Set Year=%%C
)

set "baseName=testing-%Year%%Month%%Day%-"
set "n=0"
:loop
set /a n+=1
if exist "%baseName%%n%.txt" goto :loop
type nul > "%baseName%%n%.txt"
echo "%baseName%%n%" >> teste2.txt was created
pause