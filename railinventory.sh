#!/bin/bash


case $1 in
	"run") 
        docker run --restart=always -p 80:80 -d --mount type=bind,source=/var/RailInventory,target=/app/var -it ghcr.io/jonas-luetolf/railinventory:main;;
	
	"init") 
        docker pull ghcr.io/jonas-luetolf/railinventory:main
        
        mkdir /var/RailInventory
		openssl req -newkey rsa:2048 -nodes -keyout /var/RailInventory/key.pem -x509 -days 365 -out /var/RailInventory/certificate.pem
		wget -O /var/RailInventory/.env https://github.com/Jonas-Luetolf/RailInventory/releases/download/v1.1/default.env;;	

    "update")
        docker kill ghcr.io/jonas-luetolf/railinventory:main
        docker pull ghcr.io/jonas-luetolf/railinventory:main
        docker run --restart=always -p 80:80 -d --mount type=bind,source=/var/RailInventory,target=/app/var -it ghcr.io/jonas-luetolf/railinventory:main;;

    esac
