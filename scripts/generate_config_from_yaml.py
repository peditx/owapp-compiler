import yaml
import sys

def generate_config(yaml_file, config_file):
    # باز کردن فایل yaml
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # ایجاد فایل پیکربندی OpenWrt .config
    with open(config_file, 'w') as f:
        for key, value in data.items():
            if isinstance(value, dict):
                # اگر مقدار دیکشنری است، باید کلیدهای آن را پردازش کنیم
                for subkey, subvalue in value.items():
                    if isinstance(subvalue, list):
                        for item in subvalue:
                            f.write(f"CONFIG_{key}_{subkey}_{item.upper()}={item}\n")
                    else:
                        f.write(f"CONFIG_{key}_{subkey.upper()}={subvalue}\n")
            elif isinstance(value, list):
                # اگر مقدار لیست است
                for item in value:
                    f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
            else:
                # اگر مقدار تنها یک مقدار است
                f.write(f"CONFIG_{key}_{value.upper()}={value}\n")

if __name__ == "__main__":
    yaml_file = sys.argv[1]
    config_file = sys.argv[2]
    generate_config(yaml_file, config_file)
