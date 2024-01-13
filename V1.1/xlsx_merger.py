"""This is the final 1.1 DF for sql usage later"""

import pandas as pd


string = "example\\string\\to\\extract"
delimiter = "\\"
result = string.split(delimiter)[-1]
print(result)

