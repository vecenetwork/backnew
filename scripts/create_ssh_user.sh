#!/bin/bash
# Скрипт для создания пользователя vece с SSH доступом по паролю
# Запускать на сервере с правами root/sudo

USERNAME="vece"

# Создаем пользователя
sudo useradd -m -s /bin/bash $USERNAME

# Устанавливаем пароль (замените на свой)
echo "$USERNAME:your_secure_password" | sudo chpasswd

# Добавляем в группу sudo (если нужны права администратора)
sudo usermod -aG sudo $USERNAME

# Включаем аутентификацию по паролю в SSH (если отключена)
sudo sed -i 's/#PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Перезапускаем SSH сервис
sudo systemctl restart sshd

echo "Пользователь $USERNAME создан!"
echo "Теперь можно подключиться: ssh $USERNAME@54.158.9.158"

