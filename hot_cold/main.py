import random
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image


def generate_secret_number():
    """"Генерирует случайное число
    :return:
    """
    return random.randint(1, 100)


def check_guess(secret_number, guess):
    """Проверка введенного числа
    
    :param secret_number: Загаданное число
    :param guess: введенное число
    :return: Результат
    """
    global  guesses_taken
    if guess < secret_number:
        guesses_taken += 1
        return 'Холодно'
    elif guess > secret_number:
        guesses_taken += 1
        return 'Горячо'
    else:
        return 'Победа!'


def check_button():
    """"обработка нажатия на кнопку


    :return:
    """
    guess = int(entry.get())
    result = check_guess(secret_number=secret_number, guess=guess)
    result_label.config(text=result)
    if result == 'Победа!':
        message = f'Вы угадали  число за {guesses_taken} попыток!'
        messagebox.showinfo(title='Победа!', message= message)
        root.destroy()# отключение основного окна


root = tkinter.Tk()
root.title('Холодно - горячо')
background_image = Image.open('YAke-chyslo-najbilshe.jpg')

window_width, window_height = 1900, 1000

background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry(f'{window_width}x{window_height}')
root.resizable(False, False)  # Запрет маштабирования

# Создание виджета инструкции
instructijn_label = tkinter.Label(root, text='Я загадал число от 1 до 100 попробуй его угадать',
                                  font=('Arial', 18), bg='#EFF2F5', fg='#737373')
instructijn_label.place(relx=0.5, rely=0.4, anchor='center')

# поле для ввода числа
entry = tkinter.Entry(root, font=('Arial', 15))
entry.place(relx=0.5, rely=0.5, anchor='center')

check_buttom = tkinter.Button(root, text='Проверить', font=('Arial', 15),
                              bg='#EFF2F5', fg='#737373', activeforeground='#45A049',
                              activebackground='white', command=check_button)

check_buttom.place(relx=0.5, rely=0.6, anchor='center')

# поле для результата
result_label = tkinter.Label(root, font=('Arial', 15), fg='#737373', bg='#EFF2F5')
result_label.place(relx=0.5, rely=0.7, anchor='center')

# Инициализация переменных
secret_number = generate_secret_number()  # Случайное число
guesses_taken = 0  # кол-во попыток

root.mainloop()
