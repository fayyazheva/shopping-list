from django.urls import path
from main.views import show_main, create_product, show_xml, show_json,show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
]


# Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.
# Impor path dari django.urls untuk mendefinisikan pola URL.
# Gunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
# Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.
# test_main_url_is_exist adalah tes untuk mengecek apakah path URL /main/ dapat diakses.
# test_main_using_main_template adalah tes untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.