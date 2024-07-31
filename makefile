make-docker-image:
	docker build -t myimage .

run-docker-image:
	docker run -d --name mycontainer -p 80:80 myimage

docker-down-container:
	docker rm container

down-docker-image:
	docker rmi myimage

install-packages:
	 pip3 install -r requirements.txt

freeze-requirements:
	pip freeze > requirements.txt