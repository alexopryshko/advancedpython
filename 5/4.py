import inspect
frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

foo()
# The frame was executing the code for 'bar'.
print(frame.f_code.co_name)

# Its back pointer refers to the frame for 'foo'.
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


