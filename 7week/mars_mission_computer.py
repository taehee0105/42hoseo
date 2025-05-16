import time

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
        # 5분 평균 계산을 위한 시작 시간
        self.start_time = time.time()
        # 환경 데이터 로그 (5분 평균 계산용)
        self.data_log = {key: [] for key in self.env_values}

    def format_to_json(self):
        # env_values 딕셔너리를 JSON 형식의 문자열로 변환
        json_str = '{\n'
        for key, value in self.env_values.items():
            json_str += f'    "{key}": {value},\n'
        # 마지막 쉼표 제거
        json_str = json_str.rstrip(',\n') + '\n}'
        return json_str

    def get_sensor_data(self):
        try:
            while True:
                # 센서 데이터 업데이트 (ds를 사용)
                self.env_values['mars_base_internal_temperature'] = self.ds.get_internal_temperature()
                self.env_values['mars_base_external_temperature'] = self.ds.get_external_temperature()
                self.env_values['mars_base_internal_humidity'] = self.ds.get_internal_humidity()
                self.env_values['mars_base_external_illuminance'] = self.ds.get_external_illuminance()
                self.env_values['mars_base_internal_co2'] = self.ds.get_internal_co2()
                self.env_values['mars_base_internal_oxygen'] = self.ds.get_internal_oxygen()

                # JSON 형식으로 환경 정보 출력
                print(self.format_to_json())

                # 환경 데이터 로그에 추가 (5분 평균 계산용)
                for key, value in self.env_values.items():
                    self.data_log[key].append(value)

                # 5분 평균 계산
                if time.time() - self.start_time >= 300:
                    print('\n[5분 평균 값]')
                    for key, values in self.data_log.items():
                        if values:
                            avg_value = sum(values) / len(values)
                            print(f'{key}: {avg_value:.2f}')
                    # 데이터 로그 초기화
                    self.data_log = {key: [] for key in self.env_values}
                    self.start_time = time.time()

                # 5초 대기
                time.sleep(5)

        except KeyboardInterrupt:
            # 프로그램 종료 메시지 출력
            print('\nSytem stoped…')


# 미션 컴퓨터 실행
if __name__ == '__main__':
    # MissionComputer 인스턴스 생성
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()
