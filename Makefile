TARGET_DIR = .

test: ## Run the unit tests
	$(info Running tests...)
	nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service

run: ## Run the service
	$(info Starting service...)
	python3 $(TARGET_DIR)/main.py

.PHONY: test run
