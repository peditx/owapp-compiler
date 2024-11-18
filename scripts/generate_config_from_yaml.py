import yaml
import sys

def generate_config(yaml_file, config_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # ایجاد فایل پیکربندی OpenWrt .config
    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

if __name__ == "__main__":
    yaml_file = sys.argv[1]
    config_file = sys.argv[2]
    generate_config(yaml_file, config_file)
