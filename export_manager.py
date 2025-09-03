import json
import csv

def export_to_json(data,filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            print(f"Data exported to {filename} (JSON).")
    except Exception as e:
        print(f"Error exporting data to JSON: {e}")


def export_to_csv(data,filename):
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if isinstance (data, list):
                for row in data:
                    if isinstance (row, (list, tuple)):
                        writer.writerow(row)
                    else:
                        writer.writerow([row])
            else:
                writer.writerow([data])
        print(f"Data exported to {filename} (CSV).")
    except Exception as e:
        print(f"Error exporting to data to CSV: {e}")
