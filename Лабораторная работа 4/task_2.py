import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []

    with open(INPUT_FILENAME) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            data.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
