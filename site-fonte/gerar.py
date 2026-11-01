#!/usr/bin/env python3
"""Gera o site de download do Reflex na pasta docs/ (PT, EN e ES).

Uso:  python3 site-fonte/gerar.py
      ENDERECO=https://www.seudominio.com.br/ python3 site-fonte/gerar.py

ENDERECO é o endereço final do site (com / no fim). Só é usado nas tags de
compartilhamento, no sitemap e no link canônico; o resto do site usa links
relativos e funciona em qualquer hospedagem ou subpasta.
"""
import html, json, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "docs")
ENDERECO = os.environ.get("ENDERECO", "https://cebratelli-bot.github.io/reflex-download/")
if not ENDERECO.endswith("/"):
    ENDERECO += "/"

REPO = "https://github.com/cebratelli-bot/reflex-download"
BAIXAR = REPO + "/releases/latest/download/"
LINK = {
    "win": BAIXAR + "Reflex-Setup.exe",
    "apk": BAIXAR + "Reflex-Android.apk",
    "tv": BAIXAR + "Reflex-TV.apk",
    "play": "https://play.google.com/store/apps/details?id=com.reflexapp.espelhar",
    "insta": "https://www.instagram.com/app.reflex/",
    "versoes": REPO + "/releases",
    "novidades": REPO + "/blob/main/NOVIDADES.md",
    "json": "https://raw.githubusercontent.com/cebratelli-bot/reflex-download/main/arquivos/atualizacao.json",
}

with open(os.path.join(RAIZ, "arquivos", "atualizacao.json"), encoding="utf-8") as f:
    VER = json.load(f)

IDIOMAS = ["pt", "en", "es"]
PASTA = {"pt": "", "en": "en/", "es": "es/"}
LANG_HTML = {"pt": "pt-BR", "en": "en", "es": "es"}
NOME_IDIOMA = {"pt": "Português", "en": "English", "es": "Español"}

# ---------------------------------------------------------------- textos
T = {
"pt": dict(
    titulo="Reflex: espelhe a tela do celular no PC e na TV",
    descricao="Espelhe a tela do celular Android no PC com Windows e na TV pelo Wi-Fi, com imagem e som, sem cabo. Grátis.",
    nav_baixar="Baixar", nav_recursos="Recursos", nav_usar="Como usar", nav_pro="Pro", nav_duvidas="Dúvidas",
    hero_selo="Grátis · sem anúncios · sem cabo",
    hero_titulo="Espelhe o celular no PC e na TV",
    hero_texto="Imagem e som do seu Android no computador e na televisão, pelo Wi-Fi. Abra o Reflex nos dois aparelhos, toque no radar e pronto.",
    btn_win="Baixar para Windows", btn_win_sub="Windows 10 e 11",
    btn_play="Baixar na Google Play", btn_play_sub="Celular Android",
    hero_nota="Celular com Android 10 ou mais novo · PC com Windows 10 ou 11 (64 bits) · Fire TV e Android TV",
    alt_celular="Tela inicial do Reflex no celular, com o radar mostrando PCs e TVs da rede",
    baixar_titulo="Baixe o Reflex",
    baixar_texto="Instale no celular e no aparelho onde você quer ver a tela. Os links sempre baixam a versão mais nova, e depois o Reflex se atualiza sozinho.",
    c_cel="Celular Android", c_cel_txt="O app que envia a tela. Também recebe a tela do PC.",
    c_cel_play="Google Play", c_cel_apk="Baixar o APK", c_cel_apk_txt="O APK do site inclui o controle do celular pelo mouse e teclado do PC.",
    c_win="PC com Windows", c_win_txt="Recebe a tela do celular, grava, controla jogos e transmite o PC para o celular.",
    c_win_btn="Baixar Reflex-Setup.exe", c_win_nota="Instala sem senha de administrador.",
    c_tv="Fire TV e Android TV", c_tv_txt="Veja o celular na televisão. Funciona no Fire TV Stick e nas TVs com Android.",
    c_tv_btn="Baixar Reflex-TV.apk", c_tv_nota="Na TV, digite <b>is.gd/reflextv</b> no app Downloader.",
    versao="Versão",
    rec_titulo="Tudo o que o Reflex faz",
    rec_texto="Feito para ser simples: sem conta, sem cabo e sem configurar nada.",
    recursos=[
        ("radar", "Radar que acha tudo", "O celular encontra sozinho os PCs e TVs da sua rede. Também dá para conectar pelo QR code ou por um código."),
        ("som", "Imagem e som", "Vídeos, jogos e música tocam no PC ou na TV com o som do celular, a até 60 fps."),
        ("mouse", "Controle pelo PC", "Use o mouse e o teclado do computador para mexer no celular. Disponível no APK do site."),
        ("receber", "O PC no celular", "No PC, clique em Transmitir este PC e veja o computador na tela do celular."),
        ("gravar", "Grave a tela", "Grave em vídeo MP4 o que aparece do celular, direto no PC. Atalho Ctrl+R."),
        ("jogo", "Modo Gamer", "Sem notificações, chamadas silenciadas, o menor atraso e teclas do PC mapeadas na tela do jogo."),
        ("telas", "Várias telas", "Mostre o celular em mais de um PC ou TV ao mesmo tempo."),
        ("cadeado", "Privado de verdade", "A imagem vai direto do celular para o PC dentro do seu Wi-Fi. Nada passa por servidores e nada é gravado fora dos seus aparelhos."),
    ],
    galeria_titulo="Veja como é",
    galeria_alt=["Espelhe o celular no PC e na TV", "Toque no radar e pronto", "Veja a tela do PC no celular", "Modo Gamer", "Imagem nítida a 60 fps", "Reflex Pro"],
    usar_titulo="Comece em 3 passos",
    passos=[
        ("Instale nos dois aparelhos", "Baixe o Reflex no celular e no PC ou na TV. Na primeira vez no PC, permita o Reflex em <b>Redes privadas</b> quando o Windows perguntar."),
        ("Use o mesmo Wi-Fi", "Deixe o celular e o PC (ou a TV) na mesma rede Wi-Fi e abra o Reflex nos dois."),
        ("Toque no radar", "No celular, toque no PC ou na TV que aparece no radar e aceite o aviso do Android. A tela aparece na hora."),
    ],
    inst_titulo="Como instalar",
    inst=[
        ("Celular", [
            "Baixe pela <b>Google Play</b>, ou toque em <b>Baixar o APK</b> para a versão do site.",
            "Se baixou o APK, abra o arquivo. Se o Android pedir, permita instalar apps desta fonte.",
            "Abra o Reflex e escolha o idioma.",
        ]),
        ("PC com Windows", [
            "Baixe e abra o <b>Reflex-Setup.exe</b>. Não precisa de senha de administrador.",
            "Se aparecer <i>O Windows protegeu o computador</i>, clique em <b>Mais informações</b> e depois em <b>Executar assim mesmo</b>.",
            "Na primeira vez, permita o Reflex em <b>Redes privadas</b> quando o Windows perguntar.",
        ]),
        ("Fire TV Stick", [
            "Instale o app gratuito <b>Downloader</b> pela loja da Amazon.",
            "Em <i>Configurações &gt; Minha Fire TV &gt; Opções do desenvolvedor</i>, permita instalar apps do Downloader. Se a opção não aparecer, entre em <i>Minha Fire TV &gt; Sobre</i> e clique 7 vezes no nome do aparelho.",
            "No Downloader, digite <b>is.gd/reflextv</b> e instale.",
        ]),
    ],
    pro_titulo="Grátis para sempre. Pro se quiser mais.",
    pro_texto="O plano grátis já faz tudo, sem anúncios. O Reflex Pro deixa a imagem mais nítida.",
    gratis="Grátis", gratis_preco="R$ 0", gratis_sub="para sempre",
    pro="Reflex Pro", pro_preco="R$ 9,90", pro_sub="por mês, ou R$ 80 por ano",
    pro_teste="7 dias grátis para testar",
    lista_gratis=["HD 720p", "Imagem e som", "Controle pelo PC, TV e Modo Gamer", "Gravar a tela no PC", "Sem anúncios"],
    lista_pro=["Tudo do plano grátis", "Full HD 1080p", "Qualidade Máxima, quase sem compressão", "60 fps", "Cancele quando quiser na Play Store"],
    pro_btn="Assinar no celular", pro_nota="A assinatura é feita no app do celular, na aba Pro, pelo Google Play. Preços no Brasil.",
    duv_titulo="Dúvidas frequentes",
    duvidas=[
        ("O Reflex é grátis?", "Sim. O plano grátis espelha em HD 720p, com som, sem anúncios e sem limite de tempo. O Reflex Pro é opcional e libera Full HD e a qualidade Máxima, com 7 dias grátis para testar."),
        ("Preciso de cabo ou de internet?", "Não precisa de cabo. O celular e o PC (ou a TV) só precisam estar no mesmo Wi-Fi. A imagem vai direto de um aparelho para o outro, sem passar pela internet."),
        ("O Windows mostrou \"O Windows protegeu o computador\". É seguro?", "Sim. Esse aviso aparece para programas novos que ainda não têm muitos downloads. Clique em <b>Mais informações</b> e depois em <b>Executar assim mesmo</b>."),
        ("O PC não aparece no radar. O que eu faço?", "Confira se os dois estão no mesmo Wi-Fi (redes de convidados costumam bloquear). No PC, permita o Reflex em Redes privadas no Firewall do Windows. Se ainda assim não aparecer, use <b>Ler QR code</b> ou <b>Digitar código</b> no celular."),
        ("Qual a diferença entre a Google Play e o APK do site?", "A versão da Google Play se atualiza pela loja. O APK do site inclui o controle do celular pelo mouse e teclado do PC e se atualiza sozinho. Não dá para ter os dois ao mesmo tempo: desinstale um antes de instalar o outro. Para assinar o Pro, use a versão da Google Play."),
        ("Quais aparelhos funcionam?", "Celulares com Android 10 ou mais novo, PCs com Windows 10 ou 11 de 64 bits, Fire TV Stick e TVs com Android TV."),
        ("A minha tela fica gravada em algum lugar?", "Não. Nada da sua tela é enviado para a internet, para nós ou para terceiros. Veja a <a href=\"privacidade.html\">Política de Privacidade</a>."),
    ],
    final_titulo="Pronto para ver o celular na tela grande?",
    rodape_txt="Reflex: espelhamento de tela do celular para o PC e a TV.",
    rodape_priv="Política de Privacidade", rodape_versoes="Todas as versões", rodape_novidades="Novidades",
    rodape_insta="Instagram @app.reflex", idioma="Idioma",
    priv_titulo="Política de Privacidade do Reflex", voltar="Voltar para o início",
    nf_titulo="Página não encontrada", nf_texto="O endereço que você abriu não existe. Os downloads estão na página inicial.",
),
"en": dict(
    titulo="Reflex: mirror your phone screen to PC and TV",
    descricao="Mirror your Android phone screen to your Windows PC and TV over Wi-Fi, with picture and sound, no cable. Free.",
    nav_baixar="Download", nav_recursos="Features", nav_usar="How to use", nav_pro="Pro", nav_duvidas="FAQ",
    hero_selo="Free · no ads · no cable",
    hero_titulo="Mirror your phone to PC and TV",
    hero_texto="Picture and sound from your Android on your computer and TV, over Wi-Fi. Open Reflex on both devices, tap the radar and you're done.",
    btn_win="Download for Windows", btn_win_sub="Windows 10 and 11",
    btn_play="Get it on Google Play", btn_play_sub="Android phone",
    hero_nota="Phone with Android 10 or newer · PC with Windows 10 or 11 (64-bit) · Fire TV and Android TV",
    alt_celular="Reflex home screen on the phone, with the radar showing PCs and TVs on the network",
    baixar_titulo="Download Reflex",
    baixar_texto="Install it on your phone and on the device where you want to see the screen. The links always download the newest version, and then Reflex updates itself.",
    c_cel="Android phone", c_cel_txt="The app that sends the screen. It also receives the PC screen.",
    c_cel_play="Google Play", c_cel_apk="Download the APK", c_cel_apk_txt="The website APK includes controlling the phone with the PC mouse and keyboard.",
    c_win="Windows PC", c_win_txt="Shows the phone screen, records it, controls games and casts the PC to the phone.",
    c_win_btn="Download Reflex-Setup.exe", c_win_nota="Installs without an administrator password.",
    c_tv="Fire TV and Android TV", c_tv_txt="See your phone on the TV. Works on Fire TV Stick and Android TVs.",
    c_tv_btn="Download Reflex-TV.apk", c_tv_nota="On the TV, type <b>is.gd/reflextv</b> in the Downloader app.",
    versao="Version",
    rec_titulo="Everything Reflex does",
    rec_texto="Made to be simple: no account, no cable and nothing to set up.",
    recursos=[
        ("radar", "A radar that finds everything", "Your phone finds the PCs and TVs on your network by itself. You can also connect with a QR code or a code."),
        ("som", "Picture and sound", "Videos, games and music play on the PC or TV with your phone's sound, at up to 60 fps."),
        ("mouse", "Control from the PC", "Use your computer's mouse and keyboard to use the phone. Available in the website APK."),
        ("receber", "Your PC on the phone", "On the PC, click Cast this PC and see your computer on the phone screen."),
        ("gravar", "Record the screen", "Record what the phone shows as an MP4 video, right on the PC. Shortcut Ctrl+R."),
        ("jogo", "Gamer mode", "No notifications, silenced calls, the lowest delay and PC keys mapped onto the game screen."),
        ("telas", "Many screens", "Show your phone on more than one PC or TV at the same time."),
        ("cadeado", "Truly private", "The picture goes straight from your phone to your PC inside your Wi-Fi. Nothing goes through servers and nothing is recorded outside your devices."),
    ],
    galeria_titulo="See what it looks like",
    galeria_alt=["Mirror your phone to PC and TV", "Tap the radar and you're done", "See your PC screen on the phone", "Gamer mode", "Sharp picture at 60 fps", "Reflex Pro"],
    usar_titulo="Start in 3 steps",
    passos=[
        ("Install on both devices", "Download Reflex on your phone and on your PC or TV. The first time on the PC, allow Reflex on <b>Private networks</b> when Windows asks."),
        ("Use the same Wi-Fi", "Keep the phone and the PC (or TV) on the same Wi-Fi network and open Reflex on both."),
        ("Tap the radar", "On the phone, tap the PC or TV shown on the radar and accept the Android notice. The screen shows up right away."),
    ],
    inst_titulo="How to install",
    inst=[
        ("Phone", [
            "Get it on <b>Google Play</b>, or tap <b>Download the APK</b> for the website version.",
            "If you downloaded the APK, open the file. If Android asks, allow installing apps from this source.",
            "Open Reflex and choose your language.",
        ]),
        ("Windows PC", [
            "Download and open <b>Reflex-Setup.exe</b>. No administrator password needed.",
            "If you see <i>Windows protected your PC</i>, click <b>More info</b> and then <b>Run anyway</b>.",
            "The first time, allow Reflex on <b>Private networks</b> when Windows asks.",
        ]),
        ("Fire TV Stick", [
            "Install the free <b>Downloader</b> app from the Amazon store.",
            "In <i>Settings &gt; My Fire TV &gt; Developer options</i>, allow installing apps from Downloader. If the option is missing, go to <i>My Fire TV &gt; About</i> and click the device name 7 times.",
            "In Downloader, type <b>is.gd/reflextv</b> and install.",
        ]),
    ],
    pro_titulo="Free forever. Pro if you want more.",
    pro_texto="The free plan already does everything, with no ads. Reflex Pro makes the picture sharper.",
    gratis="Free", gratis_preco="Free", gratis_sub="forever",
    pro="Reflex Pro", pro_preco="Pro", pro_sub="monthly or yearly subscription",
    pro_teste="7-day free trial",
    lista_gratis=["HD 720p", "Picture and sound", "PC control, TV and Gamer mode", "Record the screen on the PC", "No ads"],
    lista_pro=["Everything in the free plan", "Full HD 1080p", "Maximum quality, almost no compression", "60 fps", "Cancel anytime in the Play Store"],
    pro_btn="Subscribe on the phone", pro_nota="You subscribe in the phone app, on the Pro tab, through Google Play. The price for your country is shown there.",
    duv_titulo="Frequently asked questions",
    duvidas=[
        ("Is Reflex free?", "Yes. The free plan mirrors in HD 720p, with sound, no ads and no time limit. Reflex Pro is optional and unlocks Full HD and Maximum quality, with a 7-day free trial."),
        ("Do I need a cable or internet?", "No cable needed. The phone and the PC (or TV) just need to be on the same Wi-Fi. The picture goes straight from one device to the other, without going through the internet."),
        ("Windows showed \"Windows protected your PC\". Is it safe?", "Yes. This notice shows up for new programs that don't have many downloads yet. Click <b>More info</b> and then <b>Run anyway</b>."),
        ("The PC doesn't show up on the radar. What do I do?", "Check that both are on the same Wi-Fi (guest networks often block this). On the PC, allow Reflex on Private networks in Windows Firewall. If it still doesn't show up, connect with the QR code or the code option on the phone."),
        ("What's the difference between Google Play and the website APK?", "The Google Play version updates through the store. The website APK includes controlling the phone with the PC mouse and keyboard and updates itself. You can't have both at once: uninstall one before installing the other. To subscribe to Pro, use the Google Play version."),
        ("Which devices work?", "Phones with Android 10 or newer, 64-bit Windows 10 or 11 PCs, Fire TV Stick and Android TVs."),
        ("Is my screen recorded anywhere?", "No. Nothing from your screen is sent to the internet, to us or to third parties. See the <a href=\"privacidade.html\">Privacy Policy</a>."),
    ],
    final_titulo="Ready to see your phone on the big screen?",
    rodape_txt="Reflex: phone screen mirroring to PC and TV.",
    rodape_priv="Privacy Policy", rodape_versoes="All versions", rodape_novidades="What's new",
    rodape_insta="Instagram @app.reflex", idioma="Language",
    priv_titulo="Reflex Privacy Policy", voltar="Back to the home page",
    nf_titulo="Page not found", nf_texto="The address you opened doesn't exist. The downloads are on the home page.",
),
"es": dict(
    titulo="Reflex: duplica la pantalla del celular en la PC y la TV",
    descricao="Duplica la pantalla de tu celular Android en tu PC con Windows y en la TV por Wi-Fi, con imagen y sonido, sin cable. Gratis.",
    nav_baixar="Descargar", nav_recursos="Funciones", nav_usar="Cómo usar", nav_pro="Pro", nav_duvidas="Preguntas",
    hero_selo="Gratis · sin anuncios · sin cable",
    hero_titulo="Duplica el celular en la PC y la TV",
    hero_texto="Imagen y sonido de tu Android en la computadora y en la televisión, por Wi-Fi. Abre Reflex en los dos dispositivos, toca el radar y listo.",
    btn_win="Descargar para Windows", btn_win_sub="Windows 10 y 11",
    btn_play="Disponible en Google Play", btn_play_sub="Celular Android",
    hero_nota="Celular con Android 10 o más nuevo · PC con Windows 10 u 11 (64 bits) · Fire TV y Android TV",
    alt_celular="Pantalla de inicio de Reflex en el celular, con el radar mostrando las PC y TV de la red",
    baixar_titulo="Descarga Reflex",
    baixar_texto="Instálalo en el celular y en el dispositivo donde quieres ver la pantalla. Los enlaces siempre descargan la versión más nueva, y después Reflex se actualiza solo.",
    c_cel="Celular Android", c_cel_txt="La app que envía la pantalla. También recibe la pantalla de la PC.",
    c_cel_play="Google Play", c_cel_apk="Descargar el APK", c_cel_apk_txt="El APK del sitio incluye el control del celular con el mouse y el teclado de la PC.",
    c_win="PC con Windows", c_win_txt="Muestra la pantalla del celular, la graba, controla juegos y transmite la PC al celular.",
    c_win_btn="Descargar Reflex-Setup.exe", c_win_nota="Se instala sin contraseña de administrador.",
    c_tv="Fire TV y Android TV", c_tv_txt="Mira el celular en la televisión. Funciona en Fire TV Stick y en TV con Android.",
    c_tv_btn="Descargar Reflex-TV.apk", c_tv_nota="En la TV, escribe <b>is.gd/reflextv</b> en la app Downloader.",
    versao="Versión",
    rec_titulo="Todo lo que hace Reflex",
    rec_texto="Hecho para ser simple: sin cuenta, sin cable y sin configurar nada.",
    recursos=[
        ("radar", "Un radar que lo encuentra todo", "El celular encuentra solo las PC y TV de tu red. También puedes conectar con un código QR o un código."),
        ("som", "Imagen y sonido", "Videos, juegos y música se reproducen en la PC o la TV con el sonido del celular, hasta 60 fps."),
        ("mouse", "Control desde la PC", "Usa el mouse y el teclado de la computadora para manejar el celular. Disponible en el APK del sitio."),
        ("receber", "La PC en el celular", "En la PC, haz clic en Transmitir esta PC y mira la computadora en la pantalla del celular."),
        ("gravar", "Graba la pantalla", "Graba en video MP4 lo que muestra el celular, directo en la PC. Atajo Ctrl+R."),
        ("jogo", "Modo Gamer", "Sin notificaciones, llamadas silenciadas, el menor retraso y teclas de la PC asignadas en la pantalla del juego."),
        ("telas", "Varias pantallas", "Muestra el celular en más de una PC o TV al mismo tiempo."),
        ("cadeado", "Privado de verdad", "La imagen va directo del celular a la PC dentro de tu Wi-Fi. Nada pasa por servidores y nada se graba fuera de tus dispositivos."),
    ],
    galeria_titulo="Mira cómo es",
    galeria_alt=["Duplica el celular en la PC y la TV", "Toca el radar y listo", "Mira la pantalla de la PC en el celular", "Modo Gamer", "Imagen nítida a 60 fps", "Reflex Pro"],
    usar_titulo="Empieza en 3 pasos",
    passos=[
        ("Instala en los dos dispositivos", "Descarga Reflex en el celular y en la PC o la TV. La primera vez en la PC, permite Reflex en <b>Redes privadas</b> cuando Windows lo pregunte."),
        ("Usa el mismo Wi-Fi", "Deja el celular y la PC (o la TV) en la misma red Wi-Fi y abre Reflex en los dos."),
        ("Toca el radar", "En el celular, toca la PC o la TV que aparece en el radar y acepta el aviso de Android. La pantalla aparece al instante."),
    ],
    inst_titulo="Cómo instalar",
    inst=[
        ("Celular", [
            "Descárgalo en <b>Google Play</b>, o toca <b>Descargar el APK</b> para la versión del sitio.",
            "Si descargaste el APK, abre el archivo. Si Android lo pide, permite instalar apps de esta fuente.",
            "Abre Reflex y elige el idioma.",
        ]),
        ("PC con Windows", [
            "Descarga y abre <b>Reflex-Setup.exe</b>. No necesita contraseña de administrador.",
            "Si aparece <i>Windows protegió tu PC</i>, haz clic en <b>Más información</b> y luego en <b>Ejecutar de todas formas</b>.",
            "La primera vez, permite Reflex en <b>Redes privadas</b> cuando Windows lo pregunte.",
        ]),
        ("Fire TV Stick", [
            "Instala la app gratuita <b>Downloader</b> desde la tienda de Amazon.",
            "En <i>Configuración &gt; Mi Fire TV &gt; Opciones para desarrolladores</i>, permite instalar apps de Downloader. Si la opción no aparece, entra en <i>Mi Fire TV &gt; Acerca de</i> y haz clic 7 veces en el nombre del dispositivo.",
            "En Downloader, escribe <b>is.gd/reflextv</b> e instala.",
        ]),
    ],
    pro_titulo="Gratis para siempre. Pro si quieres más.",
    pro_texto="El plan gratis ya lo hace todo, sin anuncios. Reflex Pro hace la imagen más nítida.",
    gratis="Gratis", gratis_preco="Gratis", gratis_sub="para siempre",
    pro="Reflex Pro", pro_preco="Pro", pro_sub="suscripción mensual o anual",
    pro_teste="7 días gratis para probar",
    lista_gratis=["HD 720p", "Imagen y sonido", "Control desde la PC, TV y Modo Gamer", "Grabar la pantalla en la PC", "Sin anuncios"],
    lista_pro=["Todo lo del plan gratis", "Full HD 1080p", "Calidad Máxima, casi sin compresión", "60 fps", "Cancela cuando quieras en la Play Store"],
    pro_btn="Suscribirse en el celular", pro_nota="La suscripción se hace en la app del celular, en la pestaña Pro, con Google Play. Ahí ves el precio de tu país.",
    duv_titulo="Preguntas frecuentes",
    duvidas=[
        ("¿Reflex es gratis?", "Sí. El plan gratis duplica en HD 720p, con sonido, sin anuncios y sin límite de tiempo. Reflex Pro es opcional y desbloquea Full HD y la calidad Máxima, con 7 días gratis para probar."),
        ("¿Necesito cable o internet?", "No necesitas cable. El celular y la PC (o la TV) solo deben estar en el mismo Wi-Fi. La imagen va directo de un dispositivo al otro, sin pasar por internet."),
        ("Windows mostró \"Windows protegió tu PC\". ¿Es seguro?", "Sí. Ese aviso aparece con programas nuevos que todavía no tienen muchas descargas. Haz clic en <b>Más información</b> y luego en <b>Ejecutar de todas formas</b>."),
        ("La PC no aparece en el radar. ¿Qué hago?", "Revisa que los dos estén en el mismo Wi-Fi (las redes de invitados suelen bloquearlo). En la PC, permite Reflex en Redes privadas en el Firewall de Windows. Si aún no aparece, usa <b>Escanear código QR</b> o <b>Escribir código</b> en el celular."),
        ("¿Qué diferencia hay entre Google Play y el APK del sitio?", "La versión de Google Play se actualiza por la tienda. El APK del sitio incluye el control del celular con el mouse y el teclado de la PC y se actualiza solo. No puedes tener las dos a la vez: desinstala una antes de instalar la otra. Para suscribirte a Pro, usa la versión de Google Play."),
        ("¿Qué dispositivos funcionan?", "Celulares con Android 10 o más nuevo, PC con Windows 10 u 11 de 64 bits, Fire TV Stick y TV con Android TV."),
        ("¿Mi pantalla se graba en algún lugar?", "No. Nada de tu pantalla se envía a internet, a nosotros ni a terceros. Mira la <a href=\"privacidade.html\">Política de Privacidad</a>."),
    ],
    final_titulo="¿Listo para ver el celular en la pantalla grande?",
    rodape_txt="Reflex: duplicación de pantalla del celular a la PC y la TV.",
    rodape_priv="Política de Privacidad", rodape_versoes="Todas las versiones", rodape_novidades="Novedades",
    rodape_insta="Instagram @app.reflex", idioma="Idioma",
    priv_titulo="Política de Privacidad de Reflex", voltar="Volver al inicio",
    nf_titulo="Página no encontrada", nf_texto="La dirección que abriste no existe. Las descargas están en la página de inicio.",
),
}

# ---------------------------------------------------------------- ícones (traço, 24x24)
ICONE = {
    "radar": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/><path d="M12 12 18.4 5.6"/>',
    "som": '<path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/>',
    "mouse": '<rect x="6" y="3" width="12" height="18" rx="6"/><path d="M12 7v4"/>',
    "receber": '<rect x="2" y="4" width="14" height="10" rx="1.5"/><path d="M6 18h6M9 14v4"/><rect x="17" y="9" width="5" height="11" rx="1"/>',
    "gravar": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4" fill="currentColor"/>',
    "jogo": '<path d="M6 8h12a4 4 0 0 1 4 4v1a4 4 0 0 1-7 2.6L14 15h-4l-1 .6A4 4 0 0 1 2 13v-1a4 4 0 0 1 4-4z"/><path d="M7 10.5v3M5.5 12h3"/><circle cx="16.5" cy="11" r=".8" fill="currentColor"/><circle cx="18" cy="13" r=".8" fill="currentColor"/>',
    "telas": '<rect x="2" y="3" width="12" height="9" rx="1.5"/><rect x="10" y="10" width="12" height="9" rx="1.5"/>',
    "cadeado": '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><path d="M12 14v3"/>',
    "windows": '<path d="M3 5.5 10.5 4.5v7H3zM11.5 4.4 21 3v8.5h-9.5zM3 12.5h7.5v7L3 18.5zM11.5 12.5H21V21l-9.5-1.4z" fill="currentColor" stroke="none"/>',
    "android": '<rect x="5" y="2" width="14" height="20" rx="3"/><path d="M10 18.5h4"/>',
    "tv": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8"/>',
    "play": '<path d="M5 3.5v17l14-8.5z" fill="currentColor" stroke="none"/>',
    "baixar": '<path d="M12 3v12M7 10l5 5 5-5M5 20h14"/>',
    "ok": '<path d="M5 12.5 10 17 19 7"/>',
    "insta": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
    "globo": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
}
def ic(n, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONE[n]}</svg>'

LOGO = '<img src="{r}img/icone-192.png" alt="" width="36" height="36" class="logo">'

# ---------------------------------------------------------------- moldura comum
def cabeca(l, t, titulo, descricao, r, caminho, extra=""):
    alternativos = "".join(
        f'<link rel="alternate" hreflang="{LANG_HTML[x]}" href="{ENDERECO}{PASTA[x]}{caminho}">' for x in IDIOMAS)
    alternativos += f'<link rel="alternate" hreflang="x-default" href="{ENDERECO}{caminho}">'
    return f"""<!doctype html>
<html lang="{LANG_HTML[l]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(descricao)}">
<meta name="theme-color" content="#0B1A22">
<link rel="canonical" href="{ENDERECO}{PASTA[l]}{caminho}">
{alternativos}
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{html.escape(descricao)}">
<meta property="og:url" content="{ENDERECO}{PASTA[l]}{caminho}">
<meta property="og:image" content="{ENDERECO}img/compartilhar-{l}.jpg">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{r}img/favicon-32.png">
<link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="stylesheet" href="{r}estilo.css">
{extra}</head>
<body>
"""

def topo(l, t, r, caminho, ancora_base=""):
    seletor = "".join(
        f'<a href="{r}{PASTA[x]}{caminho}" data-idioma="{x}"{" aria-current=\"true\"" if x == l else ""}>{x.upper()}</a>'
        for x in IDIOMAS)
    a = ancora_base
    return f"""<header class="topo">
  <div class="largura topo-in">
    <a class="marca" href="{a or './'}">{LOGO.format(r=r)}<span>Reflex</span></a>
    <nav class="menu" aria-label="Menu">
      <a href="{a}#recursos">{t['nav_recursos']}</a>
      <a href="{a}#como-usar">{t['nav_usar']}</a>
      <a href="{a}#pro">{t['nav_pro']}</a>
      <a href="{a}#duvidas">{t['nav_duvidas']}</a>
    </nav>
    <div class="idiomas" role="group" aria-label="{t['idioma']}">{ic('globo','ic pequeno')}{seletor}</div>
    <a class="botao botao-pequeno" href="{a}#baixar">{t['nav_baixar']}</a>
  </div>
</header>
"""

def rodape(l, t, r):
    return f"""<footer class="rodape">
  <div class="largura rodape-in">
    <div>
      <a class="marca" href="./">{LOGO.format(r=r)}<span>Reflex</span></a>
      <p>{t['rodape_txt']}</p>
    </div>
    <nav aria-label="Links">
      <a href="privacidade.html">{t['rodape_priv']}</a>
      <a href="{LINK['novidades']}">{t['rodape_novidades']}</a>
      <a href="{LINK['versoes']}">{t['rodape_versoes']}</a>
      <a href="{LINK['insta']}" rel="me">{ic('insta','ic pequeno')} {t['rodape_insta']}</a>
    </nav>
  </div>
  <p class="largura copyright">© 2026 Reflex</p>
</footer>
<script src="{r}site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- página inicial
def pagina_inicial(l):
    t = T[l]; r = "../" if PASTA[l] else ""
    recursos = "".join(
        f'<li class="recurso">{ic(i)}<h3>{h}</h3><p>{p}</p></li>' for i, h, p in t["recursos"])
    galeria = "".join(
        f'<li><img src="{r}img/{l}-tela-{n}.webp" alt="{html.escape(a)}" width="540" height="960" loading="lazy"></li>'
        for n, a in enumerate(t["galeria_alt"], 1))
    passos = "".join(f'<li><span class="num">{n}</span><h3>{h}</h3><p>{p}</p></li>' for n, (h, p) in enumerate(t["passos"], 1))
    inst = "".join(
        f'<div class="inst"><h3>{h}</h3><ol>{"".join(f"<li>{x}</li>" for x in itens)}</ol></div>' for h, itens in t["inst"])
    lg = "".join(f"<li>{ic('ok','ic pequeno')}{x}</li>" for x in t["lista_gratis"])
    lp = "".join(f"<li>{ic('ok','ic pequeno')}{x}</li>" for x in t["lista_pro"])
    duv = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["duvidas"])
    play = LINK["play"] + {"pt": "&hl=pt_BR", "en": "&hl=en", "es": "&hl=es"}[l]

    corpo = f"""<main>
<section class="hero">
  <div class="largura hero-in">
    <div class="hero-txt">
      <p class="selo">{t['hero_selo']}</p>
      <h1>{t['hero_titulo']}</h1>
      <p class="lead">{t['hero_texto']}</p>
      <div class="botoes" id="botoes-hero">
        <a class="botao botao-grande" data-so="windows" href="{LINK['win']}">{ic('windows')}<span>{t['btn_win']}<small>{t['btn_win_sub']}</small></span></a>
        <a class="botao botao-grande botao-2" data-so="android" href="{play}">{ic('play')}<span>{t['btn_play']}<small>{t['btn_play_sub']}</small></span></a>
      </div>
      <p class="nota">{t['hero_nota']}</p>
    </div>
    <div class="hero-img">
      <div class="aneis" aria-hidden="true"><i></i><i></i><i></i></div>
      <img src="{r}img/{l}-celular.webp" alt="{html.escape(t['alt_celular'])}" width="444" height="843" fetchpriority="high">
    </div>
  </div>
</section>

<section id="baixar" class="secao">
  <div class="largura">
    <h2>{t['baixar_titulo']}</h2>
    <p class="sub">{t['baixar_texto']}</p>
    <div class="cartoes">
      <article class="cartao" data-so="android">
        <div class="cartao-ic">{ic('android')}</div>
        <h3>{t['c_cel']}</h3>
        <p>{t['c_cel_txt']}</p>
        <p class="versao" data-versao="android">{t['versao']} {VER['android_versao']}</p>
        <a class="botao" href="{play}">{ic('play','ic pequeno')} {t['c_cel_play']}</a>
        <a class="botao botao-contorno" href="{LINK['apk']}">{ic('baixar','ic pequeno')} {t['c_cel_apk']}</a>
        <p class="mini">{t['c_cel_apk_txt']}</p>
      </article>
      <article class="cartao" data-so="windows">
        <div class="cartao-ic">{ic('windows')}</div>
        <h3>{t['c_win']}</h3>
        <p>{t['c_win_txt']}</p>
        <p class="versao" data-versao="windows">{t['versao']} {VER['windows_versao']}</p>
        <a class="botao" href="{LINK['win']}">{ic('baixar','ic pequeno')} {t['c_win_btn']}</a>
        <p class="mini">{t['c_win_nota']}</p>
      </article>
      <article class="cartao">
        <div class="cartao-ic">{ic('tv')}</div>
        <h3>{t['c_tv']}</h3>
        <p>{t['c_tv_txt']}</p>
        <p class="versao" data-versao="tv">{t['versao']} {VER['tv_versao']}</p>
        <a class="botao" href="{LINK['tv']}">{ic('baixar','ic pequeno')} {t['c_tv_btn']}</a>
        <p class="mini">{t['c_tv_nota']}</p>
      </article>
    </div>
  </div>
</section>

<section id="recursos" class="secao secao-alt">
  <div class="largura">
    <h2>{t['rec_titulo']}</h2>
    <p class="sub">{t['rec_texto']}</p>
    <ul class="recursos">{recursos}</ul>
  </div>
</section>

<section class="secao" aria-label="{t['galeria_titulo']}">
  <div class="largura">
    <h2>{t['galeria_titulo']}</h2>
  </div>
  <ul class="galeria" tabindex="0">{galeria}</ul>
</section>

<section id="como-usar" class="secao secao-alt">
  <div class="largura">
    <h2>{t['usar_titulo']}</h2>
    <ol class="passos">{passos}</ol>
    <h2 class="h2-meio">{t['inst_titulo']}</h2>
    <div class="insts">{inst}</div>
  </div>
</section>

<section id="pro" class="secao">
  <div class="largura">
    <h2>{t['pro_titulo']}</h2>
    <p class="sub">{t['pro_texto']}</p>
    <div class="planos">
      <article class="plano">
        <h3>{t['gratis']}</h3>
        <p class="preco">{t['gratis_preco']} <span>{t['gratis_sub']}</span></p>
        <ul>{lg}</ul>
      </article>
      <article class="plano plano-pro">
        <p class="fita">{t['pro_teste']}</p>
        <h3>{t['pro']}</h3>
        <p class="preco">{t['pro_preco']} <span>{t['pro_sub']}</span></p>
        <ul>{lp}</ul>
        <a class="botao" href="{play}">{ic('play','ic pequeno')} {t['pro_btn']}</a>
      </article>
    </div>
    <p class="mini centro">{t['pro_nota']}</p>
  </div>
</section>

<section id="duvidas" class="secao secao-alt">
  <div class="largura estreito">
    <h2>{t['duv_titulo']}</h2>
    <div class="duvidas">{duv}</div>
  </div>
</section>

<section class="secao final">
  <div class="largura">
    <h2>{t['final_titulo']}</h2>
    <div class="botoes centro">
      <a class="botao botao-grande" href="{LINK['win']}">{ic('windows')}<span>{t['btn_win']}<small>{t['btn_win_sub']}</small></span></a>
      <a class="botao botao-grande botao-2" href="{play}">{ic('play')}<span>{t['btn_play']}<small>{t['btn_play_sub']}</small></span></a>
    </div>
  </div>
</section>
</main>
"""
    dados = {
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Reflex",
        "operatingSystem": "Android, Windows 10, Windows 11, Fire OS, Android TV",
        "applicationCategory": "UtilitiesApplication", "description": t["descricao"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "BRL"},
        "downloadUrl": LINK["win"], "image": ENDERECO + "img/icone-512.png",
    }
    extra = f'<script type="application/ld+json">{json.dumps(dados, ensure_ascii=False)}</script>\n'
    if l == "pt":
        extra += '<script>try{var i=localStorage.getItem("reflex-idioma"),n=(navigator.language||"").slice(0,2);if(!i&&(n==="en"||n==="es")&&!/[?&]pt\\b/.test(location.search))location.replace(n+"/")}catch(e){}</script>\n'
    return (cabeca(l, t, t["titulo"], t["descricao"], r, "", extra) + topo(l, t, r, "") + corpo + rodape(l, t, r))

# ---------------------------------------------------------------- markdown simples (política)
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s

def md(texto):
    out, lista, tabela = [], False, []
    def fecha():
        nonlocal lista, tabela
        if lista: out.append("</ul>"); lista = False
        if tabela:
            linhas = [[c.strip() for c in x.strip("|").split("|")] for x in tabela if not re.match(r"^\|[-| ]+\|$", x)]
            h = "".join(f"<th>{inline(c)}</th>" for c in linhas[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in linhas[1:])
            out.append(f'<div class="tabela"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            tabela = []
    for linha in texto.splitlines():
        if linha.startswith("|"):
            tabela.append(linha.strip()); continue
        if linha.startswith("- "):
            if not lista: fecha(); out.append("<ul>"); lista = True
            out.append(f"<li>{inline(linha[2:])}</li>"); continue
        fecha()
        if linha.startswith("## "): out.append(f"<h2>{inline(linha[3:])}</h2>")
        elif linha.startswith("# "): out.append(f"<h1>{inline(linha[2:])}</h1>")
        elif linha.strip(): out.append(f"<p>{inline(linha)}</p>")
    fecha()
    return "\n".join(out)

def pagina_privacidade(l):
    t = T[l]; r = "../" if PASTA[l] else ""
    arq = os.path.join(RAIZ, "PRIVACIDADE.md") if l == "pt" else os.path.join(RAIZ, "site-fonte", f"privacidade-{l}.md")
    with open(arq, encoding="utf-8") as f:
        corpo = md(f.read())
    return (cabeca(l, t, t["priv_titulo"], t["priv_titulo"], r, "privacidade.html")
            + topo(l, t, r, "privacidade.html", "./")
            + f'<main class="secao"><article class="largura estreito texto">{corpo}<p><a class="botao botao-contorno" href="./">{t["voltar"]}</a></p></article></main>\n'
            + rodape(l, t, r))

def pagina_404():
    l = "pt"; t = T[l]
    # 404 usa caminhos absolutos a partir do endereço do site, porque pode abrir em qualquer pasta.
    r = ENDERECO
    txt = "".join(f'<p lang="{LANG_HTML[x]}"><b>{T[x]["nf_titulo"]}.</b> {T[x]["nf_texto"]}</p>' for x in IDIOMAS)
    return (cabeca(l, t, t["nf_titulo"] + " · Reflex", t["nf_texto"], r, "404.html").replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
            + f'<main class="secao"><div class="largura estreito texto centro"><img src="{r}img/icone-192.png" alt="" width="96" height="96">{txt}<p><a class="botao" href="{r}">Reflex</a></p></div></main>\n'
            + f'<script src="{r}site.js" defer></script></body></html>\n')

# ---------------------------------------------------------------- escrever
def grava(caminho, texto):
    p = os.path.join(SAIDA, caminho)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(texto)

for l in IDIOMAS:
    grava(PASTA[l] + "index.html", pagina_inicial(l))
    grava(PASTA[l] + "privacidade.html", pagina_privacidade(l))
grava("404.html", pagina_404())
grava("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {ENDERECO}sitemap.xml\n")
urls = "".join(f"  <url><loc>{ENDERECO}{PASTA[l]}{c}</loc></url>\n" for l in IDIOMAS for c in ["", "privacidade.html"])
grava("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
grava("site.webmanifest", json.dumps({
    "name": "Reflex", "short_name": "Reflex", "start_url": "./", "display": "browser",
    "background_color": "#0B1A22", "theme_color": "#0B1A22",
    "icons": [{"src": "img/icone-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "img/icone-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
grava(".nojekyll", "")
dominio = re.match(r"https?://([^/]+)/?$", ENDERECO)
cname = os.path.join(SAIDA, "CNAME")
if dominio and not dominio.group(1).endswith("github.io"):
    grava("CNAME", dominio.group(1) + "\n")
elif os.path.exists(cname):
    os.remove(cname)
print("Site gerado em", SAIDA, "para", ENDERECO)
