l = [{"nonid": "-222", "id": 0}, {"id": -101}]

res = min(l, key=lambda d: d.get("id", float('inf')))["id"]
print(res)

results = [
	{'cost': 98, 'source': 'vk'},
	{'cost': 153, 'source': 'yandex'},
	{'cost': 110, 'source': 'facebook'},
]

#m = min(results, key=lambda dic: dic.get('cost'))['cost']

m = min(dic["cost"] for dic in results if "cost" in dic)
print(m)