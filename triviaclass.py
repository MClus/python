import sys, pygame
from pygame.locals import *

class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False 
        self.failed = False 
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        f = open(filename, 'r')
        trivate_data = f.readlines()
        f.close()

        for text_line in trivate_data:
            self.data.append(text_line.strip())
            self.total += 1 

    def show_question(self):
        print_text(font1, 210, 5, 'TRIVA GAME')
        print_text(font2, 190, 500-20, 'Press Keys (1-4) To Answer', purple)
        print_text(font2, 530, 5, 'SCORE', purple)
        print_text(font2, 550, 25, str(self.score), purple)
        
        self.correct = int(self.data[self.current+5])

        question = self.current // 6 + 1
        print_text(font1, 5, 80, 'QUESTION' + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct-1] = green
            print_text(font1, 230, 380, 'CORRECT', green)
            print_text(font2, 170, 420, 'Press Enter For Next Question', green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.correct-1] = red 
            print_text(font1, 230, 380, 'INCORRECT', red)
            print_text(font2, 170, 420, 'Press Enter For Next Question', red)

        print_text(font1, 5, 170, 'ANSWER')
        print_text(font2, 20, 210, '1 - ' + self.data[self.current+1], self.colors[0])
        print_text(font2, 20, 240, '2 - ' + self.data[self.current+2], self.colors[1])
        print_text(font2, 20, 270, '3 - ' + self.data[self.current+3], self.colors[2])
        print_text(font2, 20, 300, '4 - ' + self.data[self.current+4], self.colors[3])

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.score = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.color = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0
