# 전역변수 선언
material = ''
diameter = 0
thickness = 0
area = 0
weight = 0

# 재질별 밀도 (g/cm3)
DENSITY = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

# 화성 중력 보정 계수
GRAVITY_RATIO = 0.38

def sphere_area(diameter, material='유리', thickness=1):
    global area, weight

    # 반지름 계산 (m -> cm)
    radius_cm = (diameter * 100) / 2

    # 반구 표면적: 2 * π * r^2
    area_cm2 = 2 * 3.1415926535 * radius_cm ** 2

    # 부피 계산: 면적 × 두께
    volume_cm3 = area_cm2 * thickness

    # 무게 계산: 부피 × 밀도
    weight_grams = volume_cm3 * DENSITY[material]

    # 지구 무게 → 화성 무게
    weight_kg = (weight_grams / 1000) * GRAVITY_RATIO

    # 전역변수에 저장
    area = round(area_cm2, 3)
    weight = round(weight_kg, 3)

    # 결과 출력
    print(f'재질 ⇒ {material}, 지름 ⇒ {round(diameter, 3)}, 두께 ⇒ {round(thickness, 3)}, 면적 ⇒ {area}, 무게 ⇒ {weight} kg')

# 반복 실행
while True:
    print('\n돔 계산기 (종료하려면 q 입력)')

        # 지름 입력
    while True:
        d = input('지름 입력 (m): ')
        if d.lower() == 'q':
            exit()
        try:
            diameter = float(d)
            if diameter == 0:
                print('error: 지름은 0이 될 수 없음')
                continue
            break
        except ValueError:
            print('error: 지름은 숫자로 입력')

    # 재질 입력
    while True:
        m = input('재질 입력 (유리, 알루미늄, 탄소강, 기본값: 유리): ')
        if m.lower() == 'q':
            exit()
        if m.strip() == '':
            material = '유리'
            break
        elif m in DENSITY:
            material = m
            break
        else:
            print('error: 유리, 알루미늄, 탄소강 중 다시 선택')

    # 두께 입력
    while True:
        t = input('두께 입력 (cm, 기본값: 1): ')
        if t.lower() == 'q':
            exit()
        if t.strip() == '':
            thickness = 1
            break
        try:
            thickness = float(t)
            break
        except ValueError:
            print('error: 두께는 숫자로 입력')

    sphere_area(diameter, material, thickness)
