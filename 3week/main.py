# Mars_Base_Inventory_List.csv 파일을 읽어서 리스트로 저장
inventory = []
try:
    with open('Mars_Base_Inventory_List.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            # 줄을 쉼표 기준으로 분리
            parts = line.strip().split(',')
            if len(parts) >= 5:
                # 첫 번째 열: 물질 이름
                name = parts[0].strip()
                # 다섯 번째 열: 인화성 지수
                flammability_str = parts[4].strip()
                try:
                    flammability = float(flammability_str)
                except ValueError:
                    continue
                inventory.append([name, flammability])
except FileNotFoundError:
    print('파일을 찾을 수 없습니다: Mars_Base_Inventory_List.csv')
except IOError:
    print('파일을 읽는 도중 오류가 발생했습니다: Mars_Base_Inventory_List.csv')


# 적재 화물 목록 출력
print('적재 화물 목록:')
for item in inventory:
    name = item[0]
    flammability = item[1]
    print('이름:', name, '| 인화성 지수:', flammability)


# 인화성 순으로 정렬
sorted_inventory = sorted(inventory, key=lambda item: item[1], reverse=True)


# 인화성 지수가 0.7 이상인 항목 추출
dangerous_items = []
for item in sorted_inventory:
    name = item[0]
    flammability = item[1]
    if flammability >= 0.7:
        dangerous_items.append([name, flammability])


# 인화성 지수 0.7 이상 목록 출력
print('\n인화성 지수 0.7 이상 목록:')
for item in dangerous_items:
    name = item[0]
    flammability = item[1]
    print('이름:', name, '| 인화성 지수:', flammability)


# 위험 목록을 CSV 파일로 저장
try:
    with open('Mars_Base_Inventory_danger.csv', 'w') as file:
        file.write('Substance,Flammability\n')
        for item in dangerous_items:
            name = item[0]
            flammability = item[1]
            # CSV 형식으로 저장
            file.write(f"{name},{flammability}\n")
except IOError:
    print('CSV 파일 저장 중 오류가 발생했습니다: Mars_Base_Inventory_danger.csv')


# 인화성 정렬 목록을 이진 파일로 저장
try:
    with open('Mars_Base_Inventory_List.bin', 'wb') as file:
        for item in sorted_inventory:
            name = item[0]
            flammability = item[1]
            line = f"{name},{flammability}\n"
            # 문자열을 바이너리로 인코딩 후 저장
            file.write(line.encode('utf-8'))
except IOError:
    print('이진 파일 저장 중 오류가 발생했습니다: Mars_Base_Inventory_List.bin')


# 저장된 이진 파일 내용을 다시 읽어서 출력
try:
    with open('Mars_Base_Inventory_List.bin', 'rb') as file:
        # 바이너리를 문자열로 디코딩
        data = file.read().decode('utf-8')
        print('\nMars_Base_Inventory_List.bin 내용:')
        print(data)
except FileNotFoundError:
    print('이진 파일을 찾을 수 없습니다: Mars_Base_Inventory_List.bin')
except IOError:
    print('이진 파일을 읽는 도중 오류가 발생했습니다: Mars_Base_Inventory_List.bin')
