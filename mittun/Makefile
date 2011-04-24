clean:
	@echo "Removing trash..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "*.swp" -exec rm -f {} \;
	@echo 'Done!'

tests:
	@echo "Running all tests..."
	@python manage.py test

unit:
	echo "Running unit tests..."
	@python manage.py test unit

functional:
	@echo "Running functional tests..."
	@python manage.py test functional

acceptance:
	@echo "Running acceptance tests..."
	@python manage.py test acceptance

run:
	@python manage.py runserver

shell:
	@python manage.py shell
