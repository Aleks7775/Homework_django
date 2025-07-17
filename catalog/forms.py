from django.forms import ModelForm

from catalog.models import Product
from django.core.exceptions import ValidationError

spam = ['казино', 'биржа', 'обман', 'криптовалюта',
        'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'custom-checkbox',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену за 1 кг'
        })

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('(цена) не может быть 0 или отрицательным числом')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for i in spam:
            if i in name:
                raise ValidationError('Запрещенные слова, которые нельзя использовать в названиях')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for i in spam:
            if i in description:
                raise ValidationError('Запрещенные слова, которые нельзя использовать в описаниях')
        return description
