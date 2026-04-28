# Instalar OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Iniciar servicio
Start-Service sshd

# Hacerlo persistente (arranque automático)
Set-Service -Name sshd -StartupType Automatic

# (Opcional) permitir en firewall
New-NetFirewallRule -Name sshd `
  -DisplayName "OpenSSH Server (sshd)" `
  -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

# Verificar estado
Get-Service sshd
