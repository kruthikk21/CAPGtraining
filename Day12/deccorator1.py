def log_message(func):
    def wrap(*args,**kwargs):
        res = func(*args,**kwargs)
        with open('/tmp/decorator_logs.txt','w') as f:
            f.write(res)
        return res
    return wrap
    
@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"
    
a_function_that_returns_a_string()
a_function_that_returns_a_string_with_newline("Newline String")
a_function_that_returns_another_string(string="Another String")