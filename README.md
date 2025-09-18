# Hydrogen Maintenance Prediction

هذا المشروع يحلل بيانات أنظمة الهيدروجين الأخضر عشان:  
- يتنبأ متى الحرارة توصل لمستوى خطر  
- يحدد متى يحتاج النظام لصيانة  
- يوضح إذا فيه فقاعات غازية  

## المجلدات
- data/ : ملفات البيانات (CSV).  
- model/ : ملف الموديل المدرب.  
- backend/ : كود الباك إند (Flask).  
- frontend/ : الواجهة (Streamlit).  
- requirements.txt : المكتبات المطلوبة.  

## طريقة التشغيل
1. ثبّت المكتبات:
   ```bash
   pip install -r requirements.txt
