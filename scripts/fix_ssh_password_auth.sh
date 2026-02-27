#!/bin/bash
# Полное исправление SSH для работы с паролем

echo "Исправляю конфигурацию SSH..."

# Удаляем все настройки аутентификации
sudo sed -i '/^#*PasswordAuthentication/d' /etc/ssh/sshd_config
sudo sed -i '/^#*ChallengeResponseAuthentication/d' /etc/ssh/sshd_config
sudo sed -i '/^#*AuthenticationMethods/d' /etc/ssh/sshd_config

# Добавляем правильные настройки
cat << EOF | sudo tee -a /etc/ssh/sshd_config

# Enable password authentication
PasswordAuthentication yes
ChallengeResponseAuthentication yes
EOF

# Проверяем синтаксис
echo ""
echo "Проверка синтаксиса:"
sudo sshd -t

if [ $? -eq 0 ]; then
    echo "Синтаксис правильный, перезапускаю SSH..."
    sudo systemctl restart ssh
    echo ""
    echo "Проверяю настройки:"
    sudo grep -E "^(PasswordAuthentication|ChallengeResponseAuthentication)" /etc/ssh/sshd_config
    echo ""
    echo "Готово! Попробуйте подключиться: ssh vece@54.158.9.158"
else
    echo "ОШИБКА в конфигурации!"
fi



