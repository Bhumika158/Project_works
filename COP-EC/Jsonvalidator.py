import json

def analyze_json(json_data, raw_json_str):
    metrics = {
        "ArrayElementCount": 0,      # max elements in any array
        "ContainerDepth": 0,         # max nesting depth
        "ObjectEntryCount": 0,       # max entries in any object
        "ObjectEntryNameLength": 0,  # max key length in any object
        "StringValueLength": 0,      # max string value length
        "PayloadSizeMB": round(len(raw_json_str.encode('utf-8')) / (1024 * 1024), 4)
    }

    def traverse(node, depth):
        metrics["ContainerDepth"] = max(metrics["ContainerDepth"], depth)

        if isinstance(node, dict):
            entry_count = len(node)
            metrics["ObjectEntryCount"] = max(metrics["ObjectEntryCount"], entry_count)
            for key, value in node.items():
                key_length = len(str(key))
                metrics["ObjectEntryNameLength"] = max(metrics["ObjectEntryNameLength"], key_length)
                traverse(value, depth + 1)

        elif isinstance(node, list):
            array_length = len(node)
            metrics["ArrayElementCount"] = max(metrics["ArrayElementCount"], array_length)
            for item in node:
                traverse(item, depth + 1)

        elif isinstance(node, str):
            str_length = len(node)
            metrics["StringValueLength"] = max(metrics["StringValueLength"], str_length)

        # Other primitive types (int, float, bool, None) do not affect these metrics

    traverse(json_data, 1)
    return metrics

# Example usage
if __name__ == "__main__":
    raw_json_str = input("Enter your JSON: ")
    try:
        parsed_json = json.loads(raw_json_str)
        result = analyze_json(parsed_json, raw_json_str)
        print("\n--- JSON Maximum Metrics ---")
        for key, value in result.items():
            print(f"{key}: {value}")
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
