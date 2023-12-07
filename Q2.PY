def load_data_from_file_into_list(filename: str) -> list:
    data_table = []
    current_column = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("COLUMN"):
                current_column = line.split(" ")[1]
                data_table.append((current_column, []))
            elif line == "END":
                break
            else:
                data_table[-1][1].append(line)

    return data_table


def output_data_from_list(data_table: list):
    print("Displaying data from list...")
    for column, data in data_table:
        print("=" * 20)
        print(f"{column}")
        print("*" * 20)
        for entry in data:
            print(entry)


file_name = "dataset.txt"  
data_list = load_data_from_file_into_list(file_name)
output_data_from_list(data_list)


#