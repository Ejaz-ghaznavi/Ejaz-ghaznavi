def load_data_from_file_into_dictionary(filename: str):
   
    data_dictionary = {}
    current_column = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("COLUMN"):
                current_column = line.split(" ")[1]
                data_dictionary[current_column] = []
            elif line == "END":
                break
            else:
                data_dictionary[current_column].append(line)

    return data_dictionary


# Example usage:
file_name = "dataset.txt"  # Replace with the actual file name
data_dict = load_data_from_file_into_dictionary(file_name)
print(data_dict)








