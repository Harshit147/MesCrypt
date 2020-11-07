from .models import Message, DigitalCertificate
from django.forms import ModelForm
from Crypto.Cipher import AES
import hashlib
import base64


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['user_name', 'message', 'encrypted_message', 'hashed_message']
        labels = {
            'user_name': 'To',
            'encrypted_message': 'Cipher Text',
            'hashed_message': 'SHA3 Hashed'
        }

        def clean_encrypted_message(self):
            encryption_suite = AES.new('this is a key123', AES.MODE_CFB, 'This is an IV456')
            cipher_text = (encryption_suite.encrypt(self.cleaned_data['message']))
            cipher_text = base64.b64encode(cipher_text)
            return cipher_text

        def clean_hashed_message(self):
            h = hashlib.sha384()
            h.update(self.cleaned_data['message'])
            return h.hexdigest()
