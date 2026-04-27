from mod import cases


def read_and_write():
    with open("input.txt", "r") as file1:
        with open("output.txt", "w") as file2:
            for text in file1:
                ntext = cases.cases(text)
                file2.write(ntext)
read_and_write()