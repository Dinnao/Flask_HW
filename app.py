from flask import Flask, request, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)


key = Fernet.generate_key()
f = Fernet(key)

#берет сообщение, переводит в байты, шифрует, переводит в строку и возращяет результат
@app.route('/encrypt')
def encrypt():
    string_2_encrypt = bytes(request.args.get('string', 'Unknown'), 'utf-8')
    encrypt_str = f.encrypt(string_2_encrypt)
    return render_template('index.html',
                           way='Encrypted result:',
                           result=encrypt_str.decode())

#берет шифр, переводит в байты, разшифровывает, переводит в строку и возращяет результат
@app.route('/decrypt')
def decrypt():
    string_2_decrypt = bytes(request.args.get('string'), 'utf-8') #не понял как тут обработать на случай ошибки, перепробывал все
    decrypt_str = f.decrypt(string_2_decrypt)
    return render_template('index.html',
                           way='Decrypted result:',
                           result=decrypt_str.decode())


if __name__ == '__main__':
    app.run(debug=True)