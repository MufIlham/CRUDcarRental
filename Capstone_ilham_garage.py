# Capstone Project
# Muhammad Umar fatwa Ilhami

car_data = {
    "BR01MT" : {"Type" : "Brio", "Transmission" : "MT", "Seats" : 5, "Price" : 250000},
    "AV01MT" : {"Type" : "Avanza", "Transmission" : "MT", "Seats" : 6, "Price" : 300000},
    "FO01MT" : {"Type" : "Fortuner", "Transmission" : "MT", "Seats" : 6, "Price" : 450000},
    "IN01AT" : {"Type" : "Innova", "Transmission" : "AT", "Seats" : 8, "Price" : 500000},
    "CI01AT" : {"Type" : "Civic", "Transmission" : "AT", "Seats" : 4, "Price" : 450000},
    "HI01MT" : {"Type" : "Hiace", "Transmission" : "MT", "Seats" : 12, "Price" : 700000}
}

column_name = ["Id", "Type", "Transmission", "Seats", "Price"]

# =========================================================================================
# Menu 1
# READ (Menampilkan daftar mobil)

def menu_1():
    print('''
    MENU 1:
    1. Tampilkan isi seluruh data
    2. Tampilkan data spesifik
    3. Kembali ke main menu
    ''')
    user_input = input("Masukkan opsi yang ingin dipilih: ")

    if user_input == '1':
        menu1_sub1()
        menu_1()
    elif user_input == '2':
        menu1_sub2()
    elif user_input == '3':
        main_menu()
    else:
        print("(INFO) Input yang anda masukkan salah")
        menu_1()


# Menu 1 Sub menu 1, untuk print keseluruhan data
def menu1_sub1():
    global car_data
    global column_name

# (: <20) Format untuk string spasi, (:) untuk menyamakan spasi antar baris data,(<) untuk rata kiri pada data baris tabel
    
    print("\nList mobil yang tersedia:\n")
    print(f"{column_name[0]: <10}|{column_name[1]: <15}|{column_name[2]: <15}|{column_name[3]: <10}|{column_name[4]: <10}")
    print("----------+---------------+---------------+----------+----------")
    for i in car_data.keys():
        print(f"{i: <10}|{(car_data[i]['Type']): <15}|{(car_data[i]['Transmission']): <15}|{str(car_data[i]['Seats']): <10}|{str(car_data[i]['Price']): <10}")
    print()

    if len(car_data) == 0:
        print("\t\tTidak ada record tersedia.")


# Menu 1 Sub menu 2, untuk memilih data yang ingin di print berdasarkan kolom tertentu
def menu1_sub2():
    print('''
    Data spesifik berdasarkan:
    1. ID Mobil
    2. Type Mobil
    3. Transmission Mobil
    4. Jumlah Seat
    5. Price Per Hari

    Untuk kembali ke Menu 1, Masukkan 6
    ''')
    user_input = input("Masukkan opsi yang ingin dipilih: ")

    if user_input == '1':
        check_input_value("Id")
    elif user_input == '2':
        check_input_value("Type")
    elif user_input == '3':
        check_input_value("Transmission")
    elif user_input == '4':
        check_input_value("Seats")
    elif user_input == '5':
        check_input_value("Price")
    elif user_input == '6':
        menu_1()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        menu1_sub2()


# Untuk input value dari kolom tertentu dan print row berdasarkan value dari kolom tsb
def check_input_value(input_column_name):
    global car_data
    temp_record_value = []

    for i in car_data.keys():
        if i not in temp_record_value:
            temp_record_value.append(i)
        for j in car_data[i].values():
            if j not in temp_record_value:
                temp_record_value.append(j)

    # Untuk melakukan formatting pada input yang diberikan user sesuai input dari kolom
    if input_column_name == "Id":
        user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ").upper()
    elif input_column_name == "Type":
        user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ").capitalize()
    elif input_column_name == "Transmission":
        user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ").upper()
    elif input_column_name == "Seats":
        user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ")
        while user_input.isalpha():
            print("(INFO) Input yang anda masukkan harus berupa integer Price\n")
            user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ")
            
            if user_input.isnumeric():
                if int(user_input) > 1 and int(user_input) < 17:
                    user_input = int(user_input)
                    break
                else:
                    pass
        else:
            if int(user_input) > 1 and int(user_input) < 17:
                user_input = int(user_input)

    elif input_column_name == "Price":
        user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ")
        while user_input.isalpha():
            print("(INFO) Input yang anda masukkan harus berupa integer Price\n")
            user_input = input(f"Masukkan {input_column_name} Mobil dari mobil yang ingin ditampilkan: ")
            
            if user_input.isnumeric():
                if int(user_input) > 99999 and int(user_input) < 5000001:
                    user_input = int(user_input)
                    break
                else:
                    pass
        else:
            if int(user_input) > 99999 and int(user_input) < 5000001:
                user_input = int(user_input)

    # Apabila input berada di dalam record, maka print function akan dijalankan
    if user_input in temp_record_value:
        menu1_sub2_print(user_input, input_column_name)
        yes_no_question(menu1_sub2, main_menu)
    else:
        print(f"(INFO) Data tersebut tidak ada untuk kolom {input_column_name} pada list mobil\n")
        check_input_value(input_column_name)

# Untuk print row berdasarkan nama kolom dan user input
def menu1_sub2_print(user_input, input_column_name):
    global car_data
    global column_name

    # Apabila nama kolom adalah "Id", maka index yang digunakan adalah user_input yang berisi id. 
    # Hanya print 1 record karna ID itu unique value
    if input_column_name == "Id":
        print(f"{column_name[0]: <10}|{column_name[1]: <20}|{column_name[2]: <10}|{column_name[3]: <10}|{column_name[4]: <10}")
        print("----------+--------------------+----------+----------+----------")
        print(f"{user_input: <10}|{(car_data[user_input]['Type']): <20}|{(car_data[user_input]['Transmission']): <10}|{str(car_data[user_input]['Seats']): <10}|{str(car_data[user_input]['Price']): <10}")

    # Apabila nama kolom bukan "Id", 
    # maka akan terjadi for loop dengan kondisi dimana system akan print jika user_input memiliki value 
    # yang sama dengan value yg sedang di loop
    elif input_column_name != "Id":
        
        print(f"{column_name[0]: <10}|{column_name[1]: <20}|{column_name[2]: <10}|{column_name[3]: <10}|{column_name[4]: <10}")
        print("----------+--------------------+----------+----------+----------")
        for i in car_data.keys():
            if car_data[i][input_column_name] == user_input: 
                print(f"{i: <10}|{(car_data[i]['Ti]ype']): <20}|{(car_data[i]['Transmission']): <10}|{str(car_data[i]['Seats']): <10}|{str(car_data[i]['Price']): <10}")

# Untuk memberikan opsi function check_input_value(column_name) apakah ingin melanjutkan mencari record atau tidak
def yes_no_question(my_function_1, my_function_2):
    yes_no_input = input("\nApakah anda ingin melanjutkan (yes/no)? ").lower()

    if yes_no_input == 'yes':
        my_function_1()
    elif yes_no_input == 'no':
        my_function_2()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        yes_no_question(my_function_1, my_function_2)


# =========================================================================================
# Menu 2
# CREATE (Membuat item mobil degan attribute-attribute nya)
def menu_2():
    print('''
    MENU 2:
    1. Tambahkan Mobil Rental ke Dalam Tabel
    2. Kembali ke Main Menu
    ''')

    user_input = input("Masukkan opsi yang ingin dipilih: ")

    if user_input == '1':
        menu1_sub1()
        add_a_car()
    elif user_input == '2':
        main_menu()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        menu_2()

# Untuk menggabungkan beberapa function menjadi satu dan akan terjadi recursive function.
# Dimana function ini akan memanggil create_a_car_item() dan menu1_sub1() jika user tidak kembali ke menu 2
# melalui create_car_item()
def add_a_car():
    create_a_car_item()
    menu1_sub1()
    add_a_car()

# Untuk meminta input dan mengecek input tipe mobil dari user. Return dari function ini adalah data tipe mobil
def input_car_type():
    car_type = input("Masukkan Type Mobil: ")

    if car_type.isalpha():
        return car_type.capitalize()
    else:
        print("\n(INFO) Format type mobil yang anda masukkan salah\n")
        return input_car_type()

# Untuk meminta input dan mengecek input transmisi mobil dari user. Return dari function ini adalah data transmisi mobil
def input_car_transmission():
    car_transmission = input("Masukkan Type Transmission Mobil (MT/AT): ").upper()

    if len(car_transmission) == 2:
        if car_transmission[0] == 'M' or car_transmission[0] == 'A' and car_transmission[1] == 'T':
            return car_transmission.upper()
        else:
            print("\n(INFO) Format transmission yang anda masukkan salah\n")
            return input_car_transmission()
    else:
        print("\n(INFO) Format transmission yang anda masukkan salah\n")
        return input_car_transmission()

# UUntuk meminta input dan mengecek input seats dari user. Return dari function ini adalah jumlah seats
def input_car_seats():
    car_seats = input("Masukkan Jumlah Seat yang Dimiliki Mobil: ")

    if car_seats.isnumeric():
        if int(car_seats) > 1 and int(car_seats) < 17:
            return int(car_seats)
        else:
            print("\n(INFO) Jumlah Seat di Mobil yang Anda Masukkan Salah\n")
            return input_car_seats()
    else:
        print("\n(INFO) Format Jumlah Seat di Mobil yang Anda Masukkan Salah\n")
        return input_car_seats()

# Untuk meminta input dan mengecek input harga dari user. Return dari function ini adalah harga dari rental mobil
def input_car_price():
    car_price = input("Masukkan Price Rental dari Mobil: ")

    if car_price.isnumeric():
        if int(car_price) > 99999 and int(car_price) < 5000001:
            return int(car_price)
        else:
            print("\n(INFO) Price Rental Mobil yang Anda Masukkan Salah\n")
            return input_car_price() 
    else:
        print("\n(INFO) Format Price Rental Mobil yang Anda Masukkan Salah\n")
        return input_car_price()

# Untuk meminta input dan mengecek input id dari user. Return dari function ini adalah Id mobil
# Jika id sudah terdaftar maka ada informasi yang di print sebagai feedback utk user
def input_car_id():
    global car_data
    a_list = []
    user_input = input("Masukkan CAR ID Dengan Format AABBCC\nAA = 2 huruf dari type mobil (Brio = BR)\nBB = 2 angka unique (cth: 01)\nCC = Tipe Transmission (MT/AT)\nInput: ").upper()
    
    if user_input.isalnum() and len(user_input) == 6:
        if user_input[0:2].isalpha() and user_input[2:4].isnumeric() and user_input[4:] == 'MT' or user_input[4:] == 'AT':
            for i in car_data.keys():
                a_list.append(i)
        else:
            print("\n(INFO) Format ID Mobil yang Anda Masukkan Salah\n")
            return input_car_id()
    else:
        print("\n(INFO) Format ID Mobil yang Anda Masukkan Salah\n")
        return input_car_id()
    
    if user_input not in a_list:
        return user_input
    else:
        print("\n(INFO) ID Telah Terdaftar\n")
        return input_car_id()

# Untuk auto generate Id berdasarkan user input
def create_car_id(car_type, car_transmission):
    global car_data

    num_id = "01"
    int_num_id = int(num_id)
    car_id = car_type[0:2].upper() + num_id + car_transmission
    temp_list = []

    for i in car_data.keys():
        temp_list.append(i)
    
    for i in temp_list:
        while car_id == i:
            int_num_id = int(i[2:4])
            int_num_id += 1

            if int_num_id >= 10:
                car_id = car_type[0:2].upper() + str(int_num_id) + car_transmission
            else:
                car_id = car_type[0:2].upper() + "0" + str(int_num_id) + car_transmission

            if car_id not in temp_list:
                return car_id
            else:
                pass
        
    return car_id

# Menambahkan Item mobil kedalam car_data dictionary
def create_a_car_item():
    global car_data

    user_input = input("\nApakah anda ingin menginput ID (ya / tidak)?\nJika tidak maka kami akan buatkan ID untuk anda.\nKetik return untuk kembali ke menu 2.\nInput: ").lower()

    # Jika user mau menginput car id maka akan terjadi pengecekan di tipe dan transmisi
    # Jika tidak sesuai maka akan memberi feedback kepada user dan meminta user untuk menginput ulang
    if user_input == 'ya':
        new_car_id = input_car_id()
        new_car_type = input_car_type()

        while new_car_type[0:2].upper() != new_car_id[0:2]:
            print("\n(INFO) Input Type yang anda masukkan harus sesuai dengan input Tipe di ID Anda\n")
            new_car_type = input_car_type()

            if new_car_type[0:2].upper() == new_car_id[0:2]:
                new_car_type = new_car_type
                break
        else:
            new_car_type = new_car_type

        new_car_transmission = input_car_transmission()

        while new_car_transmission.upper() != new_car_id[4:]:
            print("\n(INFO) Input transmission yang anda masukkan harus sesuai dengan input Transmission di ID Anda\n")
            new_car_transmission = input_car_transmission()

            if new_car_transmission.upper() == new_car_id[4:]:
                new_car_type = new_car_type
                break
        else:
            new_car_type = new_car_type

        new_car_seats = input_car_seats()
        new_car_price = input_car_price()

    # Jika tidak, maka id akan system generate kan menggunakan function create_car_id
    elif user_input == 'tidak':
        new_car_type = input_car_type()
        new_car_transmission = input_car_transmission()
        new_car_seats = input_car_seats()
        new_car_price = input_car_price()
        new_car_id = create_car_id(new_car_type, new_car_transmission)

    elif user_input == 'return':
        menu_2()

    else:
        print("\n(INFO) Input yang anda masukkan salah\n")
        return create_a_car_item()
    
    yes_no_insert(new_car_id, new_car_type, new_car_transmission, new_car_seats, new_car_price)

def yes_no_insert(new_car_id, new_car_type, new_car_transmission, new_car_seats, new_car_price):
    user_input = input("Apakah anda ingin memasukkan mobil ke dalam tabel(yes/no)? ").lower()

    # Memastikan apakah user ingin menginsert item ke dalam tabel
    if user_input == 'yes':
        car_data[new_car_id] = {"Type" : new_car_type, "Transmission" : new_car_transmission, "Seats" : new_car_seats, "Price" : new_car_price}
        menu1_sub1()
    elif user_input == 'no':
        menu1_sub1()
        create_a_car_item()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        yes_no_insert(new_car_id, new_car_type, new_car_transmission, new_car_seats, new_car_price)


# =========================================================================================
# Menu 3
# UPDATE (Memodifikasi informasi dari suatu mobil)
def menu_3():
    print('''
    MENU 3:
    1. Update informasi dari mobil rental
    2. Kembali ke Main Menu
    ''')

    user_input = input("Masukkan opsi yang ingin dipilih: ")

    if user_input == '1':
        input_car_update()
    elif user_input == '2':
        main_menu()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        menu_3()

# Input ID dan nama Kolom yang akan diupdate.
# Id dan nama kolom akan di filter sesuai dengan id dan nama kolom yang terdaftar di dalam tabel
def input_car_update():
    menu1_sub1()

    global car_data
    temp_list_id = []
    temp_list_id_2 = []

    input_id = input("Masukkan ID untuk data yang mau di update: ").upper()
    
    for i in car_data.keys():
        temp_list_id.append(i)
    
    for i in car_data.keys():
        for j in car_data[i].keys():
            if j not in temp_list_id_2:
                temp_list_id_2.append(j.capitalize())

    
    if input_id in temp_list_id:
        input_column_name = input(f"Masukkan nama kolom yang anda ingin ganti dari item dengan ID {input_id}: ").capitalize()

        while input_column_name not in temp_list_id_2:
            print("(INFO) Input Kolom yang anda masukkan tidak sesuai")
            input_column_name = input(f"Masukkan nama kolom yang anda ingin ganti dari item dengan ID {input_id}: ").capitalize()

            if input_column_name in temp_list_id_2:
                return update_car_info(input_id, input_column_name)
            else:
                continue
        else:
            return update_car_info(input_id, input_column_name)

    else:
        print("(INFO) Input ID yang dimasukkan salah")
        return input_car_update()

# Untuk update informasi dari mobil
def update_car_info(car_id, column_name):
    global car_data

    new_value = input(f"Input value baru dari ID {car_id} pada kolom {column_name}: ")

    if column_name == "Type":

        while new_value.isalpha() == False or len(new_value) > 15:
            print(f"\n(INFO) Value dari kolom {column_name} yang anda masukkan salah")
            new_value = input(f"Input value baru dari ID {car_id} pada kolom {column_name}: ")

    elif column_name == "Transmission":

        while new_value.upper() != "MT" and new_value.upper() != "AT":
            print(f"\n(INFO) Value dari kolom {column_name} yang anda masukkan salah")
            new_value = input(f"Input value baru dari ID {car_id} pada kolom {column_name}: ")

    elif column_name == "Seats":

        while new_value.isnumeric() == False or int(new_value) < 2 or int(new_value) > 16:
            print(f"\n(INFO) Value dari kolom {column_name} yang anda masukkan salah")
            new_value = input(f"Input value baru dari ID {car_id} pada kolom {column_name}: ")

    elif column_name == "Price":

        while new_value.isnumeric() == False or int(new_value) < 100000 or int(new_value) > 5000000:
            print(f"\n(INFO) Value dari kolom {column_name} yang anda masukkan salah")
            new_value = input(f"Input value baru dari ID {car_id} pada kolom {column_name}: ")

    # Memberi konfirmasi kepada user apakah user ingin mengupdate data atau tidak
    yes_no = input("Apakah anda ingin mengupdate data dari data mobil (yes/no)? ")

    if yes_no == 'yes':
        # Jika numeric, new_value akan diubah ke integer
        if new_value.isnumeric():
            new_value = int(new_value)
            car_data[car_id][column_name] = new_value
            menu1_sub1()
        else:
            # Apabila user mengganti transmisi (len(new_value) == 2), maka ID akan terganti sesuai dengan apa yg user update)
            # Begitupula dengan jika user mengganti tipe dari mobil
            if len(new_value) == 2:
                new_car_id = create_car_id(car_id[0:2], new_value.upper())
                car_data[new_car_id] = car_data.pop(car_id)
                car_data[new_car_id][column_name] = new_value.upper()
                menu1_sub1()
            else:
                new_car_id = create_car_id(new_value.upper(), car_id[4:])
                car_data[new_car_id] = car_data.pop(car_id)
                car_data[new_car_id][column_name] = new_value.capitalize()
                menu1_sub1()

        continue_or_no()

    elif yes_no == 'no':
        main_menu()
    else:
        print("(INFO) Input yang anda masukkan salah")
        return update_car_info(car_id, column_name)

# Untuk memberi opsi kepada user apakah mereka ingin melanjutkan update atau tidak
def continue_or_no():
    user_input = input("Apakah anda ingin mengupdate informasi dari mobil lagi (yes/no)?").lower()

    if user_input == "yes":
        input_car_update()
    elif user_input == "no":
        main_menu()
    else:
        print("(INFO) Input yang anda masukkan salah")
        continue_or_no()


# =========================================================================================
# Menu 4
# DELETE (Menghapus item mobil dari data mobil)
def menu_4():
    print('''
    MENU 4:
    1. Delete record dari mobil rental
    2. Kembali ke Main Menu
    ''')

    user_input = input("Masukkan opsi yang ingin dipilih: ")

    if user_input == '1':
        menu1_sub1()
        check_delete_input_column()
        menu1_sub1()
        menu_4()
    elif user_input == '2':
        main_menu()
    else:
        print("\n(INFO) Input yang anda masukkan salah")
        menu_4()
    
# Untuk mengecek input kolom dari user apakah sesuai atau tidak
def check_delete_input_column():
    global car_data
    global column_name

    user_input_column = input("Masukkan Nama Kolom dari Record yang ingin anda hapus: ").capitalize()

    while user_input_column not in column_name:
        print("(INFO) Input kolom yang anda masukkan salah")
        user_input_column = input("Masukkan Nama Kolom dari Record yang ingin anda hapus: ").capitalize()

        if user_input_column in column_name:
            check_delete_input_value(user_input_column)
            break
    else:
        check_delete_input_value(user_input_column)

# Untuk mengecek apakah input value yang ingin di delete ada di dalam record
# Jika ya, maka system akan print value yang ingin di hapus dan memberi konfirmasi kepada user
# berupa apakah record ingin dihapus atau tidak
def check_delete_input_value(column_name):
    global car_data
    temp_record_value = []

    for i in car_data.keys():
        if i not in temp_record_value:
            temp_record_value.append(i)
        for j in car_data[i].values():
            if j not in temp_record_value:
                temp_record_value.append(j)
    
    if column_name == "Id":
        user_input_value = input("Masukkan Value dari Record yang ingin anda hapus: ").upper()

        if user_input_value in temp_record_value:
            menu1_sub2_print(user_input_value, column_name)
            yes_no_delete(column_name, user_input_value)
        else:
            print("(INFO) Input yang anda masukkan salah\n")
            return check_delete_input_value(column_name)

    elif column_name == "Type":
        user_input_value = input("Masukkan Value dari Record yang ingin anda hapus: ").capitalize()

        if user_input_value in temp_record_value and user_input_value.isalpha and len(user_input_value) < 16:
            menu1_sub2_print(user_input_value, column_name)
            yes_no_delete(column_name, user_input_value)
        else:
            print("(INFO) Input yang anda masukkan salah\n")
            return check_delete_input_value(column_name)

    elif column_name == "Transmission":
        user_input_value = input("Masukkan Value dari Record yang ingin anda hapus: ").upper()

        if user_input_value in temp_record_value and user_input_value == "MT" or user_input_value == "AT":
            menu1_sub2_print(user_input_value, column_name)
            yes_no_delete(column_name, user_input_value)
        else:
            print("(INFO) Input yang anda masukkan salah\n")
            return check_delete_input_value(column_name)
        
    elif column_name == "Seats" or column_name == "Harga":
        user_input_value = input("Masukkan Value dari Record yang ingin anda hapus: ")
        user_input_value = int(user_input_value)

        if column_name == "Seats":
            if user_input_value in temp_record_value and user_input_value > 1 and user_input_value < 17:
                menu1_sub2_print(user_input_value, column_name)
                yes_no_delete(column_name, user_input_value)
            else:
                print("(INFO) Input yang anda masukkan salah\n")
                return check_delete_input_value(column_name)
        elif column_name == "Price":
            if user_input_value in temp_record_value and user_input_value > 99999 and user_input_value < 5000001:
                menu1_sub2_print(user_input_value, column_name)
                yes_no_delete(column_name, user_input_value)
            else:
                print("(INFO) Input yang anda masukkan salah\n")
                return check_delete_input_value(column_name)

# Untuk menghapus record berdasarkan nama kolom dan input dari user
def delete_car_item(column_name, input_value):
    global car_data
    
    if column_name == "Id":
        del car_data[input_value]
    else:
        for i in list(car_data.keys()):
            if car_data[i][column_name] == input_value:
                del car_data[i]

# Untuk memberi konfirmasi kembali kepada user apakah user ingin menghapus record tsb 
def yes_no_delete(column_name, input_value):
    user_input = input("\nApakah anda yakin ingin menghapus record ini (yes/no)?")

    if user_input == 'yes':
        delete_car_item(column_name, input_value)
    elif user_input == 'no':
        menu_4()
    else:
        print("(INFO) Input yang anda masukkan salah\n")
        return yes_no_delete(column_name, input_value)


# =========================================================================================
# Menu 5
# EXIT (Exit program yang sedang berjalan)
def menu_5():
    exit_input = input("Apakah anda ingin keluar dari program (yes/no)? ").lower()
    if exit_input == 'yes':
        exit()
    elif exit_input == 'no':
        main_menu()
    else:
        print("\n(INFO) Tolong masukkan 'yes' atau 'no'")
        menu_5()


# =========================================================================================
# Print menu function
def main_menu():
    print()
    print("Selamat Datang di ILHAM GARAGE\nSilahkan pilih menu di bawah")
    print('''
    List Menu:
    1. Menampilkan Daftar Mobil
    2. Menambah Mobil
    3. Mengupdate Informasi dari Mobil
    4. Menghapus Mobil
    5. Exit Program
    ''')

    user_choice(choose_option())

# User input function
def choose_option():
    a_choice = input("Masukkan opsi yang ingin dipilih: ")
    return a_choice

# Untuk menentukan user di direct ke menu ke berapa sesuai input dari user
def user_choice(a_choice):

    if a_choice == '1':
        menu_1()
    elif a_choice == '2':
        menu_2()
    elif a_choice == '3':
        menu_3()
    elif a_choice == '4':
        menu_4()
    elif a_choice == '5':
        menu_5()
    else:
        print("\nInput yang anda masukkan tidak sesuai dengan pilihan menu yang tersedia")
        main_menu()
        user_choice(choose_option())

# Calling Main Function to run the program
main_menu()