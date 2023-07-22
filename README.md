# bot-ultax

# para subir como serviço
>`cp ultax.service /etc/systemd/system/`

>`systemctl daemon-reload`

>`systemctl enable ultax.service`

>`systemctl start  ultax.service`

>`systemctl status ultax.service`

>`service ultax restart && journalctl -u ultax -f`
