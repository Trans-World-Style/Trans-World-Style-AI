FROM nvidia/vulkan:1.3-470
ENV DEBIAN_FRONTEND=noninteractive
ENV CMAKE_VERSION=3.27.0-rc4
# python3 이상
ENV PYTHON_VERSION=3.8


# install python
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC && \
    apt-get update && \
    apt-get install -y software-properties-common &&\
    apt-add-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y unzip curl libssl-dev ninja-build && \
    apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-distutils && \
    apt-get install -y python3-pip && \
    python${PYTHON_VERSION} -m pip install pip && \
    rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 1 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python${PYTHON_VERSION} 1

## install cmake
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}-linux-x86_64.sh && \
    chmod +x cmake-${CMAKE_VERSION}-linux-x86_64.sh && \
    ./cmake-${CMAKE_VERSION}-linux-x86_64.sh --skip-license --prefix=/usr/local && \
    rm cmake-${CMAKE_VERSION}-linux-x86_64.sh

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get install -y swig && \
    pip install --upgrade pip && \
    # requirements \
    pip install opencv-python && \
    pip install loguru && \
    pip install rich && \
    # vulkan module
    pip install anime4k_python && \
    pip install waifu2x_ncnn_vulkan_python && \
    pip install rife_ncnn_vulkan_python && \
    pip install realcugan_ncnn_vulkan_python && \
    pip install realsr_ncnn_vulkan_python && \
    pip install srmd_ncnn_vulkan_python && \
    pip install ffmpeg-python

#COPY [".", "/workspace"]
#WORKDIR /workspace

# docker run --gpus all -itd --name video -v $PWD:/workspace -p 8000:12231 video_image
# docker run --gpus all -itd --name video -v $PWD/video2x:/workspace -p 8000:12231 k4yt3x/video2x:latest /bin/bash
# docker run --gpus all -it --rm --name video -v $PWD:/workspace -p 8000:12231 video_image bash
#docker pull k4yt3x/video2x:latest