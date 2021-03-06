print("RENTAL MOBIL ABCD")

print("-------------------------------")

#Input
nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))

if umur < 18:
    print("Maaf", nama, "anda belum bisa meminjam kendaraan")
else:
    ktp = input("Masukkan nomor KTP Anda: ")
    no_tlp = int(input("Masukkan no telepon: "))
    alamat = input("Masukan alamat rumah anda : ")
    email = input("Masukan alamat E-mail anda : ")
    k_mobil = int(input("Jumlah penumpang (maksimal 12 penumpang): "))
    if k_mobil == (1-5):
        kapasitasmobil = "maksimal 5 orang"
        harga = 500000
    elif k_mobil == (5-7):
        kapasitasmobil = "maksimal 7 orang"
        harga = 750000
    else:
        kapasitasmobil = "maksimal 12 orang"
        harga = 1050000
    if k_mobil > 12:
        print("Maksimal penumpang adalah 12 orang")
    else:
        hari = int(input("Masukkan Durasi Peminjaman (dalam hari): "))
        if hari > 14:
            print("Mohon maaf", nama, "untuk peminjaman lebih dari 14 hari,")
            print("dimohon untuk datang langsung untuk detail lebih lanjutnya")
        else:
            subtotal = (hari*harga)
            if hari > 6:
                diskon = (hari * harga) * 0.05
            else:
                diskon = 0
            total = (hari * harga) - diskon

            tra = input("Masukkan cara transaksi [c untuk cash/ t untuk non tunai]: ")

            if tra == "c":
                adm = 0
            else:
                adm = 6500

            if tra == "c":
                tran = "Cash"
                ttl = total
            else:
                tran = "Non Tunai"
                ttl = (total + adm)

            word = '*'*len(ktp)

            import locale

            locale.setlocale(locale.LC_ALL, 'id_ID')

            print("-------------------------------")
            print("RENTAL MOBIL ABCD")
            print("-------------------------------")
            print("Nama                          : ", str(nama))
            print("Alamat                        : ", str(alamat))
            print("Umur                          : ", str(umur))
            print("No telepon                    : ", str(no_tlp))
            print("KTP anda                      : ", str(word))
            print("Alamat email                  : ", str(email))
            print("Kapasitas Mobil               : ", str(k_mobil))
            print("Lama peminjaman               : ", str(hari), "hari")
            print("Biaya per hari                : ", "Rp. ", str(locale.format_string('%.2f', harga, True)))
            print("Subtotal                      : ", "Rp. ", str(locale.format_string('%.2f', subtotal, True)))
            print("Potongan yang didapat         : ", "Rp. ", str(locale.format_string('%.2f', diskon, True)))
            print("-------------------------------")
            print("Total bayar                   : ", "Rp. ", str(locale.format_string('%.2f', total, True)))
            print("-------------------------------")
            print("Metode pembayaran             : ", str(tran))
            print("Biaya admin                   : ", "Rp. ", str(locale.format_string('%.2f', adm, True)))
            print("Total setelah admin           : ", "Rp. ", str((locale.format_string('%.2f', ttl, True))))
            print()
            print()
            print("Kendaraan yang anda pinjam", str(kapasitasmobil))
            print("Transaksi ini hanya berlaku selama 3 hari")
            print("Bila transaksi tidak diproses dalam 3 hari,")
            print("maka transaksi dibatalkan")
            print("Terima kasih")

            import datetime
            import tarfile

            extension = ".txt"
            tst = datetime.datetime.now().isoformat("-").split(".")[0].replace(":", "-")
            formatfile = 'print ' + nama + ' ' + tst + extension
            tar = tarfile.open(formatfile, "w")
            deadline = datetime.date.today() + datetime.timedelta(days=3)
            pinjam = datetime.date.today()

            f = open(formatfile, "w")
            f.write("-------------------------------\n")
            f.write("RENTAL MOBIL ABCD\n")
            f.write("-------------------------------\n")
            f.write("Nama                          : %s\n" % nama)
            f.write("Alamat                        : %s\n" % alamat)
            f.write("Umur                          : %s\n" % umur)
            f.write("No telepon                    : %s\n" % no_tlp)
            f.write("KTP anda                      : %s\n" % word)
            f.write("Alamat email                  : %s\n" % email)
            f.write("Kapasitas Mobil               : %s\n" % k_mobil)
            f.write("Lama peminjaman               : %s\n" % hari)
            f.write("Biaya per hari                : Rp. %s\n" % (locale.format_string('%.2f', harga, True)))
            f.write("Subtotal                      : Rp. %s\n" % (locale.format_string('%.2f', subtotal, True)))
            f.write("Potongan yang didapat         : Rp. %s\n" % (locale.format_string('%.2f', diskon, True)))
            f.write("-------------------------------\n")
            f.write("Subtotal setelah diskon       : Rp. %s\n" % (locale.format_string('%.2f', total, True)))
            f.write("-------------------------------\n")
            f.write("Metode pembayaran             : %s\n" % tran)
            f.write("Biaya admin                   : Rp. %s\n" % (locale.format_string('%.2f', adm, True)))
            f.write("Total setelah admin           : Rp. %s\n" % (locale.format_string('%.2f', ttl, True)))
            f.write("-------------------------------\n")
            f.write("-------------------------------\n")
            f.write("Kendaraan yang anda pinjam %s\n" % kapasitasmobil)
            f.write("Transaksi ini hanya berlaku selama 3 hari\n")
            f.write("Bila transaksi tidak diproses dalam 3 hari,\n")
            f.write("maka transaksi dibatalkan\n")
            f.write("Terima kasih\n")
            f.close()

            extension1 = ".doc"
            tst1 = datetime.datetime.now().isoformat("-").split(".")[0].replace(":", "-")
            formatfile1 = 'database '+nama+' '+tst+extension1
            tar1 = tarfile.open(formatfile1, "w")

            f = open(formatfile1, "w")
            f.write("Peminjaman tanggal %s\n" % pinjam)
            f.write("Nama                          : %s\n" % nama)
            f.write("Alamat                        : %s\n" % alamat)
            f.write("Umur                          : %s\n" % umur)
            f.write("No telepon                    : %s\n" % no_tlp)
            f.write("KTP anda                      : %s\n" % ktp)
            f.write("Alamat email                  : %s\n" % email)
            f.write("Kapasitas Mobil               : %s\n" % k_mobil)
            f.write("Lama peminjaman               : %s\n" % hari)
            f.write("Metode pembayaran             : %s\n" % tran)
            f.write("Biaya per hari                : Rp. %s\n" % (locale.format_string('%.2f', harga, True)))
            f.write("Subtotal                      : Rp. %s\n" % (locale.format_string('%.2f', subtotal, True)))
            f.write("Potongan yang didapat         : Rp. %s\n" % (locale.format_string('%.2f', diskon, True)))
            f.write("Subtotal setelah diskon       : Rp. %s\n" % (locale.format_string('%.2f', total, True)))
            f.write("Biaya xadmin                   : Rp. %s\n" % (locale.format_string('%.2f', adm, True)))
            f.write("-------------------------------\n")
            f.write("Total setelah admin           : Rp. %s\n" % (locale.format_string('%.2f', ttl, True)))
            f.write("Limit pembayaran pada %s\n" % deadline)
            f.close()
