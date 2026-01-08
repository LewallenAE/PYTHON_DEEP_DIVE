#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script will evolve into a data ingester for AI eval platforms.

print("Starting data ingestion pipeline.")

print("Ready for AI eval data.")


MODEL_VERSION = "v1.2-beta"
current_batch = 1
data_path = "./evals/batch1.json"
DATA_FORMAT = "json"
print(f"Processing batch {current_batch} under {MODEL_VERSION} data path {data_path}, data_format {DATA_FORMAT}.")
