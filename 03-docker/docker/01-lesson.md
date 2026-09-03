# Основы Docker

## Запуск первого контейнера
docker run -d -p 8080:80 --name my_nginx nginx:alpine

##-d – фон

##-p 8080:80 – проброс порта

##--name my_nginx – имя контейнера


#Полезные команды
##docker ps – список работающих контейнеров

##docker ps -a – все контейнеры (включая остановленные)

##docker stop my_nginx – остановить

##docker start my_nginx – запустить остановленный

##docker rm my_nginx – удалить контейнер
