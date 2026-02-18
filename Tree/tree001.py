import matplotlib.pyplot as plt, math

def branch(x,y,l,a):
    if l<5: return
    x2,y2=x+l*math.cos(a),y+l*math.sin(a)
    plt.plot([x,x2],[y,y2],"brown")
    branch(x2,y2,l*0.7,a+0.5)
    branch(x2,y2,l*0.7,a-0.5)

branch(0,0,60,math.pi/2)
plt.axis("off")
plt.show()
