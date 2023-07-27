# BASH Scripting: Loops, Conditionals and Parsing

This directory deals with how to:

* Use `while`, `until` and `for` loops
* Use `if`, `else`, `elif` and `case` conditon statements
* Use `cut` command
* Use variable assignment and arithmetic
* Use file test and other comparison operators
* Create `ssh keys`

## Comparison Operators:

* `-a` : AND
* `-o` : OR
* `-n` : NOT
* `-gt` : GREATER THAN
* `-eq` : EQUAL TO
* `-lt` : LESS THAN
* `-ge` : GREATER THAN EQUAL TO
* `-le` : LESS THAN EQUAL TO
* `-ne` : NOT EQUAL TO
* `==` : STRING EQUAL TO
* `!=` : STRING NOT EQUAL TO
* `true`: used in infinite while loops
* `false` : always return a non-zero exit status for a command

## File Test Operators

* `-e file`: Checks if the file exists.
* `-f file`: Checks if the file exists and is a regular file.
* `-d file`: Checks if the file exists and is a directory.
* `-s file`: Checks if the file exists and is not empty (has a size greater than zero).
* `-r file`: Checks if the file exists and is readable.
* `-w file`: Checks if the file exists and is writable.
* `-x file`: Checks if the file exists and is executable.
* `-L file`: Checks if the file exists and is a symbolic link.
* `-h file`: Similar to `-L`, checks if the file exists and is a symbolic link (historical compatibility).
* `-nt file1`: Checks if `file1` is newer than `file`.
* `-ot file1`: Checks if `file1` is older than `file`.
* `-ef file1`: Checks if `file1` and `file` refer to the same file.



## Logical Operators

* `[condition] && [condition]`----------AND
* `[condition] || [condition]`----------OR
* `![condition]`--------------------------NOT

## if/elif/else Structure

```bash
if [[ condition ]];
then
    statement
elif [[ condition ]]; then
    statement
else
	 do this by default
fi
```

## While Loop Structure
```bash
while [condition]
do
    # Code block to be executed repeatedly as long as the condition is true
    # You can have multiple commands or statements here
done
```

## Until Loop Structure
```bash
until [condition]
do
    # Code block to be executed repeatedly until the condition becomes true
    # You can have multiple commands or statements here
done
```

## For Loop Structure
```bash
for variable in [list]
do
    # Code block to be executed for each item in the list
    # You can have multiple commands or statements here
done
```
