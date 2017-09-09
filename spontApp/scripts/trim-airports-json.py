import argparse
import os
import json

# def parse_args():
#     parser = argparse.ArgumentParser(description="Creates a Proteomics QC Report")
#     parser.add_argument('--input', nargs='+', type=str, help='mzML files or folders that contain mzML files separated by space.')
#     parser.add_argument('--output-dir', type=str, required=True, help='Output folder, were the report will be written.')
#     return parser.parse_args()


def trim_cities_json(keep_keys, input_file, output_file):
    with open(input_file, 'r') as input_hd:
        data = json.load(input_hd)

    new_data = []
    for record in data:
        new_record = {key: record[key] for key in record if key in keep_keys}
        new_data.append(new_record)

    with open(output_file, 'w') as output_hd:
        json.dump(obj=new_data, fp=output_hd, indent=2, sort_keys=True)


def main():
    keep_keys = ['code', 'lat', 'lon', 'name']
    trim_cities_json(keep_keys, os.path.join('..', 'static', 'airports.json'), os.path.join('..', 'static', 'airports-trimmed.json'))


if __name__ == '__main__':
    main()