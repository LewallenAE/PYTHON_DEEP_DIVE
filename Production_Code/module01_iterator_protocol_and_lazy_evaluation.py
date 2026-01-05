from typing import Iterator, Dict

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
            'amount':int(parts[1]),
            'currency': parts[2]
        }        
        yield data

def high_value_filter(transactions: Iterator[dict])-> Iterator[str]:
    for record in transactions:
        if record['currency'] == 'USD' and record['amount'] > 1000:
            yield record['id']

def run_pipeline(filepath: str):
    raw_lines = transaction_reader(filepath)
    parsed_data = transaction_parser(raw_lines)
    high_value_ids = high_value_filter(parsed_data)

    print(f"Processing {filepath}...")
    for tx_id in high_value_ids:
        print(f"Found High-Value Transaction: {tx_id}")

if __name__ == "__main__":
    run_pipeline('transactions.csv')