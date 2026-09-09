class Knight:
    __item_limit=10 # 비공개 클래스 속성
    
    def print_item_limit(self):
        print(Knight.__item_limit)
        
x=Knight()
x.print_item_limit()

print(Knight.__item_limit)