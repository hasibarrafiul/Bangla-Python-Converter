import sys
with open(str(sys.argv[1])) as f:
    contents = f.read()
    rp = contents.replace("likho", "print")
    rp = rp.replace("jodi", "if")
    rp = rp.replace("othoba", "elif")
    rp = rp.replace("nahoy", "else")
    rp = rp.replace("jotokhonProjonto", "while")
    f = open("runner.py", "w")
    f.write(rp)
    f.close()