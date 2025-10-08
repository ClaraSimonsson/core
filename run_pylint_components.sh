#!/bin/bash
# run_pylint_components_fixed.sh
# Runs pylint on each Home Assistant component and aggregates valid JSON

OUTPUT_FILE="pylint_components.json"
COMPONENTS_DIR="homeassistant/components"

# Create an empty array file
echo "[]" > "$OUTPUT_FILE"

for dir in "$COMPONENTS_DIR"/*/; do
    echo "Running pylint on $dir"
    pylint --exit-zero --disable=all --enable=E,W,C,R --output-format=json "$dir" > tmp.json

    # Merge tmp.json into the main output file
    # (jq -s adds arrays together)
    jq -s '.[0] + .[1]' "$OUTPUT_FILE" tmp.json > tmp_merged.json
    mv tmp_merged.json "$OUTPUT_FILE"
done

rm -f tmp.json
echo "✅ All results saved to $OUTPUT_FILE"
