@echo off
rmdir dist /S /Q
python setup.py sdist bdist_wheel
python -m twine upload dist/*
pause
exit