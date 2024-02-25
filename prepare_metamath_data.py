from datasets import load_dataset
import json
import io



dataset = load_dataset("meta-math/MetaMathQA")

n = 1000 #number of datapoints

# Select a subset of the dataset
subset = dataset['train'].select(range(n))



# Convert the dataset to a list of dictionaries
data_list = [item for item in subset]

# Write to a JSONL file
file_path=f'./data/metamath/train_{n}.jsonl'
with open(file_path, 'w', encoding='utf-8') as jsonl_file:
    for item in data_list:
        json_string = json.dumps(item, ensure_ascii=False)
        jsonl_file.write(json_string + '\n')