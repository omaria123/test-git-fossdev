install-all:
	cd product_service && make install
	cd discount_service && make install
	cd order_service && make install

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

clean-all:
	cd product_service && make clean
	cd discount_service && make clean
	cd order_service && make clean