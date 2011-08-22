dependencies:
	@pip install -r ../requirements.txt

clean:
	@echo "Removing trash..."
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@echo 'Done!'

tests: clean
	@echo "Running all tests..."
	@python -Wall manage.py test

unit: clean
	@echo "Running unit tests..."
	@python -Wall manage.py test unit

functional: clean
	@echo "Running functional tests..."
	@python -Wall manage.py test functional

acceptance: clean
	@echo "Running acceptance tests..."
	@python -Wall manage.py test acceptance

run:
	@python manage.py runserver

shell:
	@python manage.py shell
