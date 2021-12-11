# Apple M1 Tensorflow Bechmark Beispiele

Dieses Repository enthält einige Deep Learning Beispiele welche dazu dienen können, die Trainingsgeschwinidgkeit von Apples M1 SoC-Familie (M1, M1 Pro, M1 Max) innerhalb von Tensorflow zu messen. 

## Für wen ist dieses Repository gedacht?

Data Scientisten, welche einen Apple Rechner mit M1 besitzen, können mit Hilfe dieser Quellcodes einschätzen und ausprobieren, wie schnell sie Ihre Tensorflow-Modelle trainieren können. 

## Voraussetzungen

Um die nötige Software zu installieren, sind folgende Schritte nötig:

1. Installation von [Homebrew](https://brew.sh) ``$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`` 
1. Download Miniforge (Conda Installation) für macOS ARM64 Chips (M1, M1 Pro, M1 Max) ``$ brew install miniforge`
1. Tensorflow Conda Umgebung anlegen mit ``$ conda create -n tfm1 python=3.8``
1. Conda-Shell aktivieren mit ``$ conda init zsh`` 
1. Conda-Umgebung aktuvieren mit ``$ conda activate tfm1``
1. Tensorflow für M1 installieren mit ``$ conda install -c apple tensorflow-deps`` ``$ python3 -m pip install tensorflow-macos`` ``$ python3 -m pip install tensorflow-metal``
1. Clonen dieses Repositories mit ``$ git clone https://github.com/rawar/m1tensorbench.git``
1. Transformers Sprachmodelle mit ``$ pip install transformers` 

## Optionale Tools

Um mit Tensorflow auf dem M1 produktiv arbeiten zu können, lohnen sich auch noch folgende Tools:

1. Update der installierten pip Version mit ``$ pip install --upgrade pip``
1. Installation von Xcode mit ``$ xcode-select --install`
1. Installation von [asitop](https://github.com/tlkh/asitop) mit ``pip install asitop``
1. Tensorflow Datensätze mit ``$ pip install tensorflow-datasets``
1. Tensorflow Beispiele mit ``$ pip install -q git+https://github.com/tensorflow/examples.git``

Um die Benchmarks für die Sprachmodelle zu trainieren, wird das Transformers Paket benötigt. Für die Installation muss man wie folgt vorgehen:

1. Rust Installieren mit ``$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh``
1. Tokenizers installieren mit ``$ git clone https://github.com/huggingface/tokenizers`` und ins Verzeichnis mit den Python Bindings wechseln ``$ cd tokenizers/bindings/python``. Dort die Bindings compilieren mit ``$ pip install setuptools_rust`` und mit ``$ python setup.py install``installieren
1. Die Transformers können dann mit ``$ pip install git+https://github.com/huggingface/transformers``installiert werden.    

## Sind GPUs verfügbar?

Um zu prüfen, ob die richtige Tensorflow-Version installiert ist, kann innerhalber der Python-Kommandozeile folgender Aufruf ausgeführt werden:

<pre>
>>> import tensorflow as tf
>>> tf.__version__
>>> tf.config.list_physical_devices()
</pre>

Auf einem Mac Mini (2018) mit Intel CPU wird folgendes ausgegeben:
``

## Beispiel-Skripte

Das Repository enthält folgende Tensoflow-Trainingsskripte:

Ein einfaches LSTML-Modell wird mit Hilfe von ``$ python3 lstm.py`` trainiert.

<pre>
$ python3 train_benchmark.py --type cnn --model resnet50
$ python3 train_benchmark.py --type cnn --model mobilenetv2
$ python3 train_benchmark.py --type transformer --model distilbert-base-uncased
$ python3 train_benchmark.py --type transformer --model bert-large-uncased --bs 16
</pre>


## Ausführen der Beispiele

Die Beispiele im Verzeichnis ``m1tensorbench`` können einfach einzeln mit Hilfe von

``$ python3 lstm.py``oder  
``$ python3 mnist2.py``ausgeführt werden. Möchte man die Zeit der Ausführung messen, reicht es auf der Kommandozeile mit 

``$ time python3 lstm.py`` die Zeit zu messen. 

Möchte man sich bei der Ausführung ansehen, wie stark die GPU-Kerne und die CPU ausgelastet sind, lässt sich ``asitop``mit Hilfe von

``$ asitop`` innerhalb eines anderen Terminalfensters starten.

## Benchmark Ergebnisse

| Rechner |	RAM	| CPU/GPU | lstm.py | mnist.py | resnet50 | mobilenetv2 | distilbert | Metal | 
| --------| ---------| ---|------|-------| -------| ----- | ---- | ---- |
| Mac Mini (2018) | 8 GB | 3,2 GHz 6-Core Intel Core i7 |  96.76s user 5.51s system 113% cpu 1:30.46 total | 292.83s user 52.89s system 226% cpu 2:32.57 total | 21689.79s user 9961.12s system 759% cpu 1:09:25.48 total | 7548.09s user 5944.51s system 673% cpu 33:23.73 total | 17771.00s user 9204.41s system 743% cpu 1:00:25.83 total | nein |   
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 54,17s user 3,32s system 115% cpu 49,707 total | 139,08s user 40,62s system 207% cpu 1:26,43 total | 8624,12s user 658,72s system 813% cpu 19:01,11 total | 1975,25s user 348,53s system 751% cpu 5:09,25 total | 9719,25s user 602,15s system 842% cpu 20:24,96 total | nein |
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 36,29s user 12,58s system 101% cpu 48,321 total | 333,92s user 276,42s system 102% cpu 9:56,62 total | 10,52s user 12,66s system 20% cpu 1:53,65 total| 8,50s user 5,25s system 25% cpu 53,277 total | 17,95s user 11,78s system 21% cpu 2:20,08 total | ja |
| MacBook Pro (13" 2020) | 16 GB | Apple M1 | 0 | 0 | 0 | 0 | 0 | nein |
| MacBook Pro (13" 2020) | 16 GB | Apple M1 |  | 0 | 0 | 0 | 0 | ja |
 

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






