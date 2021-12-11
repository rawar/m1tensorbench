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

## Optionale Tools

Um mit Tensorflow auf dem M1 produktiv arbeiten zu können, lohnen sich auch noch folgende Tools:

1. Update der installierten pip Version mit ``$ pip install --upgrade pip``
1. Installation von Xcode mit ``$ xcode-select --install`
1. Installation von [asitop](https://github.com/tlkh/asitop) mit ``pip install asitop``
1. Tensorflow Datensätze mit ``$ pip install tensorflow-datasets``
1. Tensorflow Beispiele mit ``$ pip install -q git+https://github.com/tensorflow/examples.git``

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



## Ausführen der Beispiele

Die Beispiele im Verzeichnis ``...`` können einfach einzeln mit Hilfe von

``$ python3 lstm.py``oder  
``$ python3 mnist2.py``ausgeführt werden. Möchte man die Zeit der Ausführung messen, reicht es auf der Kommandozeile mit 

``$ time python3 lstm.py`` die Zeit zu messen. 

Möchte man sich bei der Ausführung ansehen, wie stark die GPU-Kerne und die CPU ausgelastet sind, lässt sich ``asitop``mit Hilfe von

``$ asitop`` innerhalb eines anderen Terminalfensters starten.

## Benchmark Ergebnisse

| Rechner |	RAM	| CPU/GPU | lstm.py | mnist.py | imgMetal |
| --------| ---------| ---|------|-------| -------| 
| Mac Mini (2018) | 8 GB | 3,2 GHz 6-Core Intel Core i7 |  96.76s user 5.51s system 113% cpu 1:30.46 total | 292.83s user 52.89s system 226% cpu 2:32.57 total | nein |   
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 54,17s user 3,32s system 115% cpu 49,707 total | 139,08s user 40,62s system 207% cpu 1:26,43 total | nein |
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 36,29s user 12,58s system 101% cpu 48,321 total | 0 | ja |






