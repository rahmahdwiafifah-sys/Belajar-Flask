# Impor library Flask agar kita bisa membuat aplikasi web menggunakan Python
from flask import Flask, render_template

# digunakan untuk membuat objek aplikasi Flask.
app = Flask(__name__)

# ROUTING
@app.route('/')
def index():
    return "hello world"

@app.route('/nama')
def nama():
    return "halaman nama"

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/mahasiswa')
def halmahasiswa():
    kelas = '4KA14'
    return render_template('mhs.html',kelas=kelas)

@app.route('/bootstrap')
def bs():
    return render_template('bs.html')

@app.route('/tabel')
def tabel():
    return render_template('tabel.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dosen')
def haldosen():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM DOSEN''')
    dosen = cursor.fetchall()
    cursor.close()
    return render_template('dosen.html', dosen=dosen)


if __name__ == '__main__':
    app.run(debug=True, port='3000') # digunakan untuk menjalankan server Flask.

