from langchain_community.llms import Ollama
import argparse
import os


def anonymise_text(text: str) -> str:
    assert isinstance(text, str)

    # load model
    llm = Ollama(model="llama3", base_url="http://192.168.1.70:11434")

    # load prompt
    with open("prompt.txt", "r") as f:
        prompt = f.read().strip() + "\n\n"

    return llm.invoke(prompt + text)


if __name__ == "__main__":
    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Path to input text file")
    parser.add_argument("--output", type=str, required=False, default=None, help="Optional. Path to output text file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Optional. Verbose mode")
    args = parser.parse_args()

    assert isinstance(args.input, str)
    assert os.path.exists(args.input)
    assert os.path.isfile(args.input)

    # open input file
    with open(args.input, "r") as f:
        data = f.read()

    # anonymise text
    anonymised_data = anonymise_text(data)

    # save anonymised text
    output_path = args.output
    if output_path is None:
        output_path = args.input + ".anonymised"

    with open(output_path, "w") as f:
        f.write(anonymised_data)

    # print output
    if args.verbose:
        print(anonymised_data)
