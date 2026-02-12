import streamlit as st
import pandas as pd
from datetime import datetime

# إعداد الواجهة
st.set_page_config(page_title="Zekeriya Muhasebe", layout="wide")
st.title("💎 نظام زكريا للمحاسبة")

# رابط الـ CSV الذي حصلت عليه من "النشر على الويب"
# استبدل الرابط أدناه بالرابط الذي نسخته من Publish to web
CSV_URL = "https://docs.google.com/spreadsheets/d/1bxWX76IO2m1gbe9yQGVF47FGXQ9J5sYvp8OGnIzuluc/export?format=csv"

try:
    # محاولة قراءة البيانات
    df = pd.read_csv(CSV_URL)
    st.success("تم الاتصال بنجاح بجداول جوجل ✅")
except Exception as e:
    st.error(f"فشل الاتصال: تأكد من 'النشر على الويب' بصيغة CSV")
    df = pd.DataFrame(columns=["التاريخ", "المادة", "السعر"])

menu = st.sidebar.radio("القائمة", ["🛒 المشتريات اليومية", "📊 عرض السجلات", "💰 الرواتب"])

if menu == "🛒 المشتريات اليومية":
    st.header("تسجيل مشتريات جديدة")
    with st.form("my_form", clear_on_submit=True):
        p_date = st.date_input("التاريخ", datetime.now())
        item = st.text_input("المادة")
        price = st.number_input("السعر", min_value=0.0)
        submit = st.form_submit_button("حفظ")
        
        if submit:
            st.info("تم التسجيل في الذاكرة المؤقتة. ميزة الحفظ التلقائي تتطلب إعداد المفاتيح الأمني.")
            # هنا سنعرض ما سجله
            st.write(f"تم تسجيل: {item} بقيمة {price}")

elif menu == "📊 عرض السجلات":
    st.header("سجل المشتريات الحالي")
    st.table(df)
