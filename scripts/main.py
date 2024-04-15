import json
import os

def main():
    missing_config = "file 'PE_data.csv' is not listed in config mapping, Skipping"
    json_data = [{
        "team": "SRE",
        "template": "default",
        "summary": "No config",
        "description": missing_config
    }]
    json_string = json.dumps(json_data)

    # Path to the GitHub Environment file (typically provided by GitHub Actions)
    github_env = os.getenv('GITHUB_ENV')

    if github_env is not None:
        with open(github_env, 'a') as env_file:
            env_file.write(f"JSON_INPUT={json_string}\n")
    else:
        print("GITHUB_ENV not found. Ensure this script is running within a GitHub Actions environment.")

if __name__ == "__main__":
    main()
