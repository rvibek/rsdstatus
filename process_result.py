#  process and translate the result
#  to be worked

def process(result):
    if result != "No Result":
        result = result.split('\nFor more details click here\n')
    else:
        result = ["No Result", "Retry with correct input"]

    data = {"result": result[0], "explain": result[1]}
    data = {"en" : data}

    return data


# in progress, final result should look like 
"""
{
    "en" : {"result" : "...result text en....", "explain": "...explain text en..."},
    "ar" : {"result" : "...result text ar....", "explain": "...explain text ar..."},
    "or" : {"result" : "...result text or....", "explain": "...explain text or..."},
    "am" : {"result" : "...result text am....", "explain": "...explain text am..."},
    "ti" : {"result" : "...result text ti....", "explain": "...explain text ti..."},
    "so" : {"result" : "...result text so....", "explain": "...explain text so..."}
}

"""

