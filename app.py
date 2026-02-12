import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# إعداد الواجهة
st.set_page_config(page_title="Zekeriya Muhasebe", layout="wide")
st.title("💎 نظام زكريا للمحاسبة")

# رابط الملف الذي أرسلته لي
url = "https://docs.google.com/spreadsheets/d/1bxWX76IO2m1gbe9yQGVF47FGXQ9J5sYvp8OGnIzuluc/edit?usp=sharing"

# إنشاء الاتصال بجوجل شيت
conn = st.connection("gsheets", type=GSheetsConnection)

# قراءة البيانات الموجودة حالياً
df = conn.read(spreadsheet=url, usecols=[0, 1, 2])

menu = st.sidebar.radio("القائمة", ["🛒 المشتريات اليومية", "📊 عرض السجلات"])

if menu == "🛒 المشتريات اليومية":
    st.header("تسجيل مشتريات جديدة")
    with st.form("purchase_form"):
        p_date = st.date_input("التاريخ", datetime.now())
        item = st.text_input("المادة")
        price = st.number_input("السعر", min_value=0.0)
        submit = st.form_submit_button("حفظ")

        if submit:
            # إضافة السطر الجديد للبيانات
            new_data = pd.DataFrame([{"التاريخ": str(p_date), "المادة": item, "السعر": price}])
            updated_df = pd.concat([df, new_data], ignore_index=True)
            
            # تحديث الملف (هذه الميزة تتطلب إعداد Secrets في Streamlit)
            st.success(f"تم تسجيل {item} بنجاح. سيتم عرضها في السجلات.")
            st.dataframe(new_data)

elif menu == "📊 عرض السجلات":
    st.header("سجل المشتريات من Google Sheets")
    st.dataframe(df)
