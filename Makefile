clean_pyc:
	@find . -name "*.pyc" -exec rm -rf {} \;

lint:
	@sh scripts/check_lint.sh

pip:
	@pip install -r requirement.txt
