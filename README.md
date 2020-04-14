# AircrackPy

Un simple módulo de automatización de crackeo de WPAKEY.

<p align="center">
    <img alt="Plataforma" src="https://img.shields.io/badge/Plataforma-win--32%20%7C%20win--64-gold"></a>
    <a href="https://github.com/4nth0nySLT/AircrackPy/releases/latest"><img alt="Release" src="https://img.shields.io/badge/AircrackPy-v1.1-blue"></a>
    <a href="https://github.com/4nth0nySLT/AircrackPy/blob/master/LICENSE.md"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-red"></a>
</p>


## ¡¡¡Se requiere de aircrack-ng.exe!!!
https://github.com/aircrack-ng/aircrack-ng

Descargalo oficialmente en: https://www.aircrack-ng.org/index.html, directamente en: https://download.aircrack-ng.org/aircrack-ng-1.6-win.zip

O solamente utilizar lo necesario que viene incluido en el repositorio, todos sus derechos reservados a sus creadores.

## Opcional crunch_win.exe
https://github.com/shadwork/Windows-Crunch/releases (Ya incluido en el repositorio.)

## Formulario
Con capacidad de enviar las contraseñas a través de un formulario, debes crear uno en https://docs.google.com/forms.
![HOLA](https://raw.githubusercontent.com/4nth0nySLT/AircrackPy/master/1.png)
![HOLA](https://raw.githubusercontent.com/4nth0nySLT/AircrackPy/master/2.png)
### Click en "Obtener enlace previamente rellenado"
![HOLA](https://raw.githubusercontent.com/4nth0nySLT/AircrackPy/master/3.png)


Luego de generar el enlace, aparecerá una opción en la que podremos copiarlo, resultara uno como este:
https://docs.google.com/forms/d/e/$$$$$$$$$$$$$$$$/viewform?usp=pp_url&entry.@@@@@@@@@@@@@=4nth0nySLT
lo cual son los parametros que hay que modificar en la linea 10 y 11 de "aircrack.py".

```python
token="$$$$$$$$$$$$$$$$"
entry="@@@@@@@@@@@@@"
```

## Importante
Si descargas la última versión compilada en https://github.com/4nth0nySLT/AircrackPy/releases
Solo tendras que modificar las dos primeras lineas del archivo de texto "variables.txt".
```txt
$$$$$$$$$$$$$$$$
@@@@@@@@@@@@@
```

![HOLA](https://raw.githubusercontent.com/4nth0nySLT/AircrackPy/master/4.png)
### Acá puedes activar las notificaciones vía gmail. :P




## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2F4nth0nySLT%2FAircrackPy.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2F4nth0nySLT%2FAircrackPy?ref=badge_large)
