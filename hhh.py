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
  <title>Valentines Day</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    .gradient-background {
      background: rgb(255, 208, 229);
      background: linear-gradient(180deg, rgba(255, 208, 229, 1) 0%, rgba(255, 232, 242, 1) 36%, rgba(255, 255, 255, 1) 100%);
    }

    .bounce2 {
      animation: bounce2 2s ease infinite;
    }

    @keyframes bounce2 {
      0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
      }
      40% {
        transform: translateY(-20px);
      }
      60% {
        transform: translateY(-10px);
      }
    }
  </style>
</head>
<body class="gradient-background">
  <div class="flex items-center justify-center h-screen">
    <div class="flex flex-col items-center p-4">
      <img id="imageDisplay" src="./images/image1.gif" alt="Cute kitten with flowers" class="rounded-md h-[300px]" style="object-fit: cover;" />
      <h2 id="valentineQuestion" class="text-4xl font-bold italic text-[#bd1e59] my-4">Will you be my Valentine?</h2>
      <div class="flex gap-4 pt-[20px] items-center" id="responseButtons">
        <button id="yesButton"
          class="bounce2 inline-flex items-center justify-center whitespace-nowrap rounded-md text-[20px] font-medium disabled:pointer-events-none disabled:opacity-50 hover:bg-green-400 min-h-12 min-w-[75px] px-4 py-2 bg-green-500 text-white transition">
          Yes
        </button>
        <button id="noButton"
          class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-[20px] font-medium transition disabled:pointer-events-none disabled:opacity-50 hover:bg-red-700 h-12 min-w-[75px] w-auto px-4 py-2 bg-red-500 text-white">
          No
        </button>
      </div>
    </div>
  </div>

  <script type="module">
    import confetti from 'https://cdn.skypack.dev/canvas-confetti';
    const yesButton = document.getElementById('yesButton');
    const noButton = document.getElementById('noButton');
    const imageDisplay = document.getElementById('imageDisplay');
    const valentineQuestion = document.getElementById('valentineQuestion');
    const responseButtons = document.getElementById('responseButtons');
  
    let noClickCount = 0;
    let buttonHeight = 48; // Starting height in pixels
    let buttonWidth = 80;
    let fontSize = 20; // Starting font size in pixels
    const imagePaths = [
      "./images/image1.gif",
      "./images/image2.gif",
      "./images/image3.gif",
      "./images/image4.gif",
      "./images/image5.gif",
      "./images/image6.gif",
      "./images/image7.gif"
    ];
  
    noButton.addEventListener('click', function() {
      if (noClickCount < 5) {
        noClickCount++;
        imageDisplay.src = imagePaths[noClickCount];
        buttonHeight += 35; // Increase height by 5px on each click
        buttonWidth += 35;
        fontSize += 25; // Increase font size by 1px on each click
        yesButton.style.height = `${buttonHeight}px`; // Update button height
        yesButton.style.width = `${buttonWidth}px`;
        yesButton.style.fontSize = `${fontSize}px`; // Update font size
        if (noClickCount < 6) {
          noButton.textContent = ["No", "Are you sure?", "Pookie please", "Don't do this to me :(", "You're breaking my heart", "I'm gonna cry..."][noClickCount];
        }
      }
    });
  
    yesButton.addEventListener('click', () => {
      imageDisplay.src = './images/image7.gif'; // Change to image7.gif
      valentineQuestion.textContent = "Yayyy!! :3"; // Change the question text
      responseButtons.style.display = 'none'; // Hide both buttons
      confetti(); // Trigger confetti animation
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


st.markdown('<p style="text-align: center; font-size: 10px; color: #686868;">Created with ❤️ by M</p>', unsafe_allow_html=True)
