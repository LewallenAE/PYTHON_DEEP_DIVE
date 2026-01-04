from typing import Iterator, Generator

def transaction_reader(filepath: str) -> Iterator[str]:
    """_summary_

    Yields lines one by one keeping one line of memory
    at a time.
    """
    
    with open(filepath, 'r') as f:
        for line in f:
            yield line

def transaction_parser(lines: Iterator[str]) -> Iterator[dict]:
    for line in lines:
        parts = line.strip().split(',')
        
        data = {
            'id': parts[0],
            'amount':.int(parts[1]),
            'currency': parts[2]
        }
        
        yield data