Plugin Odoo Citas 0.91
================================

Componente de tipo plugin desarrollado en Python y XML para el ERP Odoo usado para introducir citas y fechas.
Permite gestionar citas a través de la interfaz de nuestro ERP, facilitando su creación, listado, consulta, 
modificación y eliminación de una manera fácil e intuitiva.

Al tratarse de un plugin instalable, debemos seguir una serie de pasos antes de poder usarlo, en primer lugar 
tenemos que localizar la carpeta 'addons' de nuestro servidor ERP (Odoo) y posicionar allí el directorio 'citas'
facilitado (junto a todo su contenido), en segundo lugar reiniciaremos nuestro servidor si lo tenemos en ejecución
para que detecte el nuevo componente (si no está arrancado no será necesario), y en tercer lugar deberemos buscar
e instalar el componente desde el menú 'Configuración' -> 'Módulos' -> 'Módulos locales', para localizar el plugin
bastará con teclear su nombre 'Citas' y pulsar en 'Instalar'.

El módulo ha sido desarrollado y testeado en la versión 8.0 del ERP Odoo, por lo que no podemos garantizar su 
funcionamiento en versiones anteriores.

## Requisitos
- [Odoo] 8.0 o superior
- Navegador Web [Chrome], [Firefox], [Opera], [Microsoft Edge], etc..

## Licencia
Este plugin se ofrece bajo licencia [GPL versión 3].

[Odoo]: https://www.odoo.com/es_ES/
[Chrome]: https://www.google.es/chrome/browser/desktop/index.html
[Firefox]: https://www.mozilla.org/es-ES/firefox/new/
[Opera]: http://www.opera.com/es
[Microsoft Edge]: https://www.microsoft.com/es-es/windows/microsoft-edge
[GPL versión 3]: https://www.gnu.org/licenses/gpl-3.0.en.html
