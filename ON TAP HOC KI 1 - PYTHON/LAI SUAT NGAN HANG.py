tienGui, soThang = int(input()), int(input())
if tienGui < 1000000000:
    if soThang <= 2: laiSuat = 2.5 / 100.0
    elif 3 <= soThang <= 6: laiSuat = 3.9 / 100.0
    elif 7 <= soThang <= 12: laiSuat = 4.8 / 100.0
    elif 13 <= soThang <= 36: laiSuat = 4.8 / 100.0
    else: laiSuat = 4.7 / 100.0
elif 1000000000 <= tienGui < 3000000000:
    if soThang <= 2: laiSuat = 2.7 / 100.0
    elif 3 <= soThang <= 6: laiSuat = 4.1 / 100.0
    elif 7 <= soThang <= 12: laiSuat = 4.9 / 100.0            
    elif 13 <= soThang <= 36: laiSuat = 5.0 / 100.0            
    else: laiSuat = 4.9 / 100.0            
else:  
    if soThang <= 2: laiSuat = 2.8 / 100.0            
    elif 3 <= soThang <= 6: laiSuat = 4.3 / 100.0            
    elif 7 <= soThang <= 12: laiSuat = 5.0 / 100.0            
    elif 13 <= soThang <= 36: laiSuat = 5.1 / 100.0           
    else: laiSuat = 5.0 / 100.0 
tienLai = tienGui * laiSuat * soThang / 12
print(int(tienLai))

            