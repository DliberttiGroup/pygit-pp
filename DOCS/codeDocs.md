# Welcome to the official Code Docs of pygit++


# Section

**What is a section in pygit++?**

Since this is CLI tool it uses ```argparser``` module to
work the arguments that are passed from the command line.


A since this commands most be handled with an if statement
you will end up with something like this 

```python
if this:
    do_this()

if this2:
    do_this_but_like_this():

if this_is_not:
    do_that()
```

so in order to keep in order to keep the main file 
organized the code was divided into section each section 
being on charge to do one main thing.

**How do I make a section?**

Let's say that you have a new implementation for pygit++
so your fork the repo and clone your fork and you start 
working on it.

The first thing you should do it's make your section for your
command for this example let's say that are implementing the
```foo``` command.

So you open the main file go to the end of the file and 
add your section like this.

```python

"""
Section:
foo command
"""



"""
End Section:
foo command
"""
```

and just like this you have implemented your first section.


> [!NOTE]
>
> A section does not have to be about only one command
> it can be a bunch of minor commands implementations
> as long as they keep the context of the section


> [!TIP]
>
> You can add a little note into the section comment.
> This is so if the name of your section is to ambiguous.


> [!TIP]
>
> Always try to keep your section on context:
>
> This means if you are implementing the foo command
> try to just implement that in your section


# Functions

**General things about functions:**

Use static typed for argument and specify return type

❌ Say not to:

```python
def do_something_amazing(data, data_2, data_3):
    return 5
```

✅ Say yes to:

```python
def do_something_amazing(data: dict[str, int], data_2: int, data_3, str) -> int:
    return 5
```


Use descriptive names so no comments are necessary


❌ Say not to:

```python
def number_2(data):
    """
    gets the second item of the list provided
    """
```

✅ Say yes to:

```python
def get_which_item_is_second(data: list[int]) -> int:
```


Try only have max 79 characters per line


❌ Say not to:

```python
this_is_really_really_long_but_really_long_function(data1: str, data2: list[str], data3: int) -> None:
```

✅ Say yes to:

```python
this_is_really_really_long_but_really_long_function(
                                                    data1: str, 
                                                    data2: list[str], 
                                                    data3: int
                                                   ) -> None:
```


And finally always try to use general good code practices.


**How does a function looks like in pygit++?**

As you remember from the ```Sections``` part ```argparser```
only call one function based off the argument was passed
this means that essentially each section contains only
one giant function (or a bunch of them depending what is your
section about)

However is not a good practice to only have one big function
doing all the work so to solve this, the 'giant' function was
broke into two parts ```Main Functions``` and ```Sub Functions```


When writing code your section most contain at least one 
```Main Function``` that will be the one called by the ```argparser```
if statement.

**A real example:**

```python
if self.args.foo:
    self.do_my_amazing_foo_command()


"""
Section:
foo command
"""

def do_my_amazing_foo_command(self) -> None:
    """
    Main Function
    """
    interger = 1
    print("foo command called!")
    self.get_data(integer)

def get_data(self, argument: int) -> None:
    """
    Sub-Function of:
    do_my_amazing_foo_command
    """
    print("Get data was called")
    print(f"Interger is {integer}")
    self.get_data2()

def get_data2():
    """
    Sub-Function of:
    get_data
    """
    print("get data two was called")

    

"""
End Section:
foo command
"""
```

Some things to noticed:

- You can have a Sub Function being used as a Sub Function 
of another Sub Function this is so to increase modularity 
of the code.


# Comments

**What should a comment include?**
If you followed the previous recommendations, the only 
thing you should include in your comments is whether 
your function is a Main function or a Sub Function. 
However, you can also add brief notes or other general 
code comments.

# How to navigate the main file

The easier way to navigate the main code file is by going
to the ```setup argparser``` section, and in there look
for the ```handle_args``` function there you can look for the main
function that are being called, once you found the argument
you are looking for you can look for that main function
in NeoVim you can use 

```
/[name_of_the_main_function]
```

this will take you to the desired main function and its section.


# Existing sections

- **Total:** 8

- Section: init pygit++
- Section: Manual
- Section: Argparser
- Section: Display info from current repo
- Section: Commit Work 
- Section: Add files to index
- Section: Git work
- Section: Setup



# Working the internal modules & Internal APIs


Docs coming soon
