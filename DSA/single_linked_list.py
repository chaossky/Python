# 단일 연결 리스트 클래스
class SLinkedList:

    # 노드 클래스
    class Node:
        # 노드 클래스 생성자
        def __init__(self,value,next=None):
            self.value=value #저장된 데이터
            self.next=next #다음 노드를 가리키는 변수
            #print("노드 생성")

    # 단일 연결 리스트 클래스 생성자
    def __init__(self):
        self.head=None # 첫 생성시 내부에는 노드가 없다.
        #print("단일연결리스트 생성")
    
    def insertNode(self,value):
        # 만일 첫번째 Node 라면 ->head가 None
        if self.head is None:
            # head에 새 Node를 저장
            self.head=self.Node(value)
        else: # 이미 생성된 node가 있다면
            # head에 새 Node를 저장
            # 기존의 head에 저장된 node는 새로 생성할 노드의 next로 저장
            self.head=self.Node(value,self.head)

        #self.printNode()

    def printNode(self):
        # 저장된 데이타(node)가 없을때
        if self.head is None:
            print("저장된 데이타가 없습니다.")
            return
        else:
            print("<현재 전체 노드 구조>",end='\t')
            link=self.head #처음은 head를 지정, 이후 부터 현 node의 next를 지정
            # link가 가리키는 node가 없을때 까지 반복
            # None, 0,"" 는 조건 판단에서 False처리, 그외는 True로 처리
            while link:
                print(link.value,'->',end=' ')
                link=link.next # link를 현 위치 node의 next로 변경
                #print() #줄바꿈
            print("None")
    
    def deleteNode(self):
        # 노드가 없으면 skip
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            # head를 현재 head의 next, 즉 다음 노드로 변경
            self.head=self.head.next
            print("노드 삭제")

    def searchNode(self,value):
        # 데이타가 없을때 
        if self.head is None:
            print("저장된 데이타가 없습니다.")
            return
        else:
            link=self.head # 처음은 head로 지정. 이후 현 node를 next로 지정
            index=0 # 몇 번째 node인지를 기록
            while link:
                # 내가 찾는 값인지를 파악
                if value ==link.value:
                    return index # 위치 값을 반환
                else: #찾는 값이 없으면 다음 node로 이동
                    link=link.next # link를 현 위치의 node로 이동
                    index +=1 # 위치 값 1 증가

            # 일치하는 값이 없다면 
            print("일치하는 값이 없습니다.")



#테스트

if __name__=="__main__":
    sl = SLinkedList()
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')
    sl.printNode()  # 출력
    # sl.deleteNode()
    # sl.deleteNode()
    # sl.printNode()  # 출력
    # sl.deleteNode()
    # sl.deleteNode()
    # sl.printNode()  # 출력
   
    #탐색
    # print("<위치 탐색>")
    # result = sl.searchNode('1st')
    # print("1st의 위치 : {}".format(result))

    # result = sl.searchNode('555')
    # print("555의 위치 : {}".format(result))