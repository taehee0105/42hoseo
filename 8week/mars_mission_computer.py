import platform  # 운영체제 정보를 가져오기 위한 모듈
import os  # CPU 코어 수를 가져오기 위한 모듈
import time  # 시간 측정을 위한 모듈
import psutil  # 시스템 메모리 및 CPU 사용량을 가져오기 위한 모듈

class DummySensor:
    def __init__(self):
        # 초기 난수 시드를 현재 시간으로 설정
        self.seed = int(time.time())

    def simple_random(self, min_value, max_value):
        # 난수 생성기 (Linear Congruential Generator, LCG)
        self.seed = (self.seed * 1664525 + 1013904223) % (2**32)
        fraction = self.seed / (2**32)  # 0.0 ~ 1.0 범위의 난수 생성
        return round(min_value + (max_value - min_value) * fraction, 2)

    def get_internal_temperature(self):
        # 내부 온도 (15.0 ~ 25.0도)
        return self.simple_random(15.0, 25.0)

    def get_external_temperature(self):
        # 외부 온도 (-80.0 ~ 0.0도)
        return self.simple_random(-80.0, 0.0)

    def get_internal_humidity(self):
        # 내부 습도 (20.0 ~ 60.0%)
        return self.simple_random(20.0, 60.0)

    def get_external_illuminance(self):
        # 외부 광량 (0.0 ~ 50000.0 럭스)
        return self.simple_random(0.0, 50000.0)

    def get_internal_co2(self):
        # 내부 이산화탄소 농도 (300.0 ~ 1000.0 ppm)
        return self.simple_random(300.0, 1000.0)

    def get_internal_oxygen(self):
        # 내부 산소 농도 (19.0 ~ 23.0%)
        return self.simple_random(19.0, 23.0)

class MissionComputer:
    def __init__(self):
        # 환경 정보를 저장하는 딕셔너리
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }
        # DummySensor 인스턴스를 ds로 초기화
        self.ds = DummySensor()
        # 5분 평균 계산을 위한 시작 시간 초기화
        self.start_time = time.time()
        # 환경 데이터 로그 (5분 평균 계산용) 초기화
        self.data_log = {key: [] for key in self.env_values}

    def format_to_json(self, data):
        # 딕셔너리를 JSON 형식의 문자열로 변환 (json 모듈 사용 없이 직접 구현)
        json_str = '{\n'
        for key, value in data.items():
            json_str += f'    "{key}": {value},\n'
        # 마지막 쉼표 제거
        json_str = json_str.rstrip(',\n') + '\n}'
        return json_str

    def get_mission_computer_info(self):
        try:
            # 시스템 정보를 딕셔너리 형태로 수집
            system_info = {
                'operating_system': platform.system(),  # 운영체제 이름
                'os_version': platform.version(),  # 운영체제 버전
                'cpu_type': platform.processor(),  # CPU 타입
                'cpu_core_count': os.cpu_count(),  # CPU 코어 수
                'memory_size': f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"  # 시스템 메모리 크기
            }
            # JSON 형식으로 출력 (json 모듈 없이 직접 변환)
            print(self.format_to_json(system_info))
        except Exception as e:
            # 오류 메시지 출력
            print(f"[ERROR] 시스템 정보를 가져오는 중 오류가 발생했습니다: {e}")

    def get_mission_computer_load(self):
        try:
            # 시스템 부하 정보를 딕셔너리 형태로 수집 (cross-platform)
            load_info = {
                'cpu_usage_percent': psutil.cpu_percent(interval=1),  # CPU 사용량 (1초 평균)
                'memory_usage_percent': psutil.virtual_memory().percent  # 메모리 사용량
            }
            # JSON 형식으로 출력 (json 모듈 없이 직접 변환)
            print(self.format_to_json(load_info))
        except Exception as e:
            # 오류 메시지 출력
            print(f"[ERROR] 시스템 부하 정보를 가져오는 중 오류가 발생했습니다: {e}")

# MissionComputer 인스턴스 생성
runComputer = MissionComputer()

# 시스템 정보 출력
runComputer.get_mission_computer_info()

# 시스템 부하 정보 출력
runComputer.get_mission_computer_load()
