# Lab 1 - Implementation of Lexical Analyzer

## Aim
To implement a lexical analyzer that identifies tokens such as keywords, identifiers, operators, constants, and delimiters.

## Algorithm
1. Start the program
2. Define sets of keywords, operators, and delimiters
3. Read the input source code
4. Split the input into words (tokens)
5. For each word:
   - Check if it is a keyword
   - Else if operator
   - Else if delimiter
   - Else if numeric constant
   - Else if identifier
   - Else mark as unknown
6. Display the token type
7. Stop the program

## Program
(Refer to code.py)

## Input
int a = 5 ;

## Output
int -> Keyword  
a -> Identifier  
= -> Operator  
5 -> Constant  
; -> Delimiter  

## Result
Thus, the lexical analyzer is implemented successfully.
