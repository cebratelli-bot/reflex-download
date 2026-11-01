# Como colocar o site do Reflex no ar

O site está pronto na pasta `docs/`. São só arquivos HTML, CSS, imagens e um pouco de JavaScript, sem banco de dados e sem PHP, então ele roda em qualquer hospedagem.

Os botões de download apontam para os arquivos da última versão publicada no GitHub. Quando você publica uma atualização do Reflex, o site já passa a baixar a versão nova sozinho, sem mexer em nada.

---

## Opção 1 (recomendada): GitHub Pages, grátis

O site fica hospedado no próprio GitHub, de graça, com HTTPS (cadeado) e sem limite de visitas para um site deste tamanho.

1. Aprove (merge) o pull request do site no repositório **reflex-download**.
2. Abra https://github.com/cebratelli-bot/reflex-download/settings/pages
3. Em **Build and deployment > Source**, escolha **Deploy from a branch**.
4. Em **Branch**, escolha **main** e a pasta **/docs**. Clique em **Save**.
5. Espere 1 ou 2 minutos e atualize a página. Vai aparecer: *Your site is live at* **https://cebratelli-bot.github.io/reflex-download/**

Pronto, esse já é o link do site. Pode colocar na bio do Instagram, na Play Store e onde quiser.

---

## Opção 2: um endereço próprio, tipo `reflexapp.com.br`

Um domínio próprio custa cerca de **R$ 40 por ano** no Registro.br (para `.com.br`) ou uns US$ 10 a 15 por ano em sites como Cloudflare, Namecheap ou GoDaddy (para `.com`). A hospedagem continua grátis no GitHub Pages.

### 1. Compre o domínio

1. Entre em https://registro.br e pesquise o nome que você quer (por exemplo `reflexapp.com.br` ou `baixarreflex.com.br`).
2. Se estiver livre, registre com seu CPF e pague o boleto ou Pix. A liberação leva de minutos a algumas horas.

### 2. Aponte o domínio para o GitHub

No Registro.br, abra o domínio, vá em **DNS > Editar zona** (se pedir, clique antes em *Utilizar DNS do Registro.br*) e crie estes registros:

| Tipo | Nome | Valor |
|---|---|---|
| A | (deixe vazio) | 185.199.108.153 |
| A | (deixe vazio) | 185.199.109.153 |
| A | (deixe vazio) | 185.199.110.153 |
| A | (deixe vazio) | 185.199.111.153 |
| CNAME | www | cebratelli-bot.github.io |

Salve. Em outros sites de domínio (Cloudflare, GoDaddy, Hostinger) o nome do menu muda, mas os registros são os mesmos. No campo *Nome*, o vazio às vezes aparece como `@`.

### 3. Avise o GitHub

1. Volte em https://github.com/cebratelli-bot/reflex-download/settings/pages
2. Em **Custom domain**, digite `www.seudominio.com.br` e clique em **Save**.
3. Espere a verificação ficar verde (pode levar de 10 minutos a algumas horas, é o tempo da internet aprender o endereço novo).
4. Marque **Enforce HTTPS**.

### 4. Me avise o domínio

Me mande o domínio que você comprou. Eu gero o site de novo com ele, para os links de compartilhamento (WhatsApp, Instagram), o mapa do site para o Google e o arquivo `CNAME` ficarem certos. Se quiser fazer sozinho, é este comando na pasta do repositório:

```
ENDERECO=https://www.seudominio.com.br/ python3 site-fonte/gerar.py
```

---

## Opção 3: uma hospedagem paga que você já tenha (Hostinger, HostGator, Locaweb...)

1. Baixe o **Reflex-Site.zip** e descompacte.
2. Entre no painel da hospedagem e abra o **Gerenciador de arquivos**.
3. Abra a pasta **public_html** (às vezes se chama `www` ou `htdocs`).
4. Envie **todo o conteúdo** da pasta `site` para dentro dela (o `index.html` tem que ficar direto dentro de `public_html`, não dentro de outra pasta).
5. Abra o seu domínio no navegador. O site já aparece.

Dica: o arquivo `.nojekyll` e o `CNAME` só servem para o GitHub. Numa hospedagem comum eles podem ser apagados ou ficar lá, não atrapalham.

## Opção 4: Netlify, grátis e sem GitHub

1. Entre em https://app.netlify.com/drop (crie a conta grátis se pedir).
2. Arraste a pasta `site` descompactada para a página.
3. Em segundos aparece um link como `https://nome-aleatorio.netlify.app`. Em **Site configuration > Change site name** dá para trocar por `reflex-app.netlify.app`, se o nome estiver livre.
4. Domínio próprio: **Domain management > Add a domain**, e siga as instruções de DNS que o Netlify mostrar.

---

## Depois que o site estiver no ar

- **Instagram:** troque o link da bio pelo endereço do site.
- **Google:** cadastre o site em https://search.google.com/search-console e envie o mapa `sitemap.xml` (ex.: `https://www.seudominio.com.br/sitemap.xml`) para o site aparecer nas buscas mais rápido.
- **Play Store:** a política de privacidade também está no site (`/privacidade.html`). Dá para usar esse endereço no Play Console, no campo *Política de privacidade*.

## O que tem no site

- Página inicial em português, inglês (`/en/`) e espanhol (`/es/`). Quem abre com o celular ou PC em inglês ou espanhol vai direto para a sua língua.
- Botões de download que se ajustam ao aparelho: no Windows, o instalador aparece primeiro; no Android, a Google Play.
- Downloads do celular (Google Play e APK), do Windows e da TV, com a versão mais nova lida na hora.
- Recursos, fotos das telas, como usar, como instalar, plano grátis e Pro, dúvidas frequentes.
- Política de privacidade nas 3 línguas e página de erro 404.

## Como mudar textos

Os textos ficam no arquivo `site-fonte/gerar.py` (um bloco por idioma). Depois de mudar, rode `python3 site-fonte/gerar.py` e a pasta `docs/` é refeita. Ou é só me pedir.
