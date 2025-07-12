# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-1/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-2/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-3/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-4/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-5/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-6/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMHOT/GAFN-7/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMAOL/GAFN-8/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/GAFN-MMAOL/GAFN-9/refs/heads/main/configs/proxy_configs.txt",
    "https://sub.xn--2vxn29amga.com/s/026150b3ed3c89331dc35ada977cdcb0",
    "https://raw.githubusercontent.com/GAFN-MMAOL/GAFN-10/refs/heads/main/configs/proxy_configs.txt",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 1000

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": False,
    "ss://": True,
    "trojan://": False,
    "tuic://": False,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 365
