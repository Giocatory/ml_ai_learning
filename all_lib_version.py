import numpy
import scipy
import sklearn
import matplotlib
import PIL
import cv2

# Открываем файл для записи
with open('requirements.txt', 'w') as f:
    # Записываем версии библиотек в файл
    f.write(f'numpy=={numpy.__version__}\n')
    f.write(f'scipy=={scipy.__version__}\n')
    f.write(f'scikit-learn=={sklearn.__version__}\n')
    f.write(f'matplotlib=={matplotlib.__version__}\n')
    f.write(f'Pillow=={PIL.__version__}\n')
    f.write(f'opencv-python=={cv2.__version__}\n')