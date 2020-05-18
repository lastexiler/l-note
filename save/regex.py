import re
input_path = "./regex.txt"
output_path = "./regex_output.txt"
pattern = re.compile(r'semc_[a-z0-9_]+')
result = []
with open(input_path, mode='r') as f:
    for sub_str in f.readlines():
        result += pattern.findall(sub_str.lower())
print(result)
with open(output_path, mode='w') as f:
    f.write('\n'.join(result))
