# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4

def task(inn, out) -> None:
    global indent
    with open(inn) as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]


     # TODO считать содержимое csv файла

    with open(out, 'w') as outfile:
        json.dump(data, outfile, indent=4)


     # TODO Сериализовать в файл с отступами равными 4
if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

