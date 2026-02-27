#!/bin/bash
# Команда в одну строку для исправления SSH конфигурации

sudo sed -i '/^#*PasswordAuthentication/d' /etc/ssh/sshd_config && echo "PasswordAuthentication yes" | sudo tee -a /etc/ssh/sshd_config && sudo systemctl restart ssh



