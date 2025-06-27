import json

def analyze_json(json_data):
    metrics = {
        "ArrayElementCount": 0,
        "ContainerDepth": 0,
        "ObjectEntryCount": 0,
        "ObjectEntryNameLength": 0,
        "StringValueLength": 0
    }

    def traverse(node, depth):
        # Update maximum depth
        metrics["ContainerDepth"] = max(metrics["ContainerDepth"], depth)

        if isinstance(node, dict):
            metrics["ObjectEntryCount"] += len(node)
            metrics["ObjectEntryNameLength"] += sum(len(str(key)) for key in node.keys())
            for value in node.values():
                traverse(value, depth + 1)
        elif isinstance(node, list):
            metrics["ArrayElementCount"] += len(node)
            for item in node:
                traverse(item, depth + 1)
        elif isinstance(node, str):
            metrics["StringValueLength"] += len(node)
        # Other primitive types (int, float, bool, None) are ignored

    traverse(json_data, 1)
    return metrics

# Example usage
if __name__ == "__main__":
    input_json = input("Enter your JSON: ")
    try:
        parsed_json = json.loads(input_json)
        result = analyze_json(parsed_json)
        print("\n--- JSON Metrics ---")
        for key, value in result.items():
            print(f"{key}: {value}")
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
