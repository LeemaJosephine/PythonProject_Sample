def success():
    print("Payment Successful")

def failure():
    print("Payment Failed")

def payment(status, nothing, failure_cb):
    if status == True:
        nothing()
    else:
        failure_cb()

payment(False, success, failure)


def greet(name):
    print("Hello" + name)

def process_user(greet):
    greet("Leema")

process_user(greet)