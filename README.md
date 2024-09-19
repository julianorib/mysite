# mysite test

Este projeto tem como objetivo criar um site simples em python e que tenha métricas para ser visualizadas posteriormente em um prometheus.

Além disto, ele também utiliza como base uma imagem mais segura.\
Imagens da Chainguard, que contém somente os pacotes necessários para execução do Python e com zero ou pouquíssimas vulnerabilidades.

Também tem os manifestos para deploy em Kubernetes.


```
python3 -m venv src/.venv

source src/.venv/bin/activate

pip install flask

```