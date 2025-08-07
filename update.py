import requests, json, datetime

headers = {"User-Agent": "Mozilla/5.0"}

# 最新英雄与装备
ch = requests.get(
    "https://ddragon.leagueoflegends.com/cdn/14.15.1/data/zh_CN/champion.json",
    headers=headers
).json()

it = requests.get(
    "https://ddragon.leagueoflegends.com/cdn/14.15.1/data/zh_CN/item.json",
    headers=headers
).json()

data = {"champions": ch, "items": it, "updated": datetime.datetime.utcnow().isoformat()}
with open("latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
