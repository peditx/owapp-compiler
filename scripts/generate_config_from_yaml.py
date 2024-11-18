import yaml

def generate_config(yaml_file, config_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    f.write(f"CONFIG_{key}_{sub_key.upper()}={sub_value}\n")
            elif isinstance(value, list):
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

yaml_file = 'config.yaml'
config_file = '/home/runner/work/owapp-compiler/owapp-compiler/openwrt/.config'
generate_config(yaml_file, config_file)
