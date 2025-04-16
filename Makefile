venv:
	python -m venv .venv
	./venv/bin/pip install --upgrade pip django
	./venv/bin/pip install -r requirements.txt
	