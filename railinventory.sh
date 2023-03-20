#!/bin/bash



case $1 in
	"run") docker run -p 443:443 -d --mount type=bind,source=/var/RailInventory,target=/app/var -it railinventory;;
	
	"init") 
        docker pull ghcr.io/jonas-luetolf/railinventory:main
        mkdir /var/RailInventory
		openssl req -newkey rsa:2048 -nodes -keyout /var/RailInventory/key.pem -x509 -days 365 -out /var/RailInventory/certificate.pem
		cp var/.env /var/RailInventory/.env;;		
	esac
