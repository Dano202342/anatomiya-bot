# Botni serverga yuklaydi va o'rnatadi.
# Ishlatish:  powershell -File deploy\deploy.ps1 -Server 1.2.3.4
param(
    [Parameter(Mandatory = $true)][string]$Server,
    [string]$User = "root",
    [string]$Key = "$env:USERPROFILE\.ssh\anatomiya_vps"
)
$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$ssh = @("-i", $Key, "-o", "StrictHostKeyChecking=accept-new")

# Yuklanadigan fayllar (media/ ni server o'zi yuklab oladi — tezroq)
$tmp = Join-Path $env:TEMP "anatomiya_deploy.tar"
Push-Location $root
tar -cf $tmp bot.py media.py webserver.py resolve_media.py requirements.txt .env content webapp deploy data/media.json data/commons_anims.json data/file_ids.json
Pop-Location

ssh @ssh "$User@$Server" "mkdir -p /opt/anatomiya/data"
scp @ssh $tmp "${User}@${Server}:/tmp/anatomiya.tar"
ssh @ssh "$User@$Server" "tar -xf /tmp/anatomiya.tar -C /opt/anatomiya && sed -i 's/\r$//' /opt/anatomiya/deploy/setup.sh && bash /opt/anatomiya/deploy/setup.sh"
Remove-Item $tmp
