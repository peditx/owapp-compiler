import yaml

def generate_config(yaml_file, config_file):
    # باز کردن فایل YAML
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # باز کردن فایل .config برای نوشتن
    with open(config_file, 'w') as f:
        # نوشتن project_url
        f.write(f"CONFIG_project_url={data['project_url']}\n")
        
        # نوشتن معماری‌ها
        for arch in data.get('architectures', []):
            f.write(f"CONFIG_ARCH_{arch.upper()}={arch}\n")

# فراخوانی تابع
generate_config('config.yaml', 'openwrt/.config')
