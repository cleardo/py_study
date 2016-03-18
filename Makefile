SVN_DIR=Makefile

all:
	git add $(SVN_DIR)
	git commit $(SVN_DIR) -m"python study"
	git push origin master

up:
	cd cof; \
	git pull

git:
	cd cof; \
	make git

git2:
	git pull; \
	cd cof; \
	git pull; \
	git add .; \
	git commit -m"cof framework"; \
	git push origin master
