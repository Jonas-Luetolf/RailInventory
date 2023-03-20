#!/bin/bash



case $1 in
	"run") docker run -p 443:443 -d --mount type=bind,source=/var/RailInventory,target=/app/var -it ghcr.io/jonas-luetolf/railinventory:main;;
	
	"init") 
        docker pull ghcr.io/jonas-luetolf/railinventory:main
        mkdir /var/RailInventory
		openssl req -newkey rsa:2048 -nodes -keyout /var/RailInventory/key.pem -x509 -days 365 -out /var/RailInventory/certificate.pem
		wget -O /var/RailInventory/.env https://github.com/Jonas-Luetolf/RailInventory/releases/download/v0.0.1/default.env;;	
	esac
