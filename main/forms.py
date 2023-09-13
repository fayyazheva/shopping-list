from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

# model = Product untuk menunjukkan model yang digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product.
# fields = ["name", "price", "description"] untuk menunjukkan field dari model Product yang digunakan untuk form. Field date_added tidak dimasukkan ke list fields karena tanggal ditambahkan secara otomatis.
