
def load_data_from_file_into_list(filename: str):
   
    data_list = []
    current_column = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("COLUMN"):
                current_column = line
                data_list.append(current_column)
            elif line == "END":
                break
            else:
                data_list.append(line)

    return data_list


file_name = "dataset.txt"  
data_list = load_data_from_file_into_list(file_name)
print(data_list)



