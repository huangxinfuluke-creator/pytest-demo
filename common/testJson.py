def compare_json(expected, actual, path=""):
    for key in expected:
        if key not in actual:
            print(f"缺少字段: {path + key}")
        else:
            if isinstance(expected[key], dict):
                compare_json(expected[key], actual[key], path + key + ".")
            else:
                if expected[key] != actual[key]:
                    print(f"字段值不一致: {path + key}")
                    print(f"预期: {expected[key]}")
                    print(f"实际: {actual[key]}")



import json

# 读取 expected.json
with open("/Users/luke/pytest_demo/data/expected.json", "r", encoding="utf-8") as f:
    expected = json.load(f)

# 读取 actual.json
with open("/Users/luke/pytest_demo/data/actual.json", "r", encoding="utf-8") as f:
    actual = json.load(f)

# 直接对比
if expected == actual:
    print("JSON 完全一致，测试通过 ✅")
else:
    print("JSON 不一致，测试失败 ❌")

compare_json(expected, actual)
