@echo off

for %%A IN (*.py) do start /b /wait "" autopep8 --in-place --aggressive --aggressive "%%~fA"