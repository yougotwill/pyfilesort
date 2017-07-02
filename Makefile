default:
	python setup.py develop

clean:
	python setup.py clean
	rm -rf *.egg-info

run:
	python pyfilesort/pyfilesort.py
