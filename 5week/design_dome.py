import numpy as np

# CSV에서 strength 값만 읽기
arr1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', skip_header=1, usecols=1)
arr2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', skip_header=1, usecols=1)
arr3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', skip_header=1, usecols=1)

# 세 배열 합치기
parts = np.concatenate((arr1, arr2, arr3), axis=0)

# 평균값 계산 (단일 열이므로 값 자체가 평균 역할)
avg_values = parts

# 평균값이 50보다 작은 값만 필터링
low_avg_parts = parts[avg_values < 50]

# 조건에 맞는 파일 저장
np.savetxt('parts_to_work_on.csv', low_avg_parts, fmt='%.5f', delimiter=',')

# 보너스 과제: parts_to_work_on.csv 다시 읽기
parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')

# 평균값 계산 후 parts3에 저장하고 출력
parts3 = np.mean(parts2)
print("parts3 (평균값):", parts3)