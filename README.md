# Pasos a seguir para ejecutar esta app Con docker

## Esto es mas que todo para generar el contenedor crear las imagenes y todos los procesos de docker

docker build -t med_manager_api .

## Aqui ejecutamos el contenedor y publicamos la app en el puerto

docker run -it --publish 7000:4000 -d med_manager_api
