import tkinter
from PIL import ImageTk, Image


def calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        result = weight / (height ** 2)
        result_label.config(text=f'Индекс массы тела: {result:.1f}')
    except ValueError:
        result_label.config(text=f'Данные должны иметь числовой тип', fg='#FF1D18')


root = tkinter.Tk()  # Инициализация окна
root.title('Калькулятор веса')  # название приложения

# загрузка фона
background_image = Image.open('21894185_2111.w039.n003.5B.p1.5.jpg')
window_width = 800
window_height = 600
# Маштабирование изображения фона под размер окна
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry(f'{window_width}x{window_height}')  # Установка окна в пикселях
root.resizable(False, False)
# поле для ввода роста

height_label = tkinter.Label(root, text='Рост(м)', font=('Arial', 14), fg='#FFB952', bg='white')
height_label.place(relx=0.5, rely=0.4, anchor='center')  # размещение подсказки для ввода
height_entry = tkinter.Entry(root, font=('Arial', 14))
height_entry.place(relx=0.5, rely=0.45, anchor='center')
# поле для ввода веса!
weight_label = tkinter.Label(root, text='вес (кг)', font=('Arial', 14), fg='#FFB952', bg='white')
weight_label.place(relx=0.5, rely=0.5, anchor='center')
weight_entry = tkinter.Entry(root, font=('Arial', 14))
weight_entry.place(relx=0.5, rely=0.55, anchor='center')
# Кнопка для расчета веса
calculate_button = tkinter.Button(root, text='рассчитать', font=('Arial', 14), command=calculate,
                                  bg='#FFFFFF', fg='#FFB952', activebackground='#45A049', activeforeground='white')
calculate_button.place(relx=0.5, rely=0.6, anchor='center')
# Окно для вывода результатов
result_label = tkinter.Label(root, font=('Arial', 14), bg='white', fg='black')
result_label.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()
