
from django import forms

class DeletionReasonForm(forms.Form):
    REASON_CHOICES = [
        ("У клиента недостаточно средств", "У клиента недостаточно средств"),
        ("Клиент указал не тот товар", "Клиент указал не тот товар"),
        ("Товара нет в наличии", "Товара нет в наличии"),
    ]
    reason = forms.ChoiceField(choices=REASON_CHOICES, label="Причина удаления")