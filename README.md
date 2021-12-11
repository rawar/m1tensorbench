# Apple M1 Tensorflow Bechmark Beispiele

Dieses Repository enthält einige Deep Learning Beispiele welche dazu dienen können, die Trainingsgeschwinidgkeit von Apples M1 SoC-Familie (M1, M1 Pro, M1 Max) innerhalb von Tensorflow zu messen. 

## Für wen ist dieses Repository gedacht?

Data Scientisten, welche einen Apple Rechner mit M1 besitzen, können mit Hilfe dieser Quellcodes einschätzen und ausprobieren, wie schnell sie Ihre Tensorflow-Modelle trainieren können. 

## Voraussetzungen

Um die nötige Software zu installieren, sind folgende Schritte nötig:

1. Installation von [Homebrew](https://brew.sh) ``$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`` 
1. Download Miniforge (Conda Installation) für macOS ARM64 Chips (M1, M1 Pro, M1 Max) ``$ brew install miniforge`
1. Tensorflow Conda Umgebung anlegen mit ``$ conda create -n tfm1 python=3.8``und ``$ conda activate tfm1``
1. Tensorflow für M1 installieren mit ``$ conda install -c apple tensorflow-deps`` ``$ python3 -m pip install tensorflow-macos`` ``$ python3 -m pip install tensorflow-metal``
1. Clonen dieses Repositories mit ``$ git clone https://github.com/rawar/m1tensorbench.git``

## Optionale Tools

Um mit Tensorflow auf dem M1 produktiv arbeiten zu können, lohnen sich auch noch folgende Tools:

1. Installation von Xcode mit ``$ xcode-select --install`
1. Installation von [asitop](https://github.com/tlkh/asitop) mit ``pip install asitop``
1. Tensorflow Datensätze mit ``$ pip install tensorflow-datasets``

## Sind GPUs verfügbar?

Um zu prüfen, ob die richtige Tensorflow-Version installiert ist, kann innerhalber der Python-Kommandozeile folgender Aufruf ausgeführt werden:

<pre>
>>> import tensorflow as tf
>>> tf.__version__
>>> tf.config.list_physical_devices()
</pre>

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

| Rechner |	Speicher	| M1 | lstm | mnist |
| --------| ---------| ---|------|-------|
| MacBook Pro (16" 2021) | 64 GB | Apple M1 Max | 0 | 0 |






