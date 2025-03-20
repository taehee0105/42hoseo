# 리스트 초기화
parsing_list = []
try:
    # 로그 파일 열기기
    with open(r"C:\Users\HOSEO\Desktop\42호서\42호서\문제풀이\2week\mission_computer_main.log", 'r', encoding = 'utf-8') as file:
        # 줄마다 ',' 파싱 후 제거
        for line in file:
            # 세 개의 필드로 분리 (최대 2번의 split)
            file_line = line.strip().split(',', 2)
            if len(file_line) == 3:
                parsing_list.append({
                    "timestamp": file_line[0],
                    "event": file_line[1],
                    "message": file_line[2]
                })
        
        # 리스트 객체 화면 출력
        print('리스트 객체 화면 출력\n\n', parsing_list)
        print('\n\n')

        # 역순 정렬 문제
        print('역순 정렬\n')
        # lambda는 한 줄짜리 짧은 함수로 사용 (lambda 매개변수: 반환값)
        # 리스트의 timestamp를 기준으로 내림차순 정렬
        print_reverse_sort = sorted(parsing_list, key=lambda x: x["timestamp"], reverse=True)
        print(print_reverse_sort)
        print('\n\n')

        # 리스트 객체를 Dict 객체로 전환 문제
        print('Dict 변환\n')
        # timestamp를 키로, event와 message를 값으로 저장
        # entry로 각 키에 접근
        change_list_dict = {}
        for entry in print_reverse_sort:
            change_list_dict[entry["timestamp"]] = {"event": entry["event"], "message": entry["message"]}

        print(change_list_dict)
        print('\n\n')

        # 사전 객체(change_list_dict)를 JSON 포맷 문자열로 변환(내장 라이브러리 없이 직접 구현)
        # 여기서는 change_list_dict가 딕셔너리이며, 값은 모두 딕셔너리로 구성되어 있고 모든 값은 문자열이라고 가정
        json_string = '{\n'
        # 딕셔너리의 항목을 리스트로 변환하여 인덱스를 사용함
        items = list(change_list_dict.items())
        for idx in range(len(items)):
            timestamp, content = items[idx]
            # 키(timestamp)를 큰따옴표로 감싸고, 내부의 큰따옴표는 이스케이프 처리
            json_string += '    "' + str(timestamp) + '": {\n'
            # event 값 변환
            json_string += '        "event": "' + str(content["event"]) + '",\n'
            # message 값 변환
            json_string += '        "message": "' + str(content["message"]) + '"\n'
            json_string += '    }'
            # 마지막 항목이 아니면 콤마 추가
            if idx < len(items) - 1:
                json_string += ','
            json_string += '\n'
        json_string += '}'

        # JSON 문자열을 파일로 저장
        try:
            with open(r"C:\Users\HOSEO\Desktop\42호서\42호서\문제풀이\2week\mission_computer_main.json", 'w', encoding='utf-8') as json_file:
                json_file.write(json_string)
        except FileNotFoundError:
            print('json 파일을 찾을 수 없음')
        except Exception as e:
            print('json file 오류 발생: ', e)

# 파일 예외처리
except FileNotFoundError:
    print('로그 파일을 찾을 수 없음')
except Exception as e:
    print('log file 오류 발생: ', e)

# change_list_dict에서 event 또는 message에 입력 문자열이 포함된 항목 찾기
search_str = input('검색할 문자열을 입력하세요: ')
found = False
# 딕셔너리 항목 순회
for timestamp in change_list_dict:
    if search_str in change_list_dict[timestamp]["event"] or search_str in change_list_dict[timestamp]["message"]:
        print(timestamp, ":", change_list_dict[timestamp])
        found = True
if not found:
    print('해당 문자열을 포함하는 로그가 없습니다.')