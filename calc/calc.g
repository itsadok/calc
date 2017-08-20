%ignore /[ \t]/

program: lines 

?lines: line
      | lines "\n" line

?line: [ statement ] [ _comment ]

_comment: /#[^\n]*/ 

statement: assign
         | assign_plus

assign: identifier "=" sum

assign_plus: identifier "+=" sum

?sum: product
    | sum "+" product         -> add
    | sum "-" product         -> sub

?product: factor
        | product "*" factor  -> mul
        | product "/" factor  -> div

?factor: item
       | "-" factor           -> neg
       | "(" sum ")"

?item: number
     | pre_inc
     | post_inc
     | identifier             -> value

pre_inc: "++" identifier
post_inc: identifier "++"

number: /\d+/
identifier: /[a-zA-Z_]\w*/
