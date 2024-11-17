VENV := .venv

$(VENV):
	python3 -m venv '$(VENV)'
	. '$(VENV)/bin/activate'; pip install matplotlib chainconsumer; pip install git+https://github.com/Anirbancosmo/Limpy.git
	. '$(VENV)/bin/activate'; pip install jupyterlab
