import yaml

def generate_config(yaml_file, config_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, list):
                # اگر مقدار یک لیست بود، هر آیتم را به صورت جداگانه اضافه کن
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                # در غیر اینصورت به طور مستقیم از value استفاده کن
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

# فایل yaml و مقصد config
yaml_file = 'config.yaml'
config_file = '.config'

generate_config(yaml_file, config_file)
