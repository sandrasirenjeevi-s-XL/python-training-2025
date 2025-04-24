from pathlib import Path

if Path('file.txt').exists():
    print('file found')

with open('app_logger.log') as f:
    data=f.read()
    print(f.tell())
    f.seek()
    print(f.tell())