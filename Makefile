all:
	git pull
	git add Makefile
	git add flask_test
	git add basic
	git add cof
	git add mongo_test
	git commit -m"python study"
	git push origin master

git:
	git pull; \
	cd cof; \
	git pull; \
	git add .; \
	git commit -m"cof framework"; \
	git push origin master
