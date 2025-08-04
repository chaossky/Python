import pandas as pd

# Load the uploaded Excel file
file_path = ".xlsx"
df = pd.read_excel(file_path)

# Display the first few rows and the column names to understand the structure
df.head(), df.columns

# 열 이름 간단히 별칭 설정
school_info_col = '참가자의 소속(학생이면 학년 , 기타 선생님이나 스태프, 자원봉사이신지 등을 아래에서 선택해 주시길 바랍니다.)'
name_col = '참가자 이름 (참가하는 학생, 선생님, 자원봉사하실 보호자분의 성함을 입력해 주시길 바랍니다.)'

# 학년 정보만 필터링 (예: "초등 1학년", "중등 2학년" 등으로 시작하는 경우)
student_rows = df[df[school_info_col].str.contains('학년', na=False)]

# 학년별로 이름을 리스트로 분류
grade_groups = student_rows.groupby(school_info_col)[name_col].apply(list).to_dict()

grade_groups
