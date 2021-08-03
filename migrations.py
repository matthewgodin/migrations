import sys

if len(sys.argv) == 3 and sys.argv[1] == 'make':
    print("make")
elif len(sys.argv) == 2 and sys.argv[1] == 'migrate':
    print("migrate")
else:
    print("\nUsage:\n\nmigrations.py make <migration-name>\n\nmigrations.py migrate\n")