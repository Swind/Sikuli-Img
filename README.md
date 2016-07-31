# Sikuli-Img

# 設定開發環境 (Linux 跟 OSX）

1. Python3
2. OpenCV 3.1.0

## 安裝 pyenv 與 Python 3.5

可參考 [Install OpenCV 3.0 with Python 3.4 on OSX & Ubuntu](https://github.com/rainyear/lolita/issues/18)

```bash
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

```bash
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.0
```

## 編譯 OpenCV3

```bash
wget https://github.com/opencv/opencv/archive/3.1.0.tar.gz
tar -zxvf 3.1.0.tar.gz
cd 3.1.0

# 設定使用 python3 與 python packages
pyenv local 3.5.0
pip install numpy

# 使用 cmake 編譯
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \    -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
        -D BUILD_EXAMPLES=ON .. \
        -DPYTHON_INCLUDE_DIR=$HOME/.pyenv/versions/3.5.0/include/python3.5m -DPYTHON_LIBRARY=$HOME/.pyenv/versions/3.5.0/lib/libpython3.5m.so -DENABLE_PRECOMPILED_HEADERS=OFF

make -j4
sudo make install
```

# 測試

```python
import cv2
cv2.__version__
#=> '3.1.0'
```

# 參考連結

[pyenv](https://github.com/yyuu/pyenv)
