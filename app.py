import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Zekeriya Muhasebe", layout="wide")

# رابط البيانات المستخرج من الرابط الذي أرسلته (بصيغة CSV للقراءة)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRDLDeqhO4b9vjF9hy_D5QXxmqS_IrFAqI6bdJ-9eLBZ7r7kBq8SOiOaxOkAxw2M3Bi2vM3R5pvp3Zr/pub?output=csv"

st.markdown("<h1 style='text-align: center; color: #1E88E5;'>💎 نظام زكريا للمحاسبة</h1>", unsafe_allow_html=True)

# القائمة الجانبية
menu = st.sidebar.radio("القائمة الرئيسية:", ["📊 عرض السجلات (جوجل شيت)", "📝 تسجيل جديد"])

if menu == "📊 عرض السجلات (جوجل شيت)":
    st.subheader("البيانات الحالية من Google Sheets")
    try:
        # قراءة البيانات مباشرة من الرابط الذي أنشأته
        df = pd.read_csv(sheet_url)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error("لم نتمكن من سحب البيانات. تأكد من نشر الملف كـ CSV على الويب.")

elif menu == "📝 تسجيل جديد":
    st.info("لعرض البيانات، قم بإضافتها في ملف Google Sheets أولاً، وستظهر هنا تلقائياً.")
    st.markdown(f"[اضغط هنا لفتح ملف الجوجل شيت الخاص بك وتعديله](https://docs.google.com/spreadsheets/d/1bxWX76IO2m1gbe9yQGVF47FGXQ9J5sYvp8OGnIzuluc/edit)")
