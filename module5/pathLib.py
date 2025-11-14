from pathlib import Path

p = Path('/home/vikas.kumar/Documents/python-devops/module5')

for file in p.iterdir():
    print(file)