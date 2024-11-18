import yaml

def generate_config(yaml_file, config_file):
    # خواندن داده‌ها از فایل YAML
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # نوشتن داده‌ها به فایل .config
    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, list):  # اگر مقدار یک لیست باشد
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

# مسیر فایل‌ها را اصلاح کنید
yaml_file = "/home/runner/work/owapp-compiler/owapp-compiler/config.yaml"
config_file = "/home/runner/work/owapp-compiler/owapp-compiler/openwrt/.config"

generate_config(yaml_file, config_file)
