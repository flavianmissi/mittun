dependencies:
	@pip install -r ../requirements.txt

clean:
	@echo "Removing trash..."
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@echo 'Done!'

tests: clean
	@echo "Running all tests..."
	@python -Wall manage.py test -v 2

functional: clean
	@python -Wall manage.py test --exclude=acceptance -v 2

unit: clean
	@python -Wall manage.py test --exclude=acceptance --exclude=functional -v 2
