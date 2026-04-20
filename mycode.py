import pandas
import os

data = {
    'name' : ['vivek', 'andhre', 'august'],
    'age' : [22, 24, 26],
}

data = pandas.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

data.to_csv(file_path, index=False)

print('data file added')