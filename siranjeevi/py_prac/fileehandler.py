from pathlib import Path
if Path('app_logger.log').exists():
    print('file found')

# with open('app_logger.log') as f:
#     data=f.read()
#     print(f.tell()) #3498 bytes upto  cursor
#     f.seek(5)
