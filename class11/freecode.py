"""
Lua Tutorial for Beginners
=========================

What is Lua?
- Lua is a lightweight scripting language.
- It is often used in game engines, Roblox, Redis, and embedded apps.
- Lua files usually end with .lua

How to run Lua:
1. Install Lua from https://www.lua.org/download.html
2. Save a file like hello.lua
3. Run: lua hello.lua

Simple Lua example:

-- hello.lua
print("Hello, world!")
name = "Alice"
print("Hello, " .. name .. "!")

Basic syntax:

-- This is a Lua comment
print("Hello, Lua!")

Variables:

name = "Alice"
age = 20
isStudent = true

print(name)
print(age)
print(isStudent)

Lua has dynamic typing, so you do not need to declare a variable type.

Numbers:

x = 10
pi = 3.14

print(x + 5)
print(pi * 2)

Strings:

msg = "Hello " .. "World"
print(msg)

The .. operator is used for string concatenation.

Conditionals:

score = 85

if score >= 90 then
    print("Excellent")
elseif score >= 70 then
    print("Good")
else
    print("Try again")
end

Loops:

for i = 1, 5 do
    print(i)
end

while true do
    print("This runs forever")
    break
end

Functions:

function greet(name)
    return "Hello, " .. name .. "!"
end

print(greet("Sam"))

Tables (Lua's main data structure):
- Tables can act like arrays or dictionaries.

arr = {"apple", "banana", "orange"}
print(arr[1])

person = {name = "Ava", age = 16}
print(person.name)
print(person["age"])

Example program:

-- Save as demo.lua and run with: lua demo.lua

local total = 0

for i = 1, 10 do
    total = total + i
end

print("Sum from 1 to 10 is:", total)

Common tips:
- Use local for variables inside functions or blocks when possible.
- Lua uses end to close blocks.
- Functions are declared with function ... end.
- Use tables for objects and arrays.

Mini exercise:
Create a Lua script that asks the user for their name and prints:
"Hello, <name>! Welcome to Lua."

Example answer:

io.write("Enter your name: ")
name = io.read()
print("Hello, " .. name .. "! Welcome to Lua.")

If you want to learn more, practice:
1. Loops
2. Arrays using tables
3. Functions
4. File reading/writing
5. Lua with Roblox or game scripting

"""

print("This file contains a quick Lua tutorial. Open it in VS Code and read the comments.")
