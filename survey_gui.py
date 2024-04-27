import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import glob
import random


class ImageDisplayApp(QWidget):
    def __init__(self, real_paths, fake_paths):
        super().__init__()
        self.image_paths = mix_lists(real_paths, fake_paths)
        self.current_image_index = 0
        self.real_count = len(real_paths)
        self.fake_count = len(fake_paths)
        self.real_correct = 0
        self.fake_correct = 0
        self.is_real = True

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Display')
        self.setGeometry(100, 100, 400, 400)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.display_image()

        self.real_button = QPushButton('Real', self)
        self.real_button.clicked.connect(self.on_real)

        self.fake_button = QPushButton('Fake', self)
        self.fake_button.clicked.connect(self.on_fake)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.real_button)
        vbox.addWidget(self.fake_button)

        self.setLayout(vbox)

    def display_image(self):
        pixmap = QPixmap(self.image_paths[self.current_image_index][0])
        if self.image_paths[self.current_image_index][1] == "real":
            self.is_real = True
        else:
            self.is_real = False

        pixmap = pixmap.scaledToWidth(300)
        self.image_label.setPixmap(pixmap)

    def on_real(self):
        print("Real selected")
        if self.is_real:
            self.real_correct += 1
        self.current_image_index += 1
        if self.current_image_index < len(self.image_paths):
            self.display_image()
        else:
            self.print_results()
            QApplication.quit()

    def on_fake(self):
        print("Fake selected")
        if not self.is_real:
            self.fake_correct += 1
        self.current_image_index += 1
        if self.current_image_index < len(self.image_paths):
            self.display_image()
        else:
            self.print_results()
            QApplication.quit()

    def print_results(self):
        print("All images viewed.")
        print("Real: ", self.real_correct, "out of", self.real_count)
        print("Fake: ", self.fake_correct, "out of", self.fake_count)


def mix_lists(real_list, fake_list):
    mixed_list = list(zip(real_list, [
                      'real'] * len(real_list))) + list(zip(fake_list, ['fake'] * len(fake_list)))
    random.shuffle(mixed_list)
    return mixed_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    real_folder_path = "real_images"
    fake_folder_path = "fake_images"

    real_images_paths = glob.glob(real_folder_path + "/*")
    fake_images_paths = glob.glob(fake_folder_path + "/*")

    ex = ImageDisplayApp(real_images_paths, fake_images_paths)
    ex.show()
    sys.exit(app.exec())
