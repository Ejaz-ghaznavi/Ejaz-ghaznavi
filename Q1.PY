def load_data_from_file_into_dictionary(filename: str) -> dict:
    with open(filename, 'r') as file:
        data_table = {}
        current_column = None
        for line in file:
            line = line.strip()
            if line.startswith("COLUMN"):
                current_column = line.split(" ", 1)[1]
                data_table[current_column] = []
            elif line == "END":
                break
            else:
                data_table[current_column].append(line)
    return data_table

def output_data_from_dictionary(data_table: dict):
    print("Displaying data from dictionary...")
    for column, values in data_table.items():
        print("=" * 20)
        print(f"{column}")
        print("=" * 20)
        for value in values:
            print(value)

filename = "dataset.txt"  #

data_dict = load_data_from_file_into_dictionary(filename)

if data_dict:
    output_data_from_dictionary(data_dict)



