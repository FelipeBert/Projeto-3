import tkinter as tk
from tkinter import *
import threading
import numpy as np
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys

mp_pose = mp.solutions.pose
color = (0, 0, 255)

window = tk.Tk()

def init(window):
    width= window.winfo_screenwidth()  
    height= window.winfo_screenheight() 
    window.geometry("%dx%d" % (width, height)) 
    window.title("Shape Motion")
    window.iconbitmap("images/ShapeMotion.ico")
    background_img = PhotoImage(file = f"images/background.png")
    label_background = Label(window, image=background_img).pack()

    textUpChallenger = tk.Label(
        window,
        font=("Cabin-Bold", int(18.0)),
        text="Em Breve",
        background="#1c1c1c",
        foreground="#ffffff"
        )
    textUpChallenger.place(x=96,y=350)

    textCommunity = tk.Label(
        window,
        font=("Cabin-Bold", int(18.0)),
        text="Comunidade",
        background="#1c1c1c",
        foreground="#ffffff"
        )
    textCommunity.place(x=96,y=50)

    img0 = PhotoImage(file = f"images/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 20, y = 175,
        width = 28.5,
        height = 27)

    img1 = PhotoImage(file = f"images/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 7, y = 670,
        width=45,
        height=30
        )

    img2 = PhotoImage(file = f"images/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 19, y = 97,
        width = 28,
        height = 28)

    img3 = PhotoImage(file = f"images/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_clicked_home(window),
        relief = "flat")

    b3.place(
        x = 20, y = 22,
        width = 28,
        height = 28)

    img4 = PhotoImage(file = f"images/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img4,
        relief = "flat")

    b4.place(
        x = 67,
        y = 96,
        width=300,
        height=200
    )

    img5 = PhotoImage(file = f"images/img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b5.place(
        x = 1754, y = 103,
        width = 86,
        height = 86)

    img6 = PhotoImage(file = f"images/img6.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b6.place(
        x = 1773, y = 733,
        width = 55,
        height = 39)

    botoes = [b0, b1, b2, b3, b4, b5, b6]

    for botao in botoes:
        botao.bind("<Enter>", destacar_botao)
        botao.bind("<Leave>", remover_destaque_botao)

    window.mainloop()

def btn_clicked():
    print("Botão Clicado")

def btn_clicked_img4():
    selecao(window)

def btn_clicked_home(window):
    for widget in window.winfo_children():
        widget.destroy()
    init(window)

def selecao(window):
    for widget in window.winfo_children():
        widget.destroy()

    width= window.winfo_screenwidth()  
    height= window.winfo_screenheight() 
    window.geometry("%dx%d" % (width, height)) 
    window.title("Shape Motion")
    window.iconbitmap("images/ShapeMotion.ico")

    background2_img = PhotoImage(file = f"images/background2.png")
    label_background2 = Label(window, image=background2_img).pack()

    textSelecExer = tk.Label(
        window,
        font=("Cabin-Bold", int(25.0)),
        text="Selecine seu exercicio:",
        background="#1c1c1c",
        foreground="#ffffff"
        )
    textSelecExer.place(x=96,y=50)

    img0 = PhotoImage(file = f"images/img9.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_clicked_home(window),
        relief = "flat")

    b0.place(
        x = 20, y = 20,
        width = 28,
        height = 28)

    img1 = PhotoImage(file = f"images/img10.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 19, y = 103,
        width = 28,
        height = 28)

    img2 = PhotoImage(file = f"images/img11.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 20, y = 184,
        width = 27,
        height = 27)

    img3 = PhotoImage(file = f"images/img12.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 7, y = 670,
        width=45,
        height=30)

    img4 = PhotoImage(file = f"images/img13.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img13,
        relief = "flat")

    b4.place(
        x = 500, y = 184,
        width = 300,
        height = 200)

    img5 = PhotoImage(file = f"images/img14.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img14,
        relief = "flat")

    b5.place(
        x = 114, y = 184,
        width = 300,
        height = 200)

    img6 = PhotoImage(file = f"images/img15.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img15,
        relief = "flat")

    b6.place(
        x = 886, y = 184,
        width = 300,
        height = 200)

    img7 = PhotoImage(file = f"images/img7.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img7,
        relief = "flat")

    b7.place(
        x = 114, y = 394,
        width = 300,
        height = 200)

    img8 = PhotoImage(file = f"images/img8.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_img8,
        relief = "flat")

    b8.place(
        x = 500, y = 394,
        width = 300,
        height = 200)

    botoes = [b0, b1, b2, b3, b4, b5, b6, b7, b8]

    for botao in botoes:
        botao.bind("<Enter>", destacar_botao)
        botao.bind("<Leave>", remover_destaque_botao)

    #window.resizable(False, False)
    window.mainloop()

def btn_clicked_img15():
    exercise_type = "push-up"
    root_value = "root_value"

    inicio(exercise_type, root_value)

def btn_clicked_img14():
    exercise_type = "sit-up"
    root_value = "root_value"

    inicio(exercise_type, root_value)

def btn_clicked_img13():
    exercise_type = "squat"
    root_value = "root_value"

    inicio(exercise_type, root_value)

def btn_clicked_img7():
    exercise_type = "walk"
    root_value = "root_value"

    inicio(exercise_type, root_value)

def btn_clicked_img8():
    exercise_type = "pull-up"
    root_value = "root_value"

    inicio(exercise_type, root_value)

def destacar_botao(event):
    event.widget.config(bg="gray", cursor="hand2")

def remover_destaque_botao(event):
    event.widget.config(bg="SystemButtonFace", cursor="arrow")

def inicio(exercise, root_value):
    exercise_type = exercise
    root = root_value
    
    using_webcam = True  # Fonte de vídeo é sempre webcam
    track_pose(exercise_type, using_webcam, root)

        # Inicie o rastreamento de vídeo em um thread separado
    tracking_thread = threading.Thread(target=track_pose, args=(exercise_type, using_webcam, root))
    tracking_thread.start()

class BodyPartAngle:
    def __init__(self, landmarks):
        self.landmarks = landmarks

    def angle_of_the_left_arm(self):
        l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        l_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        l_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
        return calculate_angle(l_shoulder, l_elbow, l_wrist)

    def angle_of_the_right_arm(self):
        r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        r_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        r_wrist = detection_body_part(self.landmarks, "RIGHT_WRIST")
        return calculate_angle(r_shoulder, r_elbow, r_wrist)

    def angle_of_the_left_leg(self):
        l_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        l_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        l_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        return calculate_angle(l_hip, l_knee, l_ankle)

    def angle_of_the_right_leg(self):
        r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
        r_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        r_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        return calculate_angle(r_hip, r_knee, r_ankle)

    def angle_of_the_neck(self):
        r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        r_mouth = detection_body_part(self.landmarks, "MOUTH_RIGHT")
        l_mouth = detection_body_part(self.landmarks, "MOUTH_LEFT")
        r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
        l_hip = detection_body_part(self.landmarks, "LEFT_HIP")

        shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
                        (r_shoulder[1] + l_shoulder[1]) / 2]
        mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2,
                     (r_mouth[1] + l_mouth[1]) / 2]
        hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

        return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

    def angle_of_the_abdomen(self):
        # calculate angle of the avg shoulder
        r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
                        (r_shoulder[1] + l_shoulder[1]) / 2]

        # calculate angle of the avg hip
        r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
        l_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

        # calculate angle of the avg knee
        r_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        l_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        knee_avg = [(r_knee[0] + l_knee[0]) / 2, (r_knee[1] + l_knee[1]) / 2]

        return calculate_angle(shoulder_avg, hip_avg, knee_avg)

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # check cord sys area
    if angle > 180.0:
        angle = 360 - angle

    return angle

def detection_body_part(landmarks, body_part_name):
    return [
        landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].y,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].visibility
    ]

def detection_body_parts(landmarks):
    body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

    for i, lndmrk in enumerate(mp_pose.PoseLandmark):
        lndmrk = str(lndmrk).split(".")[1]
        cord = detection_body_part(landmarks, lndmrk)
        body_parts.loc[i] = lndmrk, cord[0], cord[1]

    return body_parts

def score_table(exercise, counter, status):
    score_table = cv2.imread("./images/score_table.png")
    cv2.putText(score_table, "Activity : " + exercise.replace("-", " "),
                (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                cv2.LINE_AA)
    cv2.putText(score_table, "Counter : " + str(counter), (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
    cv2.putText(score_table, "Status : " + str(status), (10, 135),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
    cv2.imshow("Score Table", score_table)

class TypeOfExercise(BodyPartAngle):
        
    def push_up(self, counter, status):
        global color
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_left_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                color = (255, 0, 0)
                status = False
        else:
            if avg_arm_angle > 160:
                color = (0, 0, 255)
                status = True

        return [counter, status]

    def pull_up(self, counter, status):
        global color
        nose = detection_body_part(self.landmarks, "NOSE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

        if status:
            if nose[1] > avg_shoulder_y:
                counter += 1
                color = (255, 0, 0)
                status = False

        else:
            if nose[1] < avg_shoulder_y:
                color = (0, 0, 255)
                status = True

        return [counter, status]

    def squat(self, counter, status):
        global color
        left_leg_angle = self.angle_of_the_right_leg()
        right_leg_angle = self.angle_of_the_left_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:
                counter += 1
                color = (255, 0, 0)
                status = False
        else:
            if avg_leg_angle > 160:
                color = (0, 0, 255)
                status = True

        return [counter, status]

    def walk(self, counter, status):
        global color
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                color = (255, 0, 0)
                status = False

        else:
            if left_knee[0] < right_knee[0]:
                color = (0, 0, 255)
                counter += 1
                status = True

        return [counter, status]

    def sit_up(self, counter, status):
        global color
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                color = (255, 0, 0)
                status = False
        else:
            if angle > 105:
                color = (0, 0, 255)
                status = True

        return [counter, status]

    def calculate_exercise(self, exercise_type, counter, status):
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(
                counter, status)
        elif exercise_type == "pull-up":
            counter, status = TypeOfExercise(self.landmarks).pull_up(
                counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(
                counter, status)
        elif exercise_type == "walk":
            counter, status = TypeOfExercise(self.landmarks).walk(
                counter, status)
        elif exercise_type == "sit-up":
            counter, status = TypeOfExercise(self.landmarks).sit_up(
                counter, status)

        return [counter, status]

def track_pose(exercise_type, video_source, root):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)  # webcam

    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:
        counter = 0
        status = True
        while cap.isOpened():
            try:
                ret, frame = cap.read()

                frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame.flags.writeable = False

                results = pose.process(frame)

                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark
                    counter, status = TypeOfExercise(landmarks).calculate_exercise(
                        exercise_type, counter, status)
                    
                except:
                    pass

                score_table(exercise_type, counter, status)

                mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 0, 0),  # Verifique se está em vermelho
                                   thickness=2,
                                   circle_radius=2),
            mp_drawing.DrawingSpec(color=color,  # Verifique se está em azul
                                   thickness=2,
                                   circle_radius=2),
        )

                cv2.imshow('Video', frame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    print("counter: " + str(counter))
                    break
            except:
                print("err counter: " + str(counter))
                break

        cap.release()
        cv2.destroyAllWindows()
        root.destroy()

init(window)