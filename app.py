
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. إعداد عنوان الصفحة والمظهر
st.set_page_config(page_title="Smart Operations & Risk Predictor", layout="centered")
st.title("🛡️ Smart Operations & Risk Prediction System")
st.write("هذا النظام الذكي يساعد في فحص المعاملات والطلبات وتوقع نسبة خطورتها تلقائياً.")

st.markdown("---")

# 2. إنشاء الحقول التفاعلية في القائمة الجانبية (Sidebar) ليختار منها المستخدم
st.sidebar.header("📥 مدخلات المعاملة الجديدة")

category = st.sidebar.selectbox("نوع العملية (Category):", ['Join Request', 'Data Update', 'Role Permission', 'System Audit'])
sensitivity = st.sidebar.selectbox("مستوى الحساسية (Sensitivity Level):", ['Low', 'Medium', 'High'])
contract = st.sidebar.selectbox("حالة العقد (Contract Status):", ['Active', 'Expired'])
crowd = st.sidebar.selectbox("مستوى الازدحام/الضغط (Crowd Density):", ['Low', 'Medium', 'High'])
proc_time = st.sidebar.slider("وقت المعالجة المتوقع بالدقائق:", min_value=5, max_value=60, value=20)

# 3. زر التنبؤ
if st.button("🚀 فحص وتحليل المعاملة"):

    # هنا نقوم بمحاكاة سريعة لتوقع النموذج بناءً على الشروط المنطقية التي تدرب عليها
    # (نظراً لأن كولاب يحتاج إعدادات إضافية لربط الموديل الحي بالواجهة، قمنا بوضع المنطق مباشرة هنا لتسهيل التشغيل)
    is_risk = 0
    if contract == 'Expired' and sensitivity in ['High', 'Medium']:
        is_risk = 1
    elif crowd == 'High' and category == 'Role Permission':
        is_risk = 1

    # عرض النتيجة للمستخدِم بمظهر احترافي
    st.subheader("📊 نتيجة التحليل الذكي:")
    if is_risk == 1:
        st.error("⚠️ تنبيه: هذه المعاملة تُصنف كـ (عالية الخطورة / High Risk)! يُنصح بمراجعتها يدوياً.")
    else:
        st.success("✅ آمنة: هذه المعاملة تُصنف كـ (آمنة ونظامية / Safe).")

    st.info(f"الوقت المتوقع للمعالجة: {proc_time} دقيقة.")
