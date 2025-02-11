import time

class Pomodoro:
    def __init__(self):
        self.trabalho = 25 * 60  # 25 minutos em segundos
        self.descanso = 5 * 60  # 5 minutos em segundos
        self.ciclo = 0

    def iniciar(self):
        while True:
            self.ciclo += 1
            print(f"Ciclo {self.ciclo}: Trabalho")
            self.contagem_regressiva(self.trabalho)
            print("Descanso!")
            self.contagem_regressiva(self.descanso)
            print("Próximo ciclo!")

    def contagem_regressiva(self, tempo):
        for i in range(tempo, 0, -1):
            minutos, segundos = divmod(i, 60)
            print(f"{minutos:02d}:{segundos:02d}", end="\r")
            time.sleep(1)
        print()

if __name__ == "__main__":
    pomodoro = Pomodoro()
    pomodoro.iniciar()