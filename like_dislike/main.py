import tkinter
from PIL import ImageTk, Image
import os

# Абсолютный путь к скрипту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def like():
    """"обработка нажатия на кнопку лайк

    :return:

    """
    global total_likes, likes_label, current_image_index
    total_likes += 1
    likes_label.config(text=f'Лайков: {total_likes}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    update_image()


def dislike():
    """"обработка нажатия на кнопку дизлайк

    :return:

    """
    global total_dislikes, dislike_label, current_image_index
    total_dislikes += 1
    dislike_label.config(text=f'Дизлайков: {total_dislikes}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    update_image()


def update_image():
    """"
    Обновление изображения

    :return:
    """
    # путь к конкретному изображению
    image_path = os.path.join(image_directory, images_filenames[current_image_index])

    # маштабирование полученного изображения и отображения
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo


total_likes = 0
total_dislikes = 0
current_image_index = 0  # индекс пути к отографии

image_directory = os.path.join(BASE_DIR, 'images')  # Абсолютный путь к папке с изображениями
images_filenames = sorted(os.listdir(image_directory))  # Список с изображениями

root = tkinter.Tk()
root.title('лайк-дизлайк')
root.geometry('400x450')
root.resizable(False, False)

# путь к конкретному изображению
image_path = os.path.join(image_directory, images_filenames[current_image_index])

# маштабирование полученного изображения и отображения
image = Image.open(image_path)
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tkinter.Label(image=photo)
image_label.pack(pady=10)

# добавляем изображение лайка и дизлайка
like_image = Image.open(os.path.join(BASE_DIR, 'like.png'))
dislike_image = Image.open(os.path.join(BASE_DIR, 'dislike.png'))

# маштабирование изображений
like_image = like_image.resize((100, 100), Image.LANCZOS)
dislike_image = dislike_image.resize((100, 100), Image.LANCZOS)

# конвертирование под Tkinter
like_image = ImageTk.PhotoImage(like_image)
dislike_image = ImageTk.PhotoImage(dislike_image)

# cоздаем фрейм для кнопок
buttos_frame = tkinter.Frame(root)
buttos_frame.pack(pady=20)

# создаем и размещаем кнопку лайк
like_buttom = tkinter.Button(buttos_frame, image=like_image, bd=0, command=like)
like_buttom.pack(side=tkinter.LEFT, padx=10)

# cоздаем и размещаем кнопку дизлайк
dislike_buttom = tkinter.Button(buttos_frame, image=dislike_image, bd=0, command=dislike)
dislike_buttom.pack(side=tkinter.LEFT, padx=10)

# создаем контейнер для количества лайков
likes_label = tkinter.Label(root, text='лайков: 0', font=('Arial', 14))
likes_label.pack()

# Создаем контейнер для количества дизлайков
dislike_label = tkinter.Label(root, text='дизлайков: 0', font=('Arial', 14))
dislike_label.pack()

root.mainloop()
