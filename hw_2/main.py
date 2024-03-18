import sys
from generate_latex import generation_table, generation_picture, generation_document


def main():
    data = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        data.append(line.split(" "))

    table = generation_table(data)
    with open("./artifacts/table.tex", "w") as file:
        file.write(generation_document(table))

    picture = generation_picture("./data/forest.png")
    with open("./artifacts/table_and_picture.tex", "w") as file:
        file.write(generation_document(table + picture))


if __name__ == '__main__':
    main()
