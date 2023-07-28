## 1. Basic file opening and reading

```
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
finally:
    file.close()
```

## 2. Using with statement for file handling

```
with open('example.txt', 'r') as file:
    print(file.read())
```

## 3. Writing to a file

```
with open('example.txt', 'w') as file:
    file.write("Hello, Pythonista!")
```

## 4. Reading a specific number of characters

```
with open('example.txt', 'r') as file:
    print(file.read(5))
```

## 5. Reading one line at a time using readline

```
with open('example.txt', 'r') as file:
    print(file.readline())
```

## 6. Reading all lines at once using readlines

with open('example.txt', 'r') as file:
print(file.readlines())

## 7. Looping over a file object

```
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

## 8. Looping over a file object

```
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

## 9. Writing multiple lines to a file

```
lines = ["Hello, Pythonista!\n", "Welcome to the world of Python.\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## 10. Appending to a file

```
with open('example.txt', 'a') as file:
    file.write("\nKeep on learning!")
```

## 11. Checking if a file exists

```
import os
print(os.path.isfile('example.txt'))
```

## 12. Renaming a file

```
import os
os.rename('example.txt', 'new_example.txt')
```

## 13. Removing a file

```
import os
os.remove('new_example.txt')
```

## 14. Changing the current working directory

```
import os
os.chdir('newDirectory')
```

## 15. Getting the current working directory

```
import os
os.chdir('newDirectory')
print(os.getcwd())
```

## 16. Removing a directory

```
import os
os.rmdir('newDirectory')
```

## 17. Listing all files and directories

```
import os
print(os.listdir())
```
