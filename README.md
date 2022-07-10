# Apple M1 Tensorflow Bechmark Beispiele

Dieses Repository enthält einige Deep Learning Beispiele um die Trainingsgeschwinidgkeit von Apples M1 SoC-Familie (M1, M1 Pro, M1 Max) mit Hilfe von Tensorflow zu messen. 

## Für wen ist dieses Repository gedacht?

Data Scientisten, welche einen Apple Rechner mit M1 besitzen, können mit Hilfe dieser Quellcodes einschätzen und ausprobieren, wie schnell sie Ihre Tensorflow-Modelle trainieren können. 

## Voraussetzungen

Um die nötige Software zu installieren, sind folgende Schritte nötig:

1. Installation von [Homebrew](https://brew.sh) ``$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`` 
1. Download Miniforge (Conda Installation) für macOS ARM64 Chips (M1, M1 Pro, M1 Max) ``$ brew install miniforge``
1. Tensorflow Conda Umgebung anlegen mit ``$ conda create -n tfm1 python=3.8``
1. Conda-Shell aktivieren mit ``$ conda init zsh`` 
1. Conda-Umgebung aktuvieren mit ``$ conda activate tfm1``
1. Tensorflow für M1 installieren mit ``$ conda install -c apple tensorflow-deps`` ``$ python3 -m pip install tensorflow-macos`` ``$ python3 -m pip install tensorflow-metal``
1. Clonen dieses Repositories mit ``$ git clone https://github.com/rawar/m1tensorbench.git``
1. Transformers Sprachmodelle mit ``$ pip install transformers`` 

## Optionale Tools

Um alle Beispiele ausführen zu können, lohnt die Installation folgender Tools:

1. Update der installierten pip Version mit ``$ pip install --upgrade pip``
1. Installation von Xcode mit ``$ xcode-select --install`
1. Installation von [asitop](https://github.com/tlkh/asitop) mit ``pip install asitop``
1. Tensorflow Datensätze mit ``$ pip install tensorflow-datasets``
1. Tensorflow Beispiele mit ``$ pip install -q git+https://github.com/tensorflow/examples.git``

Um die Benchmarks für die Sprachmodelle zu trainieren, wird das Transformers Paket benötigt. Für die Installation muss man wie folgt vorgehen:

1. Rust Installieren mit ``$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh``
1. Tokenizers installieren mit ``$ git clone https://github.com/huggingface/tokenizers`` und ins Verzeichnis mit den Python Bindings wechseln ``$ cd tokenizers/bindings/python``. Dort die Bindings compilieren mit ``$ pip install setuptools_rust`` und mit ``$ python setup.py install`` installieren
1. Die Transformers können dann mit ``$ pip install git+https://github.com/huggingface/transformers`` installiert werden.    

## Sind GPUs verfügbar?

Um zu prüfen, ob die richtige Tensorflow-Version installiert ist, kann innerhalber der Python-Kommandozeile folgender Aufruf ausgeführt werden:

<pre>
>>> import tensorflow as tf
>>> tf.__version__
>>> tf.config.list_physical_devices()
</pre>

Auf einem Mac Mini (2018) mit Intel CPU wird folgendes ausgegeben:

<pre>
>>> tf.__version__
'2.7.0'
>>> tf.config.list_physical_devices()
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
</pre>

Auf dem Macbook Pro (2021) mit M1 Pro:



## Beispiel-Skripte

Das Repository enthält folgende Tensoflow-Trainingsskripte:

Ein einfaches LSTML-Modell wird mit Hilfe von ``$ python3 lstm.py`` trainiert. Folgende Skripte wurden für die Benchmark-Ergebnisse ausgeführt:

<pre>
$ python3 lstm.py
$ python3 mnist.py
$ python3 train_benchmark.py --type cnn --model resnet50
$ python3 train_benchmark.py --type cnn --model mobilenetv2
$ python3 train_benchmark.py --type transformer --model distilbert-base-uncased
</pre>


## Ausführen der Beispiele

Die Beispiele im Verzeichnis ``m1tensorbench`` können einfach einzeln mit Hilfe von

``$ python3 lstm.py``oder  
``$ python3 mnist2.py``ausgeführt werden. Möchte man die Zeit der Ausführung messen, reicht es auf der Kommandozeile mit 

``$ time python3 lstm.py`` die Zeit zu messen. 

Möchte man sich bei der Ausführung ansehen, wie stark die GPU-Kerne und die CPU ausgelastet sind, lässt sich ``asitop``mit Hilfe von

``$ asitop`` innerhalb eines anderen Terminalfensters starten.

## Benchmark Ergebnisse

Alle Benchmarks sind auf macOS 12.01 (Monterey) entstanden. Die Grafikkarte des Mac Mini (Intel UHD Graphic) wurde von Tensorflow nicht als GPU erkannt und unterstützt. Ich weiss, dass die Messung mit Hilfe von ``time``etwas ungenauer sind als zum Beispiel mit ``perf stat``. Bei allen Messungen wurden keine weiteren anderen Programme gestartet (ausser die welche bei Systemstart liefen).

| Rechner |	RAM	| CPU/GPU | lstm.py | mnist.py | resnet50 | mobilenetv2 | distilbert | Metal | 
| --------| ---------| ---|------|-------| -------| ----- | ---- | ---- | 
| Mac Mini (2018) | 8 GB | 3,2 GHz 6-Core Intel Core i7 |  96.76s user 5.51s system 113% cpu 1:30.46 total | 292.83s user 52.89s system 226% cpu 2:32.57 total | 21689.79s user 9961.12s system 759% cpu 1:09:25.48 total | 7548.09s user 5944.51s system 673% cpu 33:23.73 total | 17771.00s user 9204.41s system 743% cpu 1:00:25.83 total | nein |   
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 54,17s user 3,32s system 115% cpu 49,707 total | 139,08s user 40,62s system 207% cpu 1:26,43 total | 8624,12s user 658,72s system 813% cpu 19:01,11 total | 1975,25s user 348,53s system 751% cpu 5:09,25 total | 9719,25s user 602,15s system 842% cpu 20:24,96 total | nein |
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 36,29s user 12,58s system 101% cpu 48,321 total | 333,92s user 276,42s system 102% cpu 9:56,62 total | 10,52s user 12,66s system 20% cpu 1:53,65 total| 8,50s user 5,25s system 25% cpu 53,277 total | 17,95s user 11,78s system 21% cpu 2:20,08 total | ja |
| Mac Studio | 128 GB | Apple M1 Ultra | 52,71s user 6,68s system 120% cpu 49,454 total | 60,18s user 61,10s system 207% cpu 1:46,63 total | 1906,29s user 1594,34s system 1335% cpu 4:22,02 total | 8812,16s user 2853,04s system 1450% cpu 13:24,18 total | 9795,55s user 2085,42s system 1279% cpu 15:28,57 total | nein |
| Mac Studio | 128 GB | Apple M1 Ultra | 35,35s user 15,44s system 132% cpu 38,451 total | - | 11,44s user 14,85s system 43% cpu 59,910 total | 10,49s user 12,21s system 70% cpu 32,047 total | 16,13s user 10,80s system 37% cpu 1:11,06 total | ja |
| MacBook Pro (16" 2021) | 32 GB | Apple M1 Pro | 51,39s user 3,49s system 116% cpu 47,173 total | 143,02s user 43,57s system 203% cpu 1:31,80 total | 10187,99s user 741,22s system 382% cpu 47:40,95 total | 2061,17s user 350,96s system 750% cpu 5:21,41 total | 9790,15s user 613,01s system 836% cpu 20:43,79 total | nein |
| MacBook Pro (16" 2021) | 32 GB | Apple M1 Pro | 35,53s user 12,13s system 72% cpu 1:05,49 total | 349,65s user 269,74s system 84% cpu 12:16,41 total | 13,25s user 64,56s system 34% cpu 3:42,72 total | 8,51s user 4,51s system 15% cpu 1:23,39 total | 20,71s user 53,77s system 30% cpu 4:06,54 total | ja |
| MacBook Pro (13" 2020) | 16 GB | Apple M1 | 51,67s user 5,26s system 89% cpu 1:03,29 total | 123,41s user 25,42s system 199% cpu 1:14,68 total | 11795,09s user 1567,84s system 657% cpu 33:51,89 total| 2923,15s user 882,54s system 588% cpu 10:46,19 total | 12697,26s user 1469,96s system 638% cpu 36:59,81 total | nein |
| MacBook Pro (13" 2020) | 16 GB | Apple M1 | 39,01s user 11,90s system 88% cpu 57,479 total | 360,75s user 230,07s system 116% cpu 8:26,47 total | 22,33s user 423,95s system 77% cpu 9:39,18 total | 15,69s user 106,75s system 54% cpu 3:45,36 total | 22,81s user 391,68s system 63% cpu 10:51,91 total | ja | 

## Weitere Informationen
Weitere Informationen zum Thema Tensorflow Benchmarking auf Apples M1 Silicon finden sich auf folgenden Seiten:

* [Benchmarking the Apple M1 Max](https://tlkh.dev/benchmarking-the-apple-m1-max)
* [M1 competes with 20 cores Xeon®on TensorFlow training](https://towardsdatascience.com/benchmark-m1-part-2-vs-20-cores-xeon-vs-amd-epyc-16-and-32-cores-8e394d56003d)
* [Installing Tensorflow on Apple M1 With the New Metal Plugin](
https://betterprogramming.pub/installing-tensorflow-on-apple-m1-with-new-metal-plugin-6d3cb9cb00ca)
* [Tensorflow Metal](https://developer.apple.com/metal/tensorflow-plugin/)
* [Accelerating TensorFlow Performance on Mac](https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html)
* [Getting Started with tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)
* [Install Hugging Face Transformers on Apple M1](https://towardsdatascience.com/hugging-face-transformers-on-apple-m1-26f0705874d7)






