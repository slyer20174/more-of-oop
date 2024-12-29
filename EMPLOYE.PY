class employe:
    def __init__(self):
        print("employ created")
    def __del__(self):
        print("employ depleted")
def createobject():
    object=employe()
    return object
print(createobject())