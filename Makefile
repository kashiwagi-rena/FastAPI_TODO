image:
	docker-compose build --no-cache

up:
	docker compose up
build:
	docker compose build --no-cache
# MySQLのコンテナをpull
mysql:
	docker run --name mysqldb -e MYSQL_DATABASE=test -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql:latest
#　Dockerが立ち上がっているか確認するコマンド
ps:
	docker ps