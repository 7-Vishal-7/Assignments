filename=input("the filename is:")
dict= {".py":"python",".txt":"text"}
(dict['.py']=="python")
print("python")

filename = input("Input the Filename: ")
f_extns = filename.split(".")
x,y = f_extns
if y=="py":
    print("python")
