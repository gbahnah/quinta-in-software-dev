import tkinter as tk
from tkinter import ttk
import reflection_questions.design as drq


class ReflectionPage(ttk.Frame):
    """A general page of reflection questions."""

    def __init__(self, parent, controller) -> None:
        ttk.Frame.__init__(self, parent)
        ttk.Button(self, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=0, row=0)
        self.controller = controller
        self.canvas = tk.Canvas(self)
        self.canvas.grid(column=0, row=1, sticky='nsew')
        scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.grid(column=1, row=0, sticky='ns')
        # self.canvas.configure(yscrollcommand=scrollbar.set)
        self.question_frame = ttk.Frame(self.canvas)
        self.canvas.create_window(0, 0, window=self.question_frame, anchor='nw')
        self.question_frame.bind('<Configure>', lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))

        self.question_frame.bind('<Configure', self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))
    
    


class DesignReflectionPage(ReflectionPage):
    """A reflection page for design."""

    def __init__(self, parent, controller) -> None:
        ReflectionPage.__init__(self, parent, controller)
        questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT,
                     drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]
        ttk.Label(self.question_frame, text='Design: Reflection').grid(
            column=0, row=0)
        text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(text_questions.values(), 1):
            text_question.show(0, 2*i)


class TextQuestion:
    """A question and a textbox to answer it."""

    def __init__(self, parent, question) -> None:
        self.label = ttk.Label(parent, text=question, wraplength='20cm')
        self.textbox = tk.Text(parent)

    def show(self, column, row):
        """Show the question and answer on screen."""
        self.label.grid(column=column, row=row, sticky='ew')
        self.textbox.grid(column=column, row=row+1, sticky='ew')
