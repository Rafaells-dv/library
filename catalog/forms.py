from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Coloque uma data entre agora e 4 semanas. (Padrão 3)')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Data inválida - renevoção no passado'))

        if data > (datetime.date.today() + datetime.timedelta(weeks=4)):
            raise ValidationError(_('Data inválida - renovação acima do tempo máximo'))

        return data
