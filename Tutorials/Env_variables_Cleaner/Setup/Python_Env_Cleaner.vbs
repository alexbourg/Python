'## Application Name: Python Cleaner
'## Created Date: 16.05.2021
'## Created By: Alex BOURG

'## Description: This script will clean python silently

'========================================================================
'## Global Object and Variable Settings
'======================================================================== 
'Option Explicit

Dim WshShell:	Set WshShell = CreateObject("WScript.Shell")
Dim objFSO:	Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim SourceDir:	SourceDir = Replace(WScript.ScriptFullName,WScript.ScriptName,"")
Dim value
WshShell.CurrentDirectory = SourceDir

DIM Subfolder
Dim command
'========================================================================
'## Global Object and Variable Settings
'======================================================================== 
On error resume next
wshshell.run "cmd /C ""C:\Users\usr64\Desktop\x\Python_Env_Cleaner.exe"" /kill_python /clean_old_dir /clean_all_env /clean_path_env /clean_path_ext",0,true
Set WshShell = Nothing