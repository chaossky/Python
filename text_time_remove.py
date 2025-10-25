import re

def remove_time_lines(input_file, output_file):
    # 시간 정보 패턴: MM:SS 또는 M:SS 형식 (예: 1:05, 12:30 등)
    time_pattern = re.compile(r'^\d{1,2}:\d{2}$')

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            stripped_line = line.strip()
            # 시간 정보 줄은 건너뛰고, 나머지만 출력
            if not time_pattern.match(stripped_line):
                outfile.write(stripped_line + '\n')

# 사용 예시
remove_time_lines('input.txt', 'output.txt')
