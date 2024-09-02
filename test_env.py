import sys
from io import StringIO
import re
from importlib import import_module

def read_input_data(input_string):
    input_examples = []
    output_examples = []
    
    # 正規表現パターンの定義
    pattern = r'入力例\d+\n([\s\S]*?)(?=\n出力例\d+|\Z)'
    matches = re.findall(pattern, input_string)
    
    for match in matches:
        input_example = match.strip()
        input_examples.append(input_example)
    
    # 出力例を抽出するための正規表現パターン
    pattern = r'出力例\d+\n([\s\S]*?)(?=\n入力例\d+|\Z)'
    matches = re.findall(pattern, input_string)
    
    for match in matches:
        output_example = match.strip()
        output_examples.append(output_example)
    
    return input_examples, output_examples

io_out = StringIO()

with open('input.txt', mode = 'r', encoding='utf-8') as f:
    input_strgs = f.read()

input_examples, output_examples = read_input_data(input_strgs)

sys.stdin = StringIO(input_examples[0])

# sys.stdin = open('input.txt', mode='r', encoding='utf-8')
# 標準出力を io に結びつける
# sys.stdout = io

mod = import_module('main')

# 標準出力を元に戻す
sys.stdout = sys.__stdout__

pass



# # ### 現在のpython環境を確認する
# base_path = sys.base_prefix
# venv_path = sys.prefix

# if base_path == venv_path:
#     python_path = str(pathlib.Path(base_path) / 'python.exe')
# else:
#     python_path = str(pathlib.Path(venv_path) / 'Scripts/python.exe')
# curdir = pathlib.Path(os.curdir).absolute()


# sys.stdin = 'hello world\n'
# # ### 現在のpython環境で実行する。
# output_str = subprocess.run(python_path + ' main.py', capture_output=True, text=True).stdout

pass

