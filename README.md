# Sikuli-Img

# 設定開發環境 (Windows)

參考 [Install OpenCV 3 with Python 3 on Windows](https://solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/)

P.S 未驗證，但是看起來可行

# 設定開發環境 (Linux 跟 OSX）

1. Python3
2. OpenCV 3.1.0

可參考 [Install OpenCV 3.0 with Python 3.4 on OSX & Ubuntu](https://github.com/rainyear/lolita/issues/18)

## 安裝 pyenv (為了要讓 Python 不要受系統預設的 Python 環境影響與限制) 與 Python 3.5.2

[pyenv](https://github.com/yyuu/pyenv)

```bash
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

安裝 Python 3.5.2

pyenv 會下載 Python 原始碼來編譯，所以要設定參數讓他在編譯的時候順便編譯 shared library

```bash
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.2
```

## 編譯 OpenCV3

```bash

# 下載 OpenCV3
wget https://github.com/opencv/opencv/archive/3.1.0.tar.gz
tar -zxvf 3.1.0.tar.gz
rm 3.1.0.tar.gz

# 下載 OpenCV3-contrib
wget https://github.com/opencv/opencv_contrib/archive/3.1.0.tar.gz
tar -zxvf 3.1.0.tar.gz
rm 3.1.0.tar.gz

# 設定使用 python3 與 python packages
pyenv local 3.5.2
pip install numpy
```

## 使用 cmake 產生 Makefile

進入 `opencv-3.1.0` 

```bash
cd opencv-3.1.0
```

下面可以建立一個 script 檔案，會比較方便執行。
當然也可以直接複製貼上，但是要注意一下下面 `PYTHON_INCLUDE_DIR` 等的路徑是否填寫正確。

```bash
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON .. \
      -DPYTHON_INCLUDE_DIR=$HOME/.pyenv/versions/3.5.2/include/python3.5m \
      -DPYTHON_LIBRARY=$HOME/.pyenv/versions/3.5.2/lib/libpython3.5m.so \
      -DENABLE_PRECOMPILED_HEADERS=OFF
```

cmake 產生的訊息中，注意 Python3 這邊是否有正確的找到 Python shared library 的路徑

```
--   Python 3:
--     Interpreter:                 /home/swind/.pyenv/shims/python3 (ver 3.5.2)
--     Libraries:                   /home/swind/.pyenv/versions/3.5.2/lib/libpython3.5m.so (ver 3.5.2)
--     numpy:                       /home/swind/.pyenv/versions/3.5.2/lib/python3.5/site-packages/numpy/core/include (ver 1.11.1)
--     packages path:               lib/python3.5/site-packages
```

## 編譯 OpenCV

```bash
cd build
make -j4
make install
```

# 測試

```python
import cv2
cv2.__version__
#=> '3.1.0'
```

# 參考連結

[pyenv](https://github.com/yyuu/pyenv)
