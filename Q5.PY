def output_total_mean_median(data_table, total_column_name: str):
   
    try:
        # Check if data_table is a list
        if isinstance(data_table, list):
            column_index = data_table.index(f"COLUMN {total_column_name}")
            column_data = [int(value) for value in data_table[column_index + 1:]]

        # Check if data_table is a dictionary
        elif isinstance(data_table, dict):
            column_data = [int(value) for value in data_table[total_column_name]]

        else:
            print("Invalid data structure. Please provide a list or a dictionary.")
            return

        # Calculate total, mean, and median
        total = sum(column_data)
        mean = total / len(column_data)
        sorted_data = sorted(column_data)
        mid = len(sorted_data) // 2
        median = (sorted_data[mid] + sorted_data[mid - 1]) / 2 if len(sorted_data) % 2 == 0 else sorted_data[mid]

        # Display results
        print(f"Displaying total from column {total_column_name} from ", end="")
        print("list..." if isinstance(data_table, list) else "dictionary...")

        print(f"Total from column {total_column_name} = {total}")
        print(f"The mean of column {total_column_name} = {mean}")
        print(f"The median of column {total_column_name} = {median}")

    except ValueError:
        print(f"One or more values in {total_column_name} could not be converted into numerical values")

    except IndexError:
        print(f"Column: {total_column_name} could not be found")

# Example usage with a list
data_list = [
    "COLUMN Names", "Fred", "John",
    "COLUMN Addresses", "Pontypridd", "Treforest",
    "COLUMN Credit", "10", "20",
    "COLUMN Product Names", "Widget1", "Widget2",
    "COLUMN Suppliers", "SupplierA", "SupplierB",
    "COLUMN Prices", "20", "END"
]
output_total_mean_median(data_list, "Prices")

# Example usage with a dictionary
data_dict = {
    "Names": ["Fred", "John"],
    "Addresses": ["Pontypridd", "Treforest"],
    "Credit": ["10", "20"],
    "Product Names": ["Widget1", "Widget2"],
    "Suppliers": ["SupplierA", "SupplierB"],
    "Prices": ["20"]
}
output_total_mean_median(data_dict, "Prices")



