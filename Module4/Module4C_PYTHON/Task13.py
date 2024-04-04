def salute(counter):
    
    if counter == 0:
        return
    print("Hello World")
    salute(counter - 1)

salute(3)