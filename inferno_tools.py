import os, inferno_var


def run():
    try:
        from inpy import input as n
        import cockroach
        import tikcheck
        import notify
    except ImportError:
        print("You don't have one of our libraries. Do you want to install these libraries on your device to continue? (y/n)")
        response = input("—> ").lower()

        if response == "y":
            l = 0
            while l < len(inferno_var.libs):
                os.system(f"pip install git+https://github.com/Inferno-God1001/{inferno_var.libs[l]}.git")
                l += 1
            from inpy import input    
        else:
            exit()
    
            
                

    
