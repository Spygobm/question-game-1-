import pgzrun

WIDTH = 870
HIEGHT = 650

TITLE = "QUIZ GAME"
marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

score = 0 
time_left = 10
marquee_message = ""
game_over = False
question_count = 0
question_index = 0 
questions = []

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box,"white")
    screen.draw.filled_rect(question_box,"orange")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"purple")
    
    for answerbox in answer_boxes:
        screen.draw.filled_rect(answerbox,"red")
    
    #adding the text on the box 
    screen.draw.textbox("skip",skip_box,color = "black",angle = -90)
    


def update():
    pass

pgzrun.go()