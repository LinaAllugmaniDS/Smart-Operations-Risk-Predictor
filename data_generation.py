import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# تحديد عدد السجلات
num_records = 1000

# 1. إنشاء أرقام الطلبات والتطوير
request_ids = [f"REQ-{1000 + i}" for i in range(num_records)]

# 2. توليد تواريخ عشوائية خلال النصف الأول من عام 2026
start_date = datetime(2026, 1, 1)
dates = [start_date + timedelta(days=int(np.random.randint(0, 150))) for _ in range(num_records)]

# 3. أنواع العمليات ومستويات الحساسية
categories = ['Join Request', 'Data Update', 'Role Permission', 'System Audit']
category_list = np.random.choice(categories, num_records, p=[0.4, 0.3, 0.2, 0.1])

sensitivity_levels = ['Low', 'Medium', 'High']
sensitivity_list = np.random.choice(sensitivity_levels, num_records, p=[0.5, 0.3, 0.2])

# 4. حالة العقد ومستوى الازدحام
contract_statuses = ['Active', 'Expired']
contract_list = np.random.choice(contract_statuses, num_records, p=[0.85, 0.15])

crowd_levels = ['Low', 'Medium', 'High']
crowd_list = np.random.choice(crowd_levels, num_records, p=[0.3, 0.5, 0.2])

# 5. حساب وقت المعالجة بناءً على مدخلات منطقية (حتى تكون البيانات واقعية)
processing_times = []
for i in range(num_records):
    base_time = 15
    if sensitivity_list[i] == 'High': base_time += 20
    if crowd_list[i] == 'High': base_time += 15
    # إضافة طابع عشوائي بسيط
    final_time = base_time + np.random.randint(-5, 10)
    processing_times.append(max(5, final_time))

# 6. تحديد مستوى الخطورة (المستهدف للتنبؤ المستقبلي) بناءً على شروط منطقية
risk_levels = []
for i in range(num_records):
    # إذا كان العقد منتهي والحساسية عالية -> خطورة مؤكدة
    if contract_list[i] == 'Expired' and sensitivity_list[i] in ['High', 'Medium']:
        risk_levels.append(1)
    # إذا كان الازدحام عالٍ والعملية تعديل صلاحيات
    elif crowd_list[i] == 'High' and category_list[i] == 'Role Permission':
        risk_levels.append(1)
    else:
        # نسبة خطورة عشوائية صغيرة للحالات العادية
        risk_levels.append(np.random.choice([0, 1], p=[0.92, 0.08]))

# جمع البيانات في DataFrame
df = pd.DataFrame({
    'Request_ID': request_ids,
    'Date': dates,
    'Category': category_list,
    'Sensitivity_Level': sensitivity_list,
    'Contract_Status': contract_list,
    'Crowd_Density_Level': crowd_list,
    'Processing_Time_Minutes': processing_times,
    'Risk_Level': risk_levels
})

# حفظ البيانات في ملف CSV
df.to_csv('operations_data.csv', index=False)
print("تم توليد ملف البيانات 'operations_data.csv' بنجاح يحتوي على 1000 سجل!")
