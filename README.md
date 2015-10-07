
<h3># Repository belajar Pemrograman Jaringan # </h3>
<p># Membuat Program Chatting dengan bahasa Python #</p>
---------------
<h4>Author :</h4>
<p> Ronauli S ( ronayumik@gmail.com )</p>
<p> 5113100142 </p>
<p> Pemrograman Jaringan B 2015/2016 </p>
<p> Teknik Informatika ITS, Surabaya </p>

<h4> List Fitur dan Progress</h4>
<p>
1. INISIALISASI
	[*] Port server diinput sendiri oleh user
	[*] Client harus registrasi terlebih dahulu sebelum join roomchat
		* errorHandling saat username sudah ada
	[*] Client dapat notifikasi jika registrasi sukses
	
2. PERSONAL
	[*] Client bisa mengirim pesan broadcast, tanpa harus mengetikkan header apapun
	[*] Client bisa mengirim PM
		* Format : pm {username yang dituju} {pesan yang ingin dikirimkan}
	[*] Client bisa menerima pesan broadcast 
	[*] Client bisa menerima PM
		* Format : [PrivateMessage] from {username pengirim} : {pesan yang ingin dikirimkan}
	[*] Client bisa melihat identitas dirinya sendiri (whoami)
		* Format : whoami
	[*] Client bisa melihat siapa aja user yang sedang online
		* Format : listuser
	
3. GROUPCHAT // fiturnya susah nih

	Inisialisasi :
	[*] Client bisa membuat nama untuk grupchatnya sendiri
		* Format : creategrup {grupchat_name} {*optional : adduser { username(s) }}
		* Errorhandling saat nama yang dipilih sudah terdaftar sebagai user ataupun grupchat
	[*] Client bisa mengirimkan permintaan bergabung ke user-user yang online untuk gabung grupchat 
		* Format : switchgrup {groupchat} adduser { username(s) }
	[*] Minimal ada 1 client yang tergabung dlm grupchat 
	
	Permintaan bergabung :
	[*] Client bisa menerima permintaan bergabung dengan groupchat
		* Invitation berisi : username pengirim, nama grupchat, client yang sudah bergabung
		* Clients yang tergabung groupchat mendapat notifikasi bahwa invitation telah dikirim (id username)
	[*] Client bisa menerima ataupun menolak undangan grupchat tersebut
		* Clients yang tergabung groupchat mendapat notifikasi bahwa invitation ditolak atau diterima
	[*] Client yang tidak menerima invitation tidak bisa bergabung ke grupchat
		* #TODO#
	[*] Client yang sudah tergabung bisa mengirim invitation kepada userlain bergabung ke grupchat tersebut
		* Format : switchgrup {groupchat} adduser { username(s) }
		* Errorhandling saat mengundang user yang tidak terdaftar
		* Errorhandling saat mengundang user yang sudah tergabung sebelumnya
		* Errorhandling saat mengundang user yang sudah menerima undangan yang sama sebelumnya.
		
	Didalam grup chat:
	[*] Client bisa melihat siapa saja yang sudah bergabung dengan grupchatnya
		* Format : switchgrup {groupchat} listuser
	[*] Client bisa mengirimkan pesan ke grupchatnya
		* Format : switchgrup {groupchat} {message}
	
	Keluar dari grupchat
	[*] Client bisa keluar dari grupchat
		* Format : exitgrup {nama grupchat}
		* Client yang masih tergabung dng groupchat mendapat notifikasi : '{[Groupchat]} {username} meninggalkan groupchat'
	
	Menghapus Groupchat
	[*] Pembuat grupchat tidak bisa menghapus grupchat, semua client yang tergabung punya hak akses sama
		* #TODO#
	[*] Jika hanya satu client tersisa di dalam grupchat dan client exit groupchat, maka groupchat tersebut terhapus otomatis

4. KELUAR DARI PROGRAM

	[*] Client bisa keluar dari program dengan mengetikkan 'exit'
	[*] Server mendapat notifikasi username user yang keluar dari program chat
	[*] Client mendapat notifikasi username user yang keluar dari program chat
	</p>
	
<h4>Pengembangan program</h4>
<p>
1.	Menggunakan multiproses
2.	Dengan pendekatan OOP
3.	Terminal baru untuk chat tertentu
	</p>

	

	



