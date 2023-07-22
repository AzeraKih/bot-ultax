# bot-ultax

# para subir como serviço
Não esqueça de alterar os caminhos e inserir o token de OAUTH2 no arquivo de serviço!
>`cp ultax.service /etc/systemd/system/`

>`systemctl daemon-reload`

>`systemctl enable ultax.service`

>`systemctl start  ultax.service`

>`systemctl status ultax.service`

>`service ultax restart && journalctl -u ultax -f`
