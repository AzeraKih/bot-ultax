# bot-ultax

# para subir como serviço
>`cp ultax.service /etc/systemd/system/`
<Br>
>`systemctl daemon-reload`
<Br>
>`systemctl enable ultax.service`
<Br>
>`systemctl start  ultax.service`
<Br>
>`systemctl status ultax.service`
<Br>
>`service ultax restart && journalctl -u ultax -f`
