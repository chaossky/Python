lines=['안녕하세요?\n','만나서 반갑습니다.\n','잘 지내보아요.\n']

with open('hi_list.txt','w') as file:
    file.writelines(lines)
    