# A simple calculator with variable support

Based on [Lark](https://github.com/erezsh/lark), this is a simple calculator grammar and matching implementation.

## To use

You need [pipenv](http://pipenv.org/) to install the dependency, or just `pip install lark-parser`.

```shell
$ sudo pip install pipenv
$ git clone https://github.com/itsadok/calc && cd calc
$ pipenv --three install 
$ pipenv shell
$ python test_calc.py
................
----------------------------------------------------------------------
Ran 16 tests in 0.022s

OK
$ python calc/calc.py <<END
	i = 0
	j = ++i
	x = i++ + 5
	y = 5 + 3 * 10
	i += y
END
(i=37,j=1,x=6,y=35)
$
```

# Author

Israel Tsadok. Code license - [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
