# Reflex: Política de Privacidad

*Última actualización: 4 de noviembre de 2026. Se aplica a las apps Reflex (celular), Reflex TV, Reflex para Windows y Reflex para Mac.*

**Responsable:** REFLEXX, desarrollador de Reflex. **Contacto:** por el correo de soporte que aparece en la página de Reflex en Google Play.

## Resumen

- **Tu pantalla es solo tuya.** La imagen y el sonido que Reflex transmite van directo de tu celular a tu PC o TV, por tu propia red Wi-Fi. Nada de tu pantalla se graba ni se envía a internet, a nosotros ni a terceros.
- **Sin anuncios.** Reflex no muestra anuncios y no usa el identificador de publicidad del dispositivo.
- **Conteo anónimo de uso.** Una vez al día Reflex avisa a Google Analytics que se abrió, solo para saber cuántas personas usan la app. Envía un número aleatorio creado en el dispositivo, la versión y el idioma, nada que te identifique. Se puede desactivar.
- **Cuenta Reflex (opcional).** Si entras con Google, guardamos tu nombre, correo y si tienes Reflex Pro, para que Pro funcione en el celular y en la PC. Puedes usar Reflex sin entrar y eliminar la cuenta cuando quieras.
- **Compras por Google Play.** Reflex Pro es una suscripción (mensual o anual) vendida por Google Play, que se cancela en la propia Play Store. No recibimos ni guardamos tus datos de pago.

## Qué usa la app y por qué

- **Captura de pantalla:** para mostrar la pantalla del celular en la PC o la TV. Solo funciona después de que tocas iniciar y aceptas el aviso de Android, y se detiene cuando la apagas.
- **Audio (permiso "grabar audio"):** para transmitir el sonido de las apps (videos, juegos, música). Reflex no usa el micrófono.
- **Notificaciones:** para mostrar que la duplicación está activa y poder detenerla desde ahí.
- **Red local:** para enviar la imagen a la PC o TV y para que encuentren el celular en la red.
- **Accesibilidad (opcional, solo en la versión con control):** para ejecutar en el celular los clics, deslizamientos y textos que haces en la PC conectada. Solo actúa mientras la duplicación está activa y nunca lee ni envía el contenido de la pantalla fuera de tu red.
- **Internet:** para comprobar la suscripción a Reflex Pro en Google Play, buscar actualizaciones, entrar en la Cuenta Reflex (si quieres) y enviar el conteo anónimo de uso (abajo).

## Cuenta Reflex

La Cuenta Reflex es opcional. Sirve para que Reflex Pro suscrito en el celular también funcione en Reflex para PC y vuelva solo cuando cambias de equipo.

- **Cómo se entra:** con tu cuenta de Google (en el celular, con la ventana del propio Google; en la PC, por el navegador). No creamos contraseña y nunca recibimos tu contraseña de Google.
- **Qué guardamos:** el identificador de tu cuenta de Google, tu nombre, tu correo, si quieres recibir novedades por correo, el código de la suscripción de Google Play vinculado a la cuenta, su fecha de vencimiento y las fechas de creación y último uso.
- **Para qué:** activar Reflex Pro en los equipos donde entraste. El correo solo se usa para enviar novedades si activas esa opción, y puedes desactivarla en cualquier momento. No vendemos ni compartimos estos datos.
- **Dónde:** en un servidor de Reflex en Cloudflare (Cloudflare Workers y base de datos D1), siempre con conexión cifrada (HTTPS). Para comprobar la suscripción, el servidor consulta Google Play.
- **Por cuánto tiempo:** mientras exista la cuenta. Al eliminarla, todo se borra en el momento.
- **Cómo eliminarla:** en la app, pestaña Reflex Pro > Cuenta Reflex > **Eliminar cuenta**, o en la web en [reflex-conta.reflexapp.workers.dev/apagar](https://reflex-conta.reflexapp.workers.dev/apagar). La suscripción de Google Play sigue hasta que la canceles en Play Store.

## Conteo anónimo de uso

Una vez al día, cuando abres Reflex (celular, TV o PC), la app envía a Google Analytics un único aviso con:

- un número aleatorio creado por la propia app la primera vez (no es el identificador de publicidad ni el número del dispositivo, y no está vinculado a ninguna cuenta);
- el tipo de app (celular, TV o PC), la versión de Reflex y el idioma elegido.

No se envía nombre, correo, cuenta de Google, lista de apps ni nada de lo que aparece en la pantalla. Google recibe la dirección de internet (IP) de la conexión para estimar el país y no la guarda en los informes. Solo usamos totales (cuántas personas lo usaron por día y por plataforma). Para desactivarlo: en el celular, en Ajustes > Privacidad > **Estadísticas anónimas de uso**; en la PC, en Ajustes > **Estadísticas anónimas de uso**. Borrar los datos de la app también borra el número aleatorio.

## Datos tratados por terceros

| Servicio | Datos | Para qué |
|---|---|---|
| Google Play (compras) | Cuenta de Google y registro de la compra | Procesar el pago de Reflex Pro y activar la suscripción |
| Cloudflare (servidor de la Cuenta Reflex) | Nombre, correo, identificador de la cuenta de Google y estado de Reflex Pro | Guardar la Cuenta Reflex, solo si entras |
| Google (inicio de sesión) | Cuenta de Google | Confirmar quién entra en la Cuenta Reflex |
| Google Analytics | Número aleatorio de la app, plataforma, versión, idioma y país aproximado | Contar cuántas personas usan Reflex (se puede desactivar) |

Google trata estos datos según la [Política de Privacidad de Google](https://policies.google.com/privacy). Cloudflare trata los datos de la Cuenta Reflex según la [Política de Privacidad de Cloudflare](https://www.cloudflare.com/privacypolicy/). Del conteo de uso solo vemos los totales en el panel de Google Analytics.

## Tus derechos

Según las leyes de protección de datos, como la LGPD de Brasil, puedes pedir información sobre tus datos por el contacto de arriba. Puedes ver, corregir o eliminar los datos de tu Cuenta Reflex en cualquier momento (eliminarla en la app o en la página de arriba). Las solicitudes sobre pagos las atiende Google.

## Niños

Reflex no está dirigido a niños menores de 13 años.

## Cambios

Si esta política cambia, la nueva versión se publicará en esta dirección con la fecha actualizada.
