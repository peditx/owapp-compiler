import yaml
import os

def generate_config(yaml_file, config_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    if not os.path.exists(config_file):
        os.makedirs(config_file)

    with open(config_file, 'w') as f:
        # نوشتن مشخصات پروژه
        f.write(f"CONFIG_PROJECT_URL={data['project_url']}\n")
        
        # نوشتن معماری‌ها
        for arch in data.get('architectures', []):
            f.write(f"CONFIG_ARCH_{arch.upper()}={arch}\n")
            f.write(f"CONFIG_TARGET_{arch.upper()}_OPENWRT=y\n")  # برای هر معماری تنظیم کنید

# فراخوانی تابع برای ساخت پیکربندی
generate_config('config.yaml', 'openwrt/.config')
