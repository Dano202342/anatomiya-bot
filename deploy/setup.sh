#!/usr/bin/env bash
# Anatomiya botini Ubuntu/Debian serverga o'rnatadi va 24/7 ishlatadi.
# Ishlatish (root sifatida, bot fayllari /opt/anatomiya da turgan holda):
#   bash /opt/anatomiya/deploy/setup.sh
set -euo pipefail

APP=/opt/anatomiya
IP=$(curl -4 -s https://api.ipify.org)
DOMAIN="${DOMAIN:-${IP//./-}.sslip.io}"   # domen bo'lmasa: 1-2-3-4.sslip.io → server IP siga yo'naltiriladi

echo "==> Paketlar o'rnatilmoqda"
export DEBIAN_FRONTEND=noninteractive
apt-get update -q
apt-get install -y -q python3 python3-venv python3-pip curl debian-keyring debian-archive-keyring apt-transport-https gnupg

if ! command -v caddy >/dev/null; then
  echo "==> Caddy (avtomatik HTTPS) o'rnatilmoqda"
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' > /etc/apt/sources.list.d/caddy-stable.list
  apt-get update -q && apt-get install -y -q caddy
fi

echo "==> Python muhiti"
id anatomiya >/dev/null 2>&1 || useradd --system --home "$APP" --shell /usr/sbin/nologin anatomiya
python3 -m venv "$APP/.venv"
"$APP/.venv/bin/pip" install -q --upgrade pip
"$APP/.venv/bin/pip" install -q -r "$APP/requirements.txt"

echo "==> .env sozlanmoqda (WEBAPP_URL=https://$DOMAIN)"
grep -q '^WEBAPP_URL=' "$APP/.env" && sed -i "s|^WEBAPP_URL=.*|WEBAPP_URL=https://$DOMAIN|" "$APP/.env" \
  || echo "WEBAPP_URL=https://$DOMAIN" >> "$APP/.env"
chown -R anatomiya:anatomiya "$APP"
chmod 600 "$APP/.env"

echo "==> Caddy: https://$DOMAIN → bot ichidagi 3D ko'ruvchi"
cat > /etc/caddy/Caddyfile <<EOF
$DOMAIN {
    encode gzip
    reverse_proxy 127.0.0.1:8088
}
EOF
systemctl enable caddy >/dev/null
systemctl restart caddy

echo "==> systemd xizmati (avtomatik ishga tushish va qayta ishga tushish)"
cat > /etc/systemd/system/anatomiya.service <<EOF
[Unit]
Description=Anatomiya Telegram bot
After=network-online.target
Wants=network-online.target

[Service]
User=anatomiya
WorkingDirectory=$APP
ExecStart=$APP/.venv/bin/python -u bot.py
Restart=always
RestartSec=5
Environment=PYTHONIOENCODING=utf-8

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable anatomiya >/dev/null
systemctl restart anatomiya

if command -v ufw >/dev/null && ufw status | grep -q active; then
  ufw allow 80/tcp; ufw allow 443/tcp
fi

echo "==> Media fonda yuklanmoqda (3D animatsiyalar serverga)"
runuser -u anatomiya -- nohup "$APP/.venv/bin/python" "$APP/resolve_media.py" --download > "$APP/data/download.log" 2>&1 &

sleep 5
systemctl --no-pager --lines=5 status anatomiya || true
echo
echo "✅ Tayyor! Bot 24/7 ishlaydi. 3D ko'ruvchi: https://$DOMAIN"
echo "   Loglar:  journalctl -u anatomiya -f"
