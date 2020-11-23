@echo off
color 2
echo #####Directory wide AutoPEP8 BY Sanam Jena#####
echo Enforcing PEP8 in directory:
echo %CD%
for %%A IN (*.py) do start /b /wait "" autopep8 --in-place --aggressive --aggressive "%%~fA"
echo PEP8 Successfully Enforced
echo Press any key to exit . . .
pause >nul
exit