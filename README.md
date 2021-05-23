# Configuración del entorno de desarrollo

## Creación del puente de red
Para el correcto funcionamiento del escáner de red, es necesario que el entorno de desarrollo esté en la misma subred que el resto de nodos. Para ello, se crea un puente de red con el siguiente comando:

```powershell
docker network create -d bridge --subnet 192.168.1.0/24 --gateway 192.168.1.1 bridge-redes
```

En el comando anterior se ha indicado la puerta de enlace de por defecto y la máscara subred.

| Variable    | Valor                       |
|-------------|-----------------------------|
| IP Address  | 192.168.1.0                 |
| Subnet Mask | 255.255.255.0 (24)          |
| Network     | 192.168.1.0/24              |
| Broadcast   | 192.168.1.255               |
| Range       | 192.168.1.1 - 192.168.0.254 |
| Tipo        | Privada                     |

## Creación de la imagen
En esta sección se va a crear la imagen con la que se trabajará. Esta imágen utilizará una imágen proporcionada por *Ubuntu*.

La especificación de esta se encuentra en el fichero `Dockerfile`.

```powershell
docker build -t ubuntu .
```

## Ejecución del entorno de desarrollo
Una vez creada la instancia, se ejecutará el entorno. Cabe destacar, que para la correcta conexión a la red, es necesario indicar lo siguiente:
* Dirección IP
* Adaptador de red

```powershell
docker run -it --name ubuntu-redes --network=bridge-redes --ip 192.168.1.45 -h ubuntu -v C:/Users/ferna/Desktop/redes:/home/redes ubuntu
```
