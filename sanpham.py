# Trong code này, nhập vào một số
# Kiểm tra xem số âm hay dương
# hay bằng không và hiển thị
# number = float(input("Nhập một số: "))
# if number >= 0:
#    if number == 0:
#        print("Số Không")
#    else:
#        print("Số dương")
# else:
#    print("Số âm")
# x=2
# for i in range(x):
#     sotuoi = float(input("mời bạn nhập số tuổi:"))
# if sotuoi <=15:
#     print("tuổi trẻ em")
# elif sotuoi <=18:
#     print('tuổi thiếu niên')
# elif sotuoi <=50:
#     print('tuổi lao động')
# elif sotuoi <=70:
#     print('tuổi trung niên')
# elif sotuoi >70:
#     print('tuổi già')
# else:
#     print('không hợp lệ')
a=list(map(int,input().split()))
print(max(a))