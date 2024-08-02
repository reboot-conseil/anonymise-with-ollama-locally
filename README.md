# anonymise-with-ollama-locally
Code snipet to remove PII from a text using llama3.1 with ollama locally

# Prerequisites
- ollama installed

https://ollama.com/download
- `llama3` model downloaded  
```sh
ollama pull llama3
```

# Install
```sh
git clone https://github.com/reboot-conseil/anonymise-with-ollama-locally
cd anonymise-with-ollama-locally
python3.12 -m venv .venv
```
Enter virtual environment:
- On windows : `.venv/Script/Activate.ps1`
- On Linux : `source .venv/bin/activate`

Install requirements
```sh
pip install -r requirements.txt
```

# Run demonstration
Demonstration in jupyter notebook `demonstration.ipynb`

# Run script
```sh
python main.py --input <input_file_path>
```

```sh
usage: main.py [-h] --input INPUT [--output OUTPUT] [-v]

options:
  -h, --help       show this help message and exit
  --input INPUT    Path to input text file
  --output OUTPUT  Optional. Path to output text file
  -v, --verbose    Optional. Verbose mode
```

# Customize
You can customize the prompt in the file `prompt.txt`
