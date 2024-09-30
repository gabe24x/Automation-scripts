VENV ?= .venv
REQUIREMENTS_FILE ?= requirements.txt

init:
	# Install tkinter (python3-tk) if on a Debian-based system (e.g., WSL, Ubuntu)
	@echo "Checking for tkinter (python3-tk)..."
	if command -v apt-get > /dev/null; then \
		sudo apt-get update && sudo apt-get install -y python3-tk || true; \
	fi
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip setuptools wheel
	if [ -f $(REQUIREMENTS_FILE) ]; then \
		$(VENV)/bin/python -m pip install -r $(REQUIREMENTS_FILE); \
	fi

run:
	$(VENV)/bin/python weather_notifier.py

clean:
	rm -rf $(VENV)
