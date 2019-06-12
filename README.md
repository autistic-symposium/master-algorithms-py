##   ✨ Algorithms & Data Structures in Python (Book, Hanbit Media, Inc.)  ✨ 

* Including Python solutions for every exercises from "Cracking the Code Interview".
* #### 📚[Download the digital book here.](https://github.com/bt3gl/Python-and-Algorithms-and-Data-Structures/blob/master/ebook/book_second_edition.pdf)

![](HALEIWA.jpg)


##  ✨ Installation:

The snippets are designed to be used individually. However, If you want  to install all fo the libraries in your [virtualenv](https://coderwall.com/p/8-aeka), do this:

```
$ pip install -r requirements.txt
```

---
## Top Python Interview Questions & Answers

#### What is Python? What are the benefits of using Python?

Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source.


#### What is PEP 8?

PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.


#### What is pickling and unpickling?

Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using a dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.


#### How Python is interpreted?

Python language is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the programmer into an intermediate language, which is again translated into machine language that has to be executed.


#### How memory is managed in Python?

Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap and interpreter takes care of this Python private heap.
The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.
Python also has an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space.


#### What are the tools that help to find bugs or perform static analysis?

PyChecker is a static analysis tool that detects the bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.


#### What are Python decorators?

A Python decorator is a specific change that we make in Python syntax to alter functions easily.

#### What is the difference between list and tuple?

The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.


#### How are arguments passed by value or by reference?

Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result, you cannot change the value of the references. However, you can change the objects if it is mutable.



#### What are the built-in type does python provides?

There are mutable and Immutable types of Pythons built-in types Mutable built-in types

List
Sets
Dictionaries
Immutable built-in types
Strings
Tuples
Numbers


#### What is namespace in Python?

In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get the corresponding object.


#### What is lambda in Python?

It is a single expression anonymous function often used as an inline function.


#### Why lambda forms in python do not have statements?

A lambda form in python does not have statements as it is used to make new function object and then return them at runtime.


#### What is pass in Python?

Pass means, no-operation Python statement, or in other words, it is a place holder in a compound statement, where there should be a blank left and nothing has to be written there.



#### In Python what are iterators?

In Python, iterators are used to iterate a group of elements, containers like list.


#### What is unittest in Python?

A unit testing framework in Python is known as unittest. It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections, etc.


#### In Python what is slicing?

A mechanism to select a range of items from sequence types like list, tuple, strings, etc. is known as slicing.


#### What are generators in Python?

The way of implementing iterators are known as generators. It is a normal function except that it yields expression in the function.


#### What is docstring in Python?

A Python documentation string is known as docstring, it is a way of documenting Python functions, modules and classes.


#### How can you copy an object in Python?

To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.

#### What is the difference between deep and shallow copy?

Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Whereas, a deep copy is used to store the values that are already copied.

#### What is a negative index in Python?

Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index and so forth. For negative index, (-1) is the last index and (-2) is the second last index and so forth.


#### How you can convert a number to a string?

In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().


#### What is the difference between Xrange and range?

Xrange returns the xrange object while range returns the list, and uses the same memory no matter what the range size is.


#### What is module and package in Python?

In Python, a module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.
The folder of Python program is a package of modules. A package can have modules or subfolders.


#### What are the rules for local and global variables in Python?

Local variables: If a variable is assigned a new value anywhere within the function's body, it's assumed to be local.

Global variables: Those variables that are only referenced inside a function are implicitly global.


#### How can you share global variables across modules?

To share global variables across modules within a single program, create a special module. Import the config module in all modules of your application. The module will be available as a global variable across modules.


#### Explain how can you make a Python Script executable on Unix?

To make a Python Script executable on Unix, you need to do two things,

Script file's mode must be executable and
the first line must begin with # (`#!/usr/local/bin/python`).


#### Explain how to delete a file in Python?

By using a command `os.remove (filename)` or `os.unlink(filename)`.


#### Explain how can you generate random numbers in Python?

To generate random numbers in Python, you need to import command as

```
import random
random.random()
```

This returns a random floating point number in the range [0,1)


#### Explain how can you access a module written in Python from C?

You can access a module written in Python from C by following method,

```
Module = =PyImport_ImportModule("<modulename>");
```


#### Mention the use of // operator in Python?

It is a Floor Division operator, which is used for dividing two operands with the result as quotient showing only digits before the decimal point. For instance, `10//5 = 2 and 10.0//5.0 = 2.0`.


#### Explain what is Flask & its benefits?

Flask is a web microframework for Python based on "Werkzeug, Jinja 2 and good intentions" BSD licensed. Werkzeug and jingja are two of its dependencies.

Flask is part of the micro-framework. Which means it will have little to no dependencies on external libraries. It makes the framework light while there is a little dependency to update and fewer security bugs.


#### What is the difference between Django, Pyramid, and Flask?

Flask is a "microframework" primarily build for a small application with simpler requirements. In Flask, you have to use external libraries. Flask is ready to use.

Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.

Like Pyramid, Django can also be used for larger applications. It includes an ORM.


#### Explain how you can access sessions in Flask?

A session basically allows you to remember information from one request to another. In a flask, it uses a signed cookie so the user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.


#### Is Flask an MVC model and if yes give an example showing MVC pattern for your application?

Basically, Flask is a minimalistic framework which behaves the same as MVC framework. So MVC is a perfect fit for Flask, and the pattern for MVC we will consider for the following example:

```python
from flask import Flask

app = Flask(_name_)

@app.route("/")

Def hello():

return "Hello World"

app.run(debug = True)
```

#### Explain database connection in Python Flask?

Flask supports database powered application (RDBS). Such a system requires creating a schema, which requires piping the shema.sql file into a sqlite3 command. So you need to install sqlite3 command in order to create or initiate the database in Flask.

Flask allows requesting database in three ways

* before_request() : They are called before a request and pass no arguments.
* after_request() : They are called after a request and pass the response that will be sent to the client.
* teardown_request(): They are called in a situation when an exception is raised, and response is not guaranteed. They are called after the response been constructed. They are not allowed to modify the request, and their values are ignored.



#### You are having multiple Memcache servers running Python, in which one of the Memcache server fails, and it has your data, will it ever try to get key data from that one failed server?

The data in the failed server won't get removed, but there is a provision for auto-failure, which you can configure for multiple nodes. Fail-over can be triggered during any kind of socket or Memcached server level errors and not during normal client errors like adding an existing key, etc.


#### Explain how you can minimize the Memcached server outages in your Python Development?

When one instance fails, several of them goes down, this will put a larger load on the database server when lost data is reloaded as the client make a request. To avoid this, if your code has been written to minimize cache stampedes then it will leave a minimal impact.

Another way is to bring up an instance of Memcached on a new machine using the lost machines IP address.


#### Explain how Memcached should not be used in your Python project?

Memcached common misuse is to use it as a data store, and not as a cache. Never use Memcached as the only source of the information you need to run your application. Data should always be available through another source as well. Memcached is just a key or value store and cannot perform query over the data or iterate over the contents to extract information. Memcached does not offer any form of security either in encryption or authentication.

#### What's a metaclass in Python?

This type of class holds the instructions about the behind-the-scenes code generation that you want to take place when another piece of code is being executed. With a metaclass, we can define properties that should be added to new classes that are defined in our code.

#### Why isn't all memory freed when Python exits?
Objects referenced from the global namespaces of Python modules are not always deallocated when Python exits. This may happen if there are circular references. There are also certain bits of memory that are allocated by the C library that are impossible to free/ Python is, however, aggressive about cleaning up memory on exit and does try to destroy every single object.

If you want to force Python to delete certain things on deallocation, you can use the atexit module to register one or more exit functions to handle those deletions.

#### Usage of `__slots__`?

The special attribute `__slots__` allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results:

* faster attribute access.
* space savings in memory.

#### What id() function in Python is for?

`id()` function accepts a single parameter and is used to return the identity of an object. This identity has to be unique and constant for this object during the lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.

#### Is Python call-by-value or call-by-reference? 

Neither. In Python, (almost) everything is an object. What we commonly refer to as "variables" in Python are more properly called names. Likewise, "assignment" is really the binding of a name to an object. Each binding has a scope that defines its visibility, usually the block in which the name originates.

In Python a variable is not an alias for a location in memory. Rather, it is simply binding to a Python object.ext post.

----


## License

When making a reference to my work, please use my [website](http://bt3gl.github.io/index.html).

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
