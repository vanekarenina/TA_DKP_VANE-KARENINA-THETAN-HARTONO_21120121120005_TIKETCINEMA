from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as msg
from tkinter import ttk
import datetime as dt

#Membuat sebuah class untuk methodnya
class Loginregisteruser:
    def main_screen(self):
        Button(text='Login',bg= "White",fg='Black',height= '2',width= '30',command = self.login).place(x=140, y=160)
    #inisialisasi
    def __init__(self,gui,header):
        self.gui = gui
        self.gui.geometry('480x318')
        self.gui.title(header)
        self.gui.resizable(0,0)
        self.main_screen()
    #menu login
    def login(self):
        screen1 = Toplevel(app)
        screen1.title("Login CGV CINEMA")
        screen1.geometry('350x160')
        screen1.resizable(0,0)
        Label(screen1, text= "Email").pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text = "Password").pack()
        self.entryPass = Entry(screen1,show='#',width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text = "Show Password", variable=self.check,command=self.open_password).pack(expand=False,fill=BOTH,padx=10,pady=5)
        self.showPass
        self.btnlogin = Button(screen1, text="Login", bg= 'white',fg='black',command=self.do_login).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)
    #Untuk mengecek input yang dimasukan, apakah sudah sesuai dengan file database
    def do_login(self):
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open('database.txt','r')
        
        for i in file :
            name,email,password = i.split(",")
            password = password.strip()
            if get_username == email and get_password == password:
                sukses = True
                break
        if (sukses):
            msg.showinfo("Login Success","Login Berhasil %s"%(name),parent=self.gui)
            self.sec_screen()
            return 
        elif get_username == '' or get_password == '':
            msg.showwarning("Login Gagal","Email atau Password Tidak Boleh Kosong",parent=self.gui)
            self.entryUser.focus_set()
        else :
            msg.showerror('Login Gagal','Email atau Password Salah',parent=self.gui)
            self.delete_data()

    #menampilkan password
    def open_password(self):
        Show = self.check.get()      
        if Show == 1:
            self.entryPass['show']=''
        else :
            self.entryPass['show']='#'

    #Menampilkan menu pesan tiket
    def sec_screen(self):
        global screen2
        screen2 = Toplevel(app)
        screen2.title("CGV CINEMA")
        screen2.geometry('400x450')
        screen2.resizable(0,0)
        #Header pesan tiket
        Label(screen2,text="PESAN TIKET" ,bg='Black',width='300',height='2',font= ('courier new',13, "bold"),fg='white').pack()
        
        #Menulis nama pemesan
        Label(screen2,text='').pack()
        Label(screen2,text="Nama\t\t:",).place(x=30, y=50)
        self.entry1 = Entry(screen2,font=("times new roman", 10))
        self.entry1.place(x=140, y=50)
        
        #button untuk kursi
        self.radiochr = StringVar(value="...")
        Label(screen2, text = "Seet\t\t:").place(x=30, y=75)
        self.entrykursi1 = Radiobutton(screen2, text = 'A', variable=self.radiochr,value ='A',command=self.seet)
        self.entrykursi1.place(x = 140, y = 75)
        self.entrykursi2 = Radiobutton(screen2, text = 'B', variable=self.radiochr,value ='B',command=self.seet1)
        self.entrykursi2.place(x = 140, y = 95)
        self.entrykursi3 = Radiobutton(screen2, text = 'C', variable=self.radiochr,value ='C',command=self.seet2)
        self.entrykursi3.place(x = 140, y = 115)
        Label(screen2, text='Nomor\t\t:').place(x=30, y=140)
        
        #button untuk memilih film
        self.radio = IntVar()
        Label(screen2, text = "Genre\t\t:").place(x=30, y=165)
        self.entrySrv1 = Radiobutton(screen2, text = 'Romance', variable=self.radio,value =1,command=self.roman_srv)
        self.entrySrv1.place(x = 140, y = 165)
        self.entrySrv2 = Radiobutton(screen2, text = 'Action', variable=self.radio,value =2,command=self.act_srv)
        self.entrySrv2.place(x = 140, y = 185)
        self.entrySrv3 = Radiobutton(screen2, text = 'Horor', variable=self.radio,value =3,command=self.hor_srv)
        self.entrySrv3.place(x = 140, y = 205)
        Label(screen2, text='Film\t\t:').place(x=30, y=230)

        #button untuk memilih harga
        Label (screen2, text ="Price List\t\t:").place(x=30, y=260)
        self.radiobtn = IntVar()
        self.radio1 = Radiobutton(screen2, text="Reguler - 30K",variable = self.radiobtn,value=30000).place(x = 140, y = 260)
        self.radio2 = Radiobutton(screen2,text="Sweet Box - 60K",variable = self.radiobtn,value=60000).place(x = 140, y = 280)
        
        #button untuk memilih jumlah tiket yang ingin dipesan
        Label(screen2,text=' ').pack()
        Label(screen2,text="Jumlah Tiket\t:",).place(x=30, y=315)
        self.entrysum1 = Entry(screen2,font=("times new roman", 10))
        self.entrysum1.place(x=140, y=315)
        
        #button untuk memilih payment
        Label(screen2,text="Payment Method\t:").place(x=30, y=345)
        self.strpym = StringVar(value='...') 
        self.combobox1 = ttk.Combobox(screen2,width = 17,font = ("times new roman", 10), textvariable = self.strpym, state ="readonly")
        self.combobox1.place(x=140, y=345)
        self.combobox1['values'] = ('Gopay','Dana','OVO','BCA','BRI','BNI')
        btn = Button(screen2, text="Pay", command=self.payment,bg= 'lightgreen',state=ACTIVE)
        btn.place(x=270 ,y=343)
        #buat menekan order
        self.btnsub = Button(screen2, text="Order",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.btn_sub,state = ACTIVE)
        self.btnsub.place(x = 320, y = 380)

    #Buat menentukan payment, agar sesuai dengan data yang diinginkan
    #Misalnya e-wallet akan menampilkan no hp
    def payment(self):
        Label(screen2, text ='Nomor\t\t:').place(x=30, y= 375)
        self.entrynum = Entry(screen2, font=("times new roman", 10))
        self.entrynum.place(x=140, y=375)

    #Mengambil data yang dimasukan, dan menampilkannya
    def btn_sub(self):
        name = self.entry1.get()
        kursi = self.radiochr.get()
        gnr = self.radio.get()
        film = self.region1.get()
        nom = self.radiobtn.get()
        jml = self.entrysum1.get()
        pym = self.strpym.get()
        chair = self.chair1.get()
        pay = self.entrynum.get()
        date = dt.datetime.now()
        if name == "" :
            msg.showwarning("Peringatan","Nama Tidak Boleh Kosong!",parent=self.gui)
            return
        if kursi == "...":
            msg.showwarning("Peringatan","Kursi Tidak Boleh Kosong!",parent=self.gui)
            return
        if chair == "...":
            msg.showwarning("Peringatan","Nomor Kursi Tidak Boleh Kosong!",parent=self.gui)
            return
        if gnr == 0:
            msg.showwarning("Peringatan","Genre Tidak Boleh Kosong!",parent=self.gui)
            return
        if film == "...":
            msg.showwarning("Peringatan","Film Tidak Boleh Kosong!",parent=self.gui)
            return
        if nom == 0:
            msg.showwarning("Peringatan","Harap Pilih Nominal Tiket!",parent=self.gui)
            return
        if pym == "...":
            msg.showwarning("Peringatan","Harap Pilih Metode Pembayaran!",parent=self.gui)
            return
        if pay == "":
            msg.showwarning("Peringatan","Nomor HP/Rek Tidak Boleh Kosong!",parent=self.gui)
            return
        else :
            msg.showinfo("Info Pesanan",f"Nama\t\t\t: {self.entry1.get()} \nSeet\t\t\t: {self.radiochr.get()} \nKursi\t\t\t: {self.chair1.get()} \nFilm\t\t\t: {self.region1.get()} \nTanggal Pemesanan\t: {date:%A, %B %d, %Y} \nMetode Pembayaran\t: {self.strpym.get()} \nTotal Pembayaran\t\t: Rp.{self.radiobtn.get() * int(self.entrysum1.get())},- \nStatus Pembayaran\t: Sukses!" )
            self.close_gui()

    def roman_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('A Whisker Away','Sweet And Sour','Josee, The Tiger and The Fish','Secret')
   
    def act_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2, width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('Doctor Strange in the Multiverse of Madness','Avengers: Endgame','Thor: Ragnarok','Black Panther')
    
    def hor_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('KKN di Desa Penari','Silent Hill')

    def seet(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')
    
    def seet1(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2, width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')

    def seet2(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')

    def delete_data(self):
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryUser.focus_set()
    
    def delete_uname(self): 
        self.entryPass.focus_set()
        self.entryUser.focus_set()
        self.entryUserName.delete(0,END)
        self.entryUserName.focus_set()
    
    def delete_email(self):
        self.entryUser.delete(0,END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryUser.focus_set()

    def delete_pass(self):
        self.entryPass.delete(0,END)
        self.entryUserName.focus_set()
        self.entryUser.focus_set()
        self.entryPass.focus_set()
        
    def close_gui(self):
        self.gui.destroy()

#Main menu agar GUI dapat berjalan
if __name__ == '__main__':
    global app
    app = Tk()
    logo = PhotoImage(file="Back1.png")
    app.iconphoto(True,logo)
    label = Label(app)
    bg = PhotoImage(file='Back.png')
    a_label = Label(app, image=bg)
    a_label.place(x=0, y=0, relheight=1, relwidth=1)
    start = Loginregisteruser(app,"CGV CINEMA")
    app.mainloop()

    #Variabel dan Tipe Data
    #Pengkondisian
    #Perulangan (for) 
    #Method and Function
    #OOP1 (Class and Contructor)
    #OOP2 (Setter and Getter)
    #GUI 
