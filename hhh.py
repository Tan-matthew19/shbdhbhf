import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credit: Dibuat dengan cinta oleh Stanislaus Matthew Sutandang
# Email: matthewsutandang.tren@gmail.com
# Tujuan: Aplikasi interaktif dengan tema Valentine

# Fungsi untuk mengirim email
def send_email(message):
    sender_email = "matthewsutandang.tren@gmail.com"  # Ganti dengan email pengirim
    receiver_email = "luvlubtest@gmail.com"  # Ganti dengan email penerima
    password = "gkly zfzx vohz zgon"  # Ganti dengan password email pengirim (gunakan App Password jika Gmail)

    # Set up server SMTP Gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)

    # Membuat email
    subject = "Pesan Valentine"
    body = f"Pesan: {message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Kirim email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# HTML, CSS, and JS
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random No Button</title>
  <style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Poppins', Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: linear-gradient(135deg, #ffafbd, #ffc3a0);
        color: #333;
    }
    .wrapper {
        position: relative;
        width: 90%;
        max-width: 400px;
        text-align: center;
        background: white;
        padding: 20px 15px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .question {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
        color: #333;
    }
    .gif {
        max-width: 100%;
        height: auto;
        margin-bottom: 15px;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }
    .btn-group {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .yes-btn {
        background-color: #4caf50;
        color: white;
    }
    .yes-btn:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .no-btn {
        background-color: #ff4d4d;
        color: white;
    }
    .no-btn:hover {
        background-color: #e43e3e;
        transform: scale(1.05);
    }
  </style>
</head>
<body>
<div class="wrapper">
  <h2 class="question">Do you love me?</h2>
  <img class="gif" alt="gif" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjJvdWZzYXc1NGJ6aGp1cDE3b2dyNnVzOGN1andkMjVrMmRzeGwwZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3OhXBaoR1tVPW/giphy.gif" />
  <div class="btn-group">
    <button class="yes-btn">Yes</button>
    <button class="no-btn">No</button>
  </div>
</div>
<script>
  const yesBtn = document.querySelector(".yes-btn");
  const noBtn = document.querySelector(".no-btn");
  const question = document.querySelector(".question");
  const gif = document.querySelector(".gif");

  yesBtn.addEventListener("click", () => {
    question.textContent = "Being with you is the greatest gift in my life. I love you. -m";
    gif.src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGNhdXh1b252b2F2b2U4cHRlNGkwMDZsajllaGF1cDJyb2p4NXl2YiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/G6N0pDDgDpLjUvNoyQ/giphy.gif";
    noBtn.style.display = "none";
  });

  noBtn.addEventListener("mouseover", () => {
    const wrapper = document.querySelector(".wrapper");
    const wrapperRect = wrapper.getBoundingClientRect();
    const noBtnRect = noBtn.getBoundingClientRect();

    const maxX = wrapperRect.width - noBtnRect.width;
    const maxY = wrapperRect.height - noBtnRect.height;

    const randomX = Math.random() * maxX;
    const randomY = Math.random() * maxY;

    noBtn.style.position = "absolute";
    noBtn.style.left = `${randomX}px`;
    noBtn.style.top = `${randomY}px`;
  });
</script>
</body>
</html>
"""

# Menampilkan HTML di Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)

# Pemutar musik MP3
st.markdown("## 💌")
# Pemutar lagu pertama
try:
    with open("Love.mp3", "rb") as audio_file1:
        st.audio(audio_file1.read(), format="audio/mp3")
except FileNotFoundError:
    st.error("File 'Love.mp3' tidak ditemukan. Pastikan file tersedia.")

# Pemutar lagu kedua
try:
    with open("Blessed.mp3", "rb") as audio_file2:
        st.audio(audio_file2.read(), format="audio/mp3")
except FileNotFoundError:
    st.error("File 'Blessed.mp3' tidak ditemukan. Pastikan file tersedia.")

# Menambahkan fitur email setelah pesan dikirim
message = st.text_area("Pesan untuk Pengirim:")
if st.button("Kirim Pesan"):
    if message:
        send_email(message)
        st.success("Pesan telah terkirim! 💌")
    else:
        st.error("Pesan tidak boleh kosong.")
