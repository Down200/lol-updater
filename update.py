import requests, json, datetime

headers = {"User-Agent": "Mozilla/5.0"}

# 1. 获取最新版本号（动态适配，避免手动修改）
versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
latest_version = requests.get(versions_url, headers=headers).json()[0]  # 取第一个（最新版本）

# 2. 使用最新版本号获取英雄和装备数据
ch_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/zh_CN/champion.json"
it_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/zh_CN/item.json"

ch = requests.get(ch_url, headers=headers).json()
it = requests.get(it_url, headers=headers).json()

# 3. 保存数据
data = {
    "version": latest_version,  # 存储版本号
    "champions": ch,
    "items": it,
    "updated": datetime.datetime.utcnow().isoformat()
}

with open("latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"数据已更新至版本 {latest_version}，保存到 latest.json")
