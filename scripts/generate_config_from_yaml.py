import yaml

def generate_config(yaml_file, config_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, dict):  # Check if the value is a dictionary
                for subkey, subvalue in value.items():
                    f.write(f"CONFIG_{key}_{subkey.upper()}={subvalue}\n")
            else:
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_config_from_yaml.py <yaml_file> <config_file>")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    config_file = sys.argv[2]
    
    generate_config(yaml_file, config_file)
