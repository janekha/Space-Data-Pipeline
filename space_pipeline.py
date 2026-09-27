import requests

# 1. الذهاب إلى الفضاء وجلب البيانات الحية عن محطة الفضاء الدولية
response = requests.get("http://open-notify.org")

# 2. التقاط البيانات طاقياً وتحويلها لشكل مقروء
data = response.json()

# 3. إظهار النتيجة الفورية لعقلك السريع
print(f"إحداثيات محطة الفضاء الآن هي: {data['iss_position']}")
