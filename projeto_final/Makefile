VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
KERNEL_NAME := projeto-venv
KERNEL_DISPLAY := Python (projeto)

.PHONY: setup install kernel jupyter clean

setup: $(VENV)/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install jupyterlab ipykernel
	$(PYTHON) -m ipykernel install --user \
		--name $(KERNEL_NAME) \
		--display-name "$(KERNEL_DISPLAY)"
	@mkdir data
	@mkdir data/interim
	@mkdir data/processed
	@mkdir data/raw

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

install:
	$(PIP) install -r requirements.txt

kernel:
	$(PIP) install ipykernel
	$(PYTHON) -m ipykernel install --user \
		--name $(KERNEL_NAME) \
		--display-name "$(KERNEL_DISPLAY)"

jupyter:
	$(VENV)/bin/jupyter lab

clean:
	rm -rf $(VENV)
