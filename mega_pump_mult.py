# 최초의 자리 0,0 자리로 이동 시키는 함수
def back(x=0,y=0):
	while x!=get_pos_x() or y!=get_pos_y(): #(0,0)자리 가 아닐때
		while get_pos_x()!=x: 				# x 가 0아닌 동안에
			if(get_pos_x()<x):				# 좌표가 0보다 작으면 동쪽으로 이동(오른쪽)
				moveEx(East)
			else:
				moveEx(West)				#왼쪽으로 이동(서쪽)
		while get_pos_y()!=y:				# y의 좌표가 0이 아니면
			if(get_pos_y()<y):				# 위쪽 ( 북쪽)으로 이동
				moveEx(North)
			else:
				moveEx(South)				#아래쪽 (남쪽)으로 이동

def moveEx(dir):
    dirs = [East, South, West, North]   # 네 방향을 리스트로 준비
    dirs.remove(dir)                    # 현재 시도할 방향(dir)을 제외
    if (not move(dir)):                 # 먼저 dir 방향으로 이동 시도
        if (not move(dirs[0])):         # 실패하면 dirs[0] 방향으로 이동 시도
            if (not move(dirs[1])):     # 또 실패하면 dirs[1] 방향으로 이동 시도
                if (not move(dirs[2])): # 마지막으로 dirs[2] 방향으로 이동 시도
                    return False        # 네 방향 모두 실패하면 False 반환
	
def do(x,worldsize=0):
	if worldsize == 0:
		worldsize=get_world_size()
	dir=East
	for i in range(worldsize):
		for j in range(worldsize-1):
			x()
			move(dir)
		x()
		move(North)
		if(dir==East):
			dir=West
		else:
			dir=East

# --- Pumpkin Logic Start ---
def plantpumpkin():
	plant(Entities.Pumpkin) 

def doPumpkin():
	back()
	success = []
	def adddie():
		if not can_harvest():
			success.append({"x":get_pos_x(),"y":get_pos_y()})
			plantpumpkin()

	def removedie():
		if(can_harvest()):
			success.remove({"x":get_pos_x(),"y":get_pos_y()})
		else:
			plantpumpkin()

	def plantonce(x):
		dir = East
		for i in range(get_world_size()):
			for j in range(get_world_size()-1):
				x()
				move(dir)
			x()
			move(North)
			if dir == East:
				dir=West
			else:
				dir=East
	
	plantonce(plantpumpkin) # First planting
	back()
	plantonce(adddie) # Check for failures
	
	# Keep fixing specific spots
	while(len(success) != 0):
		for pos in success:
			back(pos["x"],pos["y"])
			removedie()

	return len(success)==0

def pumpProject():
	# Helper to till ground first
	def tillx():
		if(get_ground_type()==Grounds.Grassland):
			till()
	back()
	do(tillx)
	
	while True:
		# Wait until doPumpkin returns true (all spots ready)
		while doPumpkin():
			back()
			harvest()
# --- Pumpkin Logic End ---

# Start the bot
set_world_size(32)
clear()
pumpProject()