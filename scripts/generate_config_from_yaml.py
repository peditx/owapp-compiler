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
                            if isinstance(item, str):  # بررسی اینکه item یک رشته باشد
                                f.write(f"CONFIG_{key}_{subkey}_{item.upper()}={item}\n")
                            else:
                                # اگر item یک دیکشنری یا نوع دیگری است، آن را به صورت پیش‌فرض بنویسیم
                                f.write(f"CONFIG_{key}_{subkey}_{str(item)}={str(item)}\n")
                    else:
                        if isinstance(subvalue, str):
                            f.write(f"CONFIG_{key}_{subkey.upper()}={subvalue}\n")
                        else:
                            f.write(f"CONFIG_{key}_{subkey.upper()}={str(subvalue)}\n")
            elif isinstance(value, list):
                # اگر مقدار لیست است
                for item in value:
                    if isinstance(item, str):  # بررسی اینکه item یک رشته باشد
                        f.write(f"CONFIG_{key}_{item.upper()}={item}\n")
                    else:
                        # اگر item یک دیکشنری یا نوع دیگری است، آن را به صورت پیش‌فرض بنویسیم
                        f.write(f"CONFIG_{key}_{str(item)}={str(item)}\n")
            else:
                # اگر مقدار تنها یک مقدار است
                f.write(f"CONFIG_{key}_{str(value).upper()}={str(value)}\n")

if __name__ == "__main__":
    yaml_file = sys.argv[1]
    config_file = sys.argv[2]
    generate_config(yaml_file, config_file)
