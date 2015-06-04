#Dynamically imports all files in this directory
import os

MODULES = []

for module in os.listdir(os.path.dirname(__file__)):
	if module == '__init__.py' or module[-3:] != '.py':
		continue

	__import__(module[:-3], locals(), globals())
	MODULES.append(module[:-3])

del module
