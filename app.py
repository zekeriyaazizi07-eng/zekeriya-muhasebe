import streamlit as st
import pandas as pd
from datetime import datetime

# إعداد واجهة البرنامج
st.set_page_config(page_title="Zekeriya Muhasebe", layout="wide")

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>💎 نظام زكريا للمحاسبة</h1>", unsafe_allow_html=True)

# قائمة التحكم الجانبية
menu = st.sidebar.radio("القائمة الرئيسية:", ["🛒 المشتريات اليومية", "⏱️ دوام العمال", "💰 كشف الرواتب (16/31)"])

# 1. قسم المشتريات
if menu == "🛒 المشتريات اليومية":
    st.header("تسجيل المشتريات")
    with st.form("p_form"):
        item = st.text_input("اسم المادة")
        price = st.number_input("السعر", min_value=0.0)
        date = st.date_input("التاريخ", datetime.now())
        if st.form_submit_button("حفظ"):
            st.success(f"تم تسجيل شراء {item} بمبلغ {price}")

# 2. قسم الدوام
elif menu == "⏱️ دوام العمال":
    st.header("سجل ساعات العمال")
    with st.form("w_form"):
        worker = st.text_input("اسم العامل")
        h_normal = st.number_input("ساعات عادية", min_value=0)
        h_extra = st.number_input("ساعات إضافي", min_value=0)
        if st.form_submit_button("تسجيل اليوم"):
            st.info(f"تم تسجيل دوام {worker}")

# 3. قسم الرواتب
elif menu == "💰 كشف الرواتب (16/31)":
    st.header("احتساب الدفعات النصف شهرية")
    day = datetime.now().day
    period = "النصف الأول (1-15)" if day <= 15 else "النصف الثاني (16-31)"
    st.warning(f"الفترة الحالية: {period}")
    st.write("بانتظار ربط قاعدة البيانات لعرض الحسابات...")
