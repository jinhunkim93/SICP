from operator import add

######################################
#             Values                 #
######################################

# Values - programs manipulate values
# Each Value has a certain data type
"""
Data Type   | Example Values
Integers    |  1 24 -5
Floats      |  3.14  -1.0
Booleans    |  True  False
Strings     |  'a' 'yolo'
"""
# print() - print(3), print('hi'), print(1+2), ...
3
'a'
'Hello'

######################################
#            Expressions             #
######################################

# Expressions - expressions evaluate to values
# 1) Operator Expressions: +, -, ...
1 + 2    # 3
'yo' + 'lo'    # 'yolo'
# 2) Function Call Expressions: min, max, pow ...
# Call Expression:
"""
  min     (    1    ,     6    )
operator    operand    operand
1. Evaluate the Operator
2. Evaluate the Operands
3. Apply the Operator to the evaluated Operands
"""
min(1, 3)
max(1, 3)
pow(2, 3)
# min, max, pow are built-in but there are others such as add from the operator module from the Python standard library
# from operator import add
12 + 12 == add(12, 12)
# Evaluating Nested Expressions
"""
add(1,add(min(2,3), add(1,2)))
 |
add

add ( 1 , add(min(2,3), add(1,2)))
 |    |
add   |
      1

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |
          add

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |     |
          add    |
              min(2,3)
              
add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |     |
          add    |
              min(2,3)
               |
              min
              
add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |     |
          add    |
              min( 2, 3 )
               |   |
              min  2
              
add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |     |
          add    |
              min( 2, 3 )
               |   |  |
              min  2  3
              
add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add(1,2))
           |     |
          add    |
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) 
            |     |          |
            |     |     add( 1, 2 )
            |     |      |
           add    |     add
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) 
            |     |          |
            |     |      add( 1, 2 )
            |     |       |
           add    |      add
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) 
            |     |          |
            |     |      add( 1, 2 )
            |     |       |   |
           add    |      add  1 
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) 
            |     |          |
            |     |      add( 1, 2 )
            |     |       |   |  |
           add    |      add  1  2
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) 
            |     |          |
            |     |      add( 1, 2 ) = 3
            |     |       |   |  |
           add    |      add  1  2
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2)))
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) = 5
            |     |          |
            |     |      add( 1, 2 ) = 3
            |     |       |   |  |
           add    |      add  1  2
              min( 2, 3 ) = 2
               |   |  |
              min  2  3

add ( 1 , add(min(2,3), add(1,2))) = 6
 |    |             |
add   |             |
      1             |
          add(min(2,3), add( 1, 2 )) = 5
            |     |          |
            |     |      add( 1, 2 ) = 3
            |     |       |   |  |
           add    |      add  1  2
              min( 2, 3 ) = 2
               |   |  |
              min  2  3
"""
add(1,add(min(2,3), add(1,2))) # 6

######################################
#               Names                #
######################################

# Names - can be bound to a value
# A name that's bound to a data value is also known as a Variable
# Assignment Statement
"""
  x   =    6
 Name    Value

  x   =    2 + 3 * 4
 Name      Expression
"""
a = 1
b = 2
# Name Rebinding
a = 3
b = b + 2 # 4
# b = b + 2 is equivalent to b += 2

######################################
#             Function               #
######################################

# A function is a sequence of code that performs a particular task and can be easily reused
"""
        input        ->   task   -> output
arguments/parameters -> function -> return Value

Function Definition:

def <name>(<parameters>):           # function signature
    return <return expression>      # function body

def sum(a, b):
    return a + b

sum(1,2) # 3

"""
