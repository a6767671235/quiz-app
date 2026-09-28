import pgzrun 

TITLE="quiz master"
WIDTH=870
HEIGTH=650

marquee_box=Rect(0, 0, 880, 80)
question_box=Rect(0, 0, 650, 150)
timer_box=Rect(0, 0, 150, 150)
anwer_box1=Rect(0, 0, 300, 150)
anwer_box2=Rect(0, 0, 300, 150)
anwer_box3=Rect(0, 0, 300, 150)
anwer_box=Rect(0, 0, 300, 150)
skip_box=Rect(0, 0, 150, 330)

score=0
time_left=0
question_file_name="questions.txt"
marquee_message=""
is_game_over=False

anwer_boxes=[anwer_box1, anwer_box2, anwer_box3, anwer_box4]
questions=[]
question_count=0
question_index=0

marquee_box.move_ip(0,0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
anwer_box1._ip(20,270)
anwer_box2._ip(370,270)
anwer_box3._ip(20,450)
anwer_box4._ip(370,450)
skip_box.move_ip(700, 270)

def draw():
    global marquee_message
    screen.clear
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.filled.rect(timer_box,"navy blue")
    screen.filled.rect(skip_box,"dark green")

for answer_box in anwer_boxes:
    sreen.draw.fillled_rect(anwer_box, dark orange)

    marquee_message="welcome to Quiz master........."
    marquee_message=marquee_message+f"{question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box, color="white")
    screen.draw.textbox()