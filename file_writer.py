import sys


class FileWriter:
    def __init__(self, filepath="./lines.txt") -> None:
        self.filepath = filepath

    def write(self, line, line_number):
        outfile = open(self.filepath, 'a')

        outfile.write(f"{line_number:03}")
        outfile.write(" = ")
        outfile.write(line)
        outfile.close()


if __name__ == "__main__":
    writer = FileWriter()

    last_is_blank = False
    line_number = 0

    for line in sys.stdin:
        line_number += 1

        if line == "\n":
            if last_is_blank:
                break
            else:
                last_is_blank = True
        
        writer.write(line, line_number)
