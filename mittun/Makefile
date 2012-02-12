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

functional: clean
	@python -Wall manage.py test --exclude=acceptance

acceptance: clean
	@python -Wall manage.py acceptance
