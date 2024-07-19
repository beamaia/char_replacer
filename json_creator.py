import click
import numpy as np
import re

@click.command()
@click.option('--file_path', help='The file path to read', required=True)
@click.option('--output', help='The output file path', default='output.txt')
def main(file_path, output):
    with open(file_path, 'r', encoding="utf8") as f:
        content = f.read()
    
    data = {
        "content": content,
    }

    with open(output, 'w', encoding="utf8") as f:
        f.write(str(data))
    

if __name__ == '__main__':
    main()