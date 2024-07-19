import click
import numpy as np
import re

@click.command()
@click.option('--file_path', help='The file path to read', required=True)
@click.option('--output', help='The output file path', default='output.txt')
@click.option('--replace_in', help='The string to replace', required=True)
@click.option('--replace_with', help='The string to replace with', required=True)
def main(file_path, output, replace_in, replace_with):
    with open(file_path, 'r', encoding="utf8") as f:
        content = f.read()
    
    if replace_in == replace_with:
        raise ValueError("replace_in and replace_with should be different")
    
    new_content = re.sub(replace_in, replace_with, content)

    with open(output, 'w', encoding="utf8") as f:
        f.write(new_content)

if __name__ == '__main__':
    main()