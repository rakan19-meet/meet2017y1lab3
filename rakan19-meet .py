Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "don't"+"forget"+"to"+"conserve"+"waterr"
"don'tforgettoconservewaterr"
>>> 'don't+'forget'+'to'+'conserve'+'water'
SyntaxError: invalid syntax
>>> 'don't+'forget'+'to'+'conserve'+'water'
SyntaxError: invalid syntax
>>> "the"*#
SyntaxError: invalid syntax
>>> "the"*3
'thethethe'
>>> 'the'+3
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    'the'+3
TypeError: Can't convert 'int' object to str implicitly
>>> the"*3 + "beautiful" + "Earth"
SyntaxError: invalid syntax
>>> 2*"True"
'TrueTrue'
>>> a = 'save'
>>> ​ b = 'the'
SyntaxError: invalid character in identifier
>>> ​ b = 'the'
SyntaxError: invalid character in identifier
>>> b='the'
>>> c = 'planet'
>>> print('a ' + 'b '+ 'c')
a b c
>>> a+b+c
'savetheplanet'
>>> len(20)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len(20)
TypeError: object of type 'int' has no len()
>>> t = "rakan"
>>> t
'rakan'
>>> len(t)
5
>>> len(t * 1000)
5000
>>> test="i love meeet"
>>> len(test)
12
>>> a="MEET"
>>> b="meet"
>>> c="Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a!=b
True
>>> a!=c
True
>>> b!=c
True
>>> name = "rakan"
>>> student2 = "rakan"
>>> name == student2
True
>>> (erakan)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    (erakan)
NameError: name 'erakan' is not defined
>>> rakan=1
>>> (rakan)
1
>>> a=2
>>> b=3
>>> a==b
False
>>> a!=b
True
>>> my_string="thinkBIG"
>>> meet_value="alexadamfarahkatamir"
>>> len(my_value)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    len(my_value)
NameError: name 'my_value' is not defined
>>> len(my_string)
8
>>> meet_value[0:8]
'alexadam'
>>> meet_value
'alexadamfarahkatamir'
>>> meet_value='alexadam'
>>> len(meet_value)
8
>>> meet_value==my_string
False
>>> len(meet_value)==len(my_string)
True
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = 'bananayellowthinkhatgreyBIGcalifornia314'
>>> meet_value=my_string'[12:17]
SyntaxError: EOL while scanning string literal
>>> meet_value=my_string[12;17]
SyntaxError: invalid syntax
>>> meet_value=my_string[12:17]
>>> meet_value
'think'
>>> meet_value=my_string[12:17] + my_string[24:27]
>>> meet_value
'thinkBIG'
>>> meet_value="thinkBIG"+" "
>>> meet_value
'thinkBIG '
>>> meet_value="THINK BIG"
>>> meet_value
'THINK BIG'
>>> meet_value.swapcase()
'think big'
>>> meet_value.swapcase()
'think big'
>>> 
