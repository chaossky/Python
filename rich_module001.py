import time
from rich import print
from rich.table import Table
from rich.progress import track
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown
md = Markdown("# 제목\n- 리스트 항목\n**굵은 글씨**")
print(md)
code = """def hello():\n    print("Hello, world!")"""
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
print(syntax)

print(Panel("이건 패널 안의 텍스트입니다", title="패널 제목"))

for step in track(range(100), description="처리 중..."):
    time.sleep(0.1)

table=Table(title="예시 테이블")

table.add_column("이름",style="cyan")
table.add_column("나이",justify="right",style="magenta")
table.add_row("장훈","29")
table.add_row("민수","34")

print(table)
print("[bold magenta]Hello, Rich![/bold magenta] 😎")
