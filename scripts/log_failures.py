# This script logs failed test cases where calculated response is far from expected
import pandas as pd
import json

def log_failures(input_csv='data/dose_response_with_failures.csv', output_json='reports/failed_cases_log.json', threshold=0.05):
    df = pd.read_csv(input_csv)
    failed_cases = []

    for idx, row in df.iterrows():
        error = abs(row['expected_response'] - row['calculated_response'])
        if error > threshold:
            failed_cases.append({
                'sample_id': int(row['sample_id']),
                'drug_name': row['drug_name'],
                'dose_mg': row['dose_mg'],
                'expected': row['expected_response'],
                'actual': row['calculated_response'],
                'error': round(error, 3)
            })

    with open(output_json, 'w') as f:
        json.dump(failed_cases, f, indent=4)

    print(f"Logged {len(failed_cases)} failed test cases to {output_json}")

if __name__ == '__main__':
    log_failures()
