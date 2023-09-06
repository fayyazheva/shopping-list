from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]


# Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.
# Impor path dari django.urls untuk mendefinisikan pola URL.
# Gunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
# Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.
# test_main_url_is_exist adalah tes untuk mengecek apakah path URL /main/ dapat diakses.
# test_main_using_main_template adalah tes untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.