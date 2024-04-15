import json

def main():
    missing_config = "file 'PE_data.csv' is not listed in config mapping, Skipping"
    json_data = [{
        "team": "SRE",
        "template": "default",
        "summary": "No config",
        "description": missing_config
    }]
    json_string = json.dumps(json_data)
    
    # Print JSON string to standard output for capture
    print(json_string)

if __name__ == "__main__":
    main()
