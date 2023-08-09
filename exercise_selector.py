import tkinter as tk

class ExerciseSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise Selector")

        self.exercise_type = None

        self.label = tk.Label(root, text="Selecione o exercício:")
        self.label.pack()

        self.push_up_button = tk.Button(root, text="Push-Up", command=self.select_push_up)
        self.push_up_button.pack()

        self.pull_up_button = tk.Button(root, text="Pull-Up", command=self.select_pull_up)
        self.pull_up_button.pack()

        self.sit_up_button = tk.Button(root, text="Sit-Up", command=self.select_sit_up)
        self.sit_up_button.pack()

        self.squat_button = tk.Button(root, text="Squat", command=self.select_squat)
        self.squat_button.pack()

        self.walk_button = tk.Button(root, text="Walk", command=self.select_walk)
        self.walk_button.pack()

    def select_push_up(self):
        self.exercise_type = "push-up"
        self.root.destroy()

    def select_walk(self):
        self.exercise_type = "walk"
        self.root.destroy()

    def select_pull_up(self):
        self.exercise_type = "pull-up"
        self.root.destroy()
    
    def select_sit_up(self):
        self.exercise_type = "sit-up"
        self.root.destroy()
    
    def select_squat(self):
        self.exercise_type = "squat"
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExerciseSelector(root)
    root.mainloop()

    # Depois que a janela é fechada, envie o exercício selecionado para o script principal
    if app.exercise_type:
        print("Exercício selecionado:", app.exercise_type)
        # Agora você pode iniciar o rastreamento de vídeo com o exercício selecionado no script principal
