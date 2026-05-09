from mod import cases, casen

def read_and_write():
    with open("input.txt", "r") as file1:
        with open("output.txt", "w") as file2:
            for text in file1:
                ntext = casen.caseN(text)
                file2.write(ntext)
read_and_write()