parking_smart = []
id = 1

while True:
    print("\n====================================")
    print("      SMART PARKING MANAGEMENT")
    print("=====================================")
    print("1. Them xe moi")
    print("2. Hien thi danh sach xe")
    print("3. Xoa xe khoi bai")
    print("4. Thoat")
    print("=====================================")

    choice = input("Nhap lua chon cua ban(1-4): ")
    if choice == "1":
        vehicle_type = input("Nhap loai xe: ").strip().title()
        while vehicle_type == "":
            print("Ko de trong loai xe!")
            vehicle_type = input("Nhap lai loai xe: ").strip().title()
        owner = input("Nhap ten chu xe: ").strip().title()
        while owner == "":
            print("Ko duoc de trong ten chu xe!")
            owner = input("Nhap lai ten chu xe: ").strip().title()
        vehicle = {
            "id": id,
            "type": vehicle_type,
            "owner": owner
        }
        parking_smart.append(vehicle)
        print(f"Da them xe ID {id} thanh cog!")
        id += 1

    elif choice == "2":
        if len(parking_smart) == 0:
            print("Bai xe hien dag trong!")
        else:
            header = (f"| {'ID':<5} | "f"{'Loại xe':<20} | "f"{'Chủ xe':<25} |")
            print("-" * len(header))
            print(header)
            print("-" * len(header))
            for vehicle in parking_smart:
                print(f"| {vehicle['id']:<5} | "f"{vehicle['type']:<20} | "f"{vehicle['owner']:<25} |")
            print("-" * len(header))

    elif choice == "3":
        delete_id = int(input("Nhap Id xe can xoa: "))
        found_index = False
        for vehicle in parking_smart:
            if vehicle["id"] == delete_id:
                parking_smart.remove(vehicle)
                found_index = True
                print(f"Da xoa xe ID {delete_id} thanh cong!")
                break
        if not found_index:
            print("Ko tim thay xe de xoa!")

    elif choice == "4":
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon ko hop le!")