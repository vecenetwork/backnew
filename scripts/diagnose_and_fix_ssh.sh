#!/bin/bash
# Полная диагностика и исправление SSH для входа по паролю

echo "=== Диагностика SSH конфигурации ==="
echo ""
echo "1. Проверяю текущие настройки PasswordAuthentication:"
sudo grep -i "PasswordAuthentication" /etc/ssh/sshd_config

echo ""
echo "2. Проверяю настройки ChallengeResponseAuthentication:"
sudo grep -i "ChallengeResponseAuthentication" /etc/ssh/sshd_config

echo ""
echo "3. Проверяю настройки UsePAM:"
sudo grep -i "UsePAM" /etc/ssh/sshd_config

echo ""
echo "4. Проверяю, существует ли пользователь vece:"
id vece

echo ""
echo "=== Исправление конфигурации ==="

# Создаем резервную копию
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d_%H%M%S)

# Удаляем все строки с PasswordAuthentication
sudo sed -i '/^#*PasswordAuthentication/d' /etc/ssh/sshd_config

# Удаляем все строки с ChallengeResponseAuthentication
sudo sed -i '/^#*ChallengeResponseAuthentication/d' /etc/ssh/sshd_config

# Удаляем все строки с UsePAM
sudo sed -i '/^#*UsePAM/d' /etc/ssh/sshd_config

# Добавляем правильные настройки в конец файла
cat << EOF | sudo tee -a /etc/ssh/sshd_config

# Password authentication settings
PasswordAuthentication yes
ChallengeResponseAuthentication yes
UsePAM yes
EOF

echo ""
echo "=== Новая конфигурация ==="
sudo grep -E "(PasswordAuthentication|ChallengeResponseAuthentication|UsePAM)" /etc/ssh/sshd_config

echo ""
echo "=== Проверка синтаксиса конфигурации ==="
sudo sshd -t

if [ $? -eq 0 ]; then
    echo "Синтаксис конфигурации правильный!"
    echo ""
    echo "Перезапускаю SSH сервис..."
    sudo systemctl restart ssh 2>/dev/null || sudo systemctl restart sshd 2>/dev/null || sudo service ssh restart 2>/dev/null || sudo service sshd restart 2>/dev/null
    
    echo ""
    echo "=== Статус SSH сервиса ==="
    sudo systemctl status ssh 2>/dev/null | head -10 || sudo systemctl status sshd 2>/dev/null | head -10
    
    echo ""
    echo "=== Готово! ==="
    echo "Попробуйте подключиться: ssh vece@54.158.9.158"
    echo ""
    echo "Если не работает, проверьте:"
    echo "1. Пароль установлен: sudo passwd vece"
    echo "2. Пользователь может войти локально"
    echo "3. Файрвол не блокирует SSH (порт 22)"
else
    echo "ОШИБКА: Синтаксис конфигурации неправильный!"
    echo "Восстанавливаю резервную копию..."
    sudo cp /etc/ssh/sshd_config.backup.* /etc/ssh/sshd_config
fi



