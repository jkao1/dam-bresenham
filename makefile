run: main.py
	python main.py
	convert foo.ppm foo.png

clean:
	rm *.pyc
	rm *~
