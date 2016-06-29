@ECHO OFF
@SETLOCAL enableextensions enabledelayedexpansion

IF "x%SKIP%"=="x0" (
    ECHO SKIPPING: %*
    GOTO done
)

IF NOT DEFINED CMAKE_GENERATOR ( GOTO visual_studio )
IF NOT "x%CMAKE_GENERATOR:MinGW=%"=="x%CMAKE_GENERATOR%" ( GOTO mingw )

visual_studio:
    SET script=ci\appveyor\run-with-visual-studio.cmd
    GOTO run

mingw:
    SET script=ci\appveyor\run-with-mingw.cmd
    GOTO run

run:
    echo cmd /E:ON /V:ON /C %script% %*
    cmd /E:ON /V:ON /C %script% %*

done:

ENDLOCAL
