import yaml

def generate_config(yaml_file, config_file):
    # باز کردن فایل YAML
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # نوشتن در فایل پیکربندی
    with open(config_file, 'w') as f:
        for key, value in data.items():
            # اگر value یک لیست یا دیکشنری باشد، باید آن را بررسی کنیم
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    f.write(f"CONFIG_{key}_{sub_key.upper()}={sub_value}\n")
            elif isinstance(value, list):
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

# مسیر صحیح فایل‌ها
yaml_file = '/root/config.yaml'  # مسیر صحیح به فایل YAML
config_file = '/root/openwrt/.config'  # مسیر صحیح به فایل پیکربندی

generate_config(yaml_file, config_file)
