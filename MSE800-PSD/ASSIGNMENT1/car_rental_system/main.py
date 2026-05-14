def register(username, password, role):
    db = Database()
    if db.get_user(username):
        print("Username already exists.")
        return None
    db.add_user(username, password, role)
    user = UserFactory.create_user(role, username, password)
    print(f"{role.capitalize()} {username} registered.")
    return user

def login(username, password):
    db = Database()
    user_row = db.get_user(username)
    if user_row and user_row['password'] == password:
        user = UserFactory.create_user(user_row['role'], user_row['username'], user_row['password'])
        print(f"{user.get_role().capitalize()} {username} logged in.")
        return user
    else:
        print("Invalid credentials.")
        return None

from datetime import datetime, timedelta
from car_rental_system.user_factory import UserFactory
from car_rental_system.car import Car
from car_rental_system.database import Database

def main_menu():
    print("\n==== Car Rental System ====")
    print("1. 用户注册")
    print("2. 用户登录")
    print("3. 退出")
    return input("请选择操作: ")

def user_menu(user):
    if user.get_role() == "admin":
        return admin_menu(user)
    else:
        return customer_menu(user)

def admin_menu(admin):
    while True:
        print("\n==== 管理员菜单 ====")
        print("1. 添加车辆")
        print("2. 更新车辆")
        print("3. 删除车辆")
        print("4. 审批租赁")
        print("5. 查看所有车辆")
        print("6. 登出")
        choice = input("请选择操作: ")
        if choice == "1":
            while True:
                try:
                    car_id = int(input("车辆ID: "))
                    break
                except ValueError:
                    print("车辆ID必须为整数！")
            make = input("品牌: ")
            model = input("型号: ")
            while True:
                try:
                    year = int(input("年份: "))
                    break
                except ValueError:
                    print("年份必须为整数！")
            while True:
                try:
                    mileage = int(input("里程: "))
                    break
                except ValueError:
                    print("里程必须为整数！")
            while True:
                yn = input("现在可用(y/n): ").lower()
                if yn in ['y', 'n']:
                    available_now = yn == 'y'
                    break
                else:
                    print("请输入y或n！")
            while True:
                try:
                    min_period = int(input("最短租期(天): "))
                    break
                except ValueError:
                    print("最短租期必须为整数！")
            while True:
                try:
                    max_period = int(input("最长租期(天): "))
                    break
                except ValueError:
                    print("最长租期必须为整数！")
            while True:
                try:
                    price_per_day = float(input("日租金: "))
                    break
                except ValueError:
                    print("日租金必须为数字！")
            car = Car(car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day)
            db = Database()
            db.add_car(car)
            print(f"Car {car_id} added.")
        elif choice == "2":
            while True:
                try:
                    car_id = int(input("车辆ID: "))
                    break
                except ValueError:
                    print("车辆ID必须为整数！")
            field = input("要更新的字段(make/model/year/mileage/available_now/min_period/max_period/price_per_day): ")
            value = input("新值: ")
            if field in ["year", "mileage", "min_period", "max_period"]:
                try:
                    value = int(value)
                except ValueError:
                    print("该字段必须为整数！")
                    return
            if field == "available_now":
                if value.lower() not in ['y', 'n']:
                    print("请输入y或n！")
                    return
                value = value.lower() == 'y'
            if field == "price_per_day":
                try:
                    value = float(value)
                except ValueError:
                    print("日租金必须为数字！")
                    return
            db = Database()
            db.update_car(car_id, **{field: value})
            print(f"Car {car_id} updated.")
        elif choice == "3":
            while True:
                try:
                    car_id = int(input("车辆ID: "))
                    break
                except ValueError:
                    print("车辆ID必须为整数！")
            db = Database()
            db.delete_car(car_id)
            print(f"Car {car_id} deleted.")
        elif choice == "4":
            db = Database()
            for r in db.get_all_rentals():
                print(f"Rental {r[0]}: {r[2]} by {r[1]} ({r[5]}, {r[6]}) from {r[3]} to {r[4]}, Status: {r[7]}, Fee: {r[8]}")
            while True:
                try:
                    rental_id = int(input("要审批的租赁ID: "))
                    break
                except ValueError:
                    print("租赁ID必须为整数！")
            while True:
                yn = input("批准(y)还是拒绝(n): ").lower()
                if yn in ['y', 'n']:
                    approve = yn == 'y'
                    break
                else:
                    print("请输入y或n！")
            db.update_rental_status(rental_id, "approved" if approve else "rejected")
            print(f"Rental {rental_id} {'approved' if approve else 'rejected'}.")
        elif choice == "5":
            db = Database()
            print("\n--- 所有车辆 ---")
            for c in db.get_all_cars():
                print(f"{c[0]}: {c[1]} {c[2]} ({c[3]}), Mileage: {c[4]}, Price/Day: {c[8]}, Available: {bool(c[5])}")
        elif choice == "6":
            print("已登出\n")
            break
        else:
            print("无效选择")

def customer_menu(customer):
    while True:
        print("\n==== 客户菜单 ====")
        print("1. 查看可用车辆")
        print("2. 预订车辆")
        print("3. 查看我的租赁")
        print("4. 登出")
        choice = input("请选择操作: ")
        if choice == "1":
            db = Database()
            for c in db.get_all_cars():
                if c[5]:
                    print(f"{c[0]}: {c[1]} {c[2]} ({c[3]}), Mileage: {c[4]}, Price/Day: {c[8]}, Available: {bool(c[5])}")
        elif choice == "2":
            while True:
                try:
                    car_id = int(input("车辆ID: "))
                    break
                except ValueError:
                    print("车辆ID必须为整数！")
            while True:
                name = input("您的姓名: ")
                if len(name.strip()) == 0:
                    print("姓名不能为空！")
                else:
                    break
            while True:
                phone = input("手机号: ")
                if not phone.isdigit() or len(phone) < 7:
                    print("手机号必须为7位及以上数字！")
                else:
                    break
            while True:
                start = input("开始日期(YYYY-MM-DD): ")
                try:
                    start_date = datetime.strptime(start, "%Y-%m-%d")
                    break
                except ValueError:
                    print("日期格式错误，应为YYYY-MM-DD！")
            while True:
                end = input("结束日期(YYYY-MM-DD): ")
                try:
                    end_date = datetime.strptime(end, "%Y-%m-%d")
                    if end_date <= start_date:
                        print("结束日期必须晚于开始日期！")
                        continue
                    break
                except ValueError:
                    print("日期格式错误，应为YYYY-MM-DD！")
            db = Database()
            car_row = db.get_car(car_id)
            if not car_row or not car_row[5]:
                print("Car not available.")
                return
            from car_rental_system.rental import Rental
            rental_id = None # 由数据库自增
            rental = Rental(rental_id, customer.username, car_id, start_date, end_date, name, phone)
            db.add_rental(rental)
            print(f"Rental request submitted.")
        elif choice == "3":
            db = Database()
            for r in db.get_rentals_by_customer(customer.username):
                print(f"Rental {r[0]}: {r[2]} by {r[1]} ({r[5]}, {r[6]}) from {r[3]} to {r[4]}, Status: {r[7]}, Fee: {r[8]}")
        elif choice == "4":
            print("已登出\n")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    db = Database()
    # 预置一个管理员账号
    if not db.get_user("admin1"):
        register("admin1", "adminpass", "admin")
    current_user = None
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                username = input("用户名: ")
                if len(username.strip()) == 0:
                    print("用户名不能为空！")
                else:
                    break
            while True:
                password = input("密码: ")
                if len(password) < 4:
                    print("密码长度不能小于4位！")
                else:
                    break
            while True:
                role = input("角色(admin/customer): ").lower()
                if role not in ["admin", "customer"]:
                    print("角色只能是admin或customer！")
                else:
                    break
            register(username, password, role)
        elif choice == "2":
            username = input("用户名: ")
            password = input("密码: ")
            user = login(username, password)
            if user:
                user_menu(user)
        elif choice == "3":
            print("再见！")
            break
        else:
            print("无效选择")
