# Reflex: Política de Privacidade

*Última atualização: 4 de novembro de 2026. Vale para os apps Reflex (celular), Reflex TV, Reflex para Windows e Reflex para Mac.*

**Responsável:** REFLEXX, desenvolvedor do Reflex. **Contato:** pelo e-mail de suporte que aparece na página do Reflex no Google Play.

## Resumo

- **A sua tela é só sua.** A imagem e o som que o Reflex transmite vão direto do seu celular para o seu PC ou TV, pela sua própria rede Wi-Fi. Nada da sua tela é gravado nem enviado para a internet, para nós ou para terceiros.
- **Sem anúncios.** O Reflex não mostra anúncios e não usa o identificador de publicidade do aparelho.
- **Contagem anônima de uso.** Uma vez por dia o Reflex avisa o Google Analytics que foi aberto, só para sabermos quantas pessoas usam o app. Vai um número aleatório criado no aparelho, a versão e o idioma, nada que identifique você. Dá para desligar.
- **Conta Reflex (opcional).** Se você entrar com o Google, guardamos seu nome, e-mail e se você tem o Reflex Pro, para o Pro valer no celular e no PC. Dá para usar o Reflex sem entrar e apagar a conta quando quiser.
- **Compras pelo Google Play.** O Reflex Pro é uma assinatura (mensal ou anual) vendida pelo Google Play, que se cancela na própria Play Store. Não recebemos nem guardamos seus dados de pagamento.

## O que o app acessa e por quê

- **Captura de tela:** para mostrar a tela do celular no PC ou na TV. Só funciona depois que você toca em iniciar e aceita o aviso do Android, e para quando você desliga.
- **Áudio (permissão "gravar áudio"):** para transmitir o som dos apps (vídeos, jogos, música). O Reflex não usa o microfone.
- **Notificações:** para mostrar que o espelhamento está ligado e permitir parar por ali.
- **Rede local:** para enviar a imagem ao PC ou TV e para que eles encontrem o celular na rede.
- **Acessibilidade (opcional, só na versão com controle):** para executar no celular os cliques, deslizes e textos que você faz no PC conectado. Só age enquanto o espelhamento está ligado e nunca lê nem envia o conteúdo da tela para fora da sua rede.
- **Internet:** para conferir a assinatura do Reflex Pro no Google Play, procurar atualizações, entrar na Conta Reflex (se você quiser) e enviar a contagem anônima de uso (abaixo).

## Conta Reflex

A Conta Reflex é opcional. Ela existe para o Reflex Pro assinado no celular valer também no Reflex do PC e voltar sozinho quando você troca de aparelho.

- **Como entra:** com a sua conta Google (no celular, pela janela do próprio Google; no PC, pelo navegador). Não criamos senha e não recebemos a sua senha do Google.
- **O que guardamos:** o identificador da sua conta Google, seu nome, seu e-mail, se você quer receber novidades por e-mail, o código da assinatura do Google Play ligado à conta, a data em que ela vence e as datas de criação e último uso.
- **Para quê:** liberar o Reflex Pro nos aparelhos em que você entrou. O e-mail só é usado para mandar novidades se você marcar essa opção, e dá para desmarcar a qualquer momento. Não vendemos nem compartilhamos esses dados.
- **Onde fica:** num servidor do Reflex no Cloudflare (Cloudflare Workers e banco D1), com a conexão sempre criptografada (HTTPS). Para conferir a assinatura, o servidor consulta o Google Play.
- **Por quanto tempo:** enquanto a conta existir. Ao apagar a conta, tudo isso é apagado na hora.
- **Como apagar:** no app, na aba Reflex Pro > Conta Reflex > **Apagar conta**, ou pela web em [reflex-conta.reflexapp.workers.dev/apagar](https://reflex-conta.reflexapp.workers.dev/apagar). A assinatura do Google Play continua até você cancelar na Play Store.

## Contagem anônima de uso

Uma vez por dia, quando você abre o Reflex (celular, TV ou PC), o app envia ao Google Analytics um único aviso com:

- um número aleatório criado pelo próprio app na primeira vez (não é o identificador de publicidade, nem o número do aparelho, e não está ligado a nenhuma conta);
- o tipo de app (celular, TV ou PC), a versão do Reflex e o idioma escolhido.

Não vai nome, e-mail, conta Google, lista de apps, nem nada do que aparece na tela. O Google recebe o endereço de internet (IP) da conexão para estimar o país e não o guarda nos relatórios. Usamos só os totais (quantas pessoas usaram por dia e por plataforma). Para desligar: no celular, em Configurações > Privacidade > **Estatísticas anônimas de uso**; no PC, em Configurações > **Estatísticas anônimas de uso**. Apagar os dados do app também apaga o número aleatório.

## Dados tratados por terceiros

| Serviço | Dados | Para quê |
|---|---|---|
| Google Play (compras) | Conta Google e registro da compra | Processar o pagamento do Reflex Pro e liberar a assinatura |
| Cloudflare (servidor da Conta Reflex) | Nome, e-mail, identificador da conta Google e estado do Reflex Pro | Guardar a Conta Reflex, só se você entrar |
| Google (login) | Conta Google | Confirmar quem está entrando na Conta Reflex |
| Google Analytics | Número aleatório do app, plataforma, versão, idioma e país aproximado | Contar quantas pessoas usam o Reflex (pode ser desligado) |

Esses dados são tratados pelo Google de acordo com a [Política de Privacidade do Google](https://policies.google.com/privacy). O Cloudflare trata os dados da Conta Reflex de acordo com a [Política de Privacidade do Cloudflare](https://www.cloudflare.com/privacypolicy/). Da contagem de uso, vemos só os totais no painel do Google Analytics.

## Seus direitos

Pela LGPD, você pode pedir informações sobre seus dados pelo contato acima. Você pode ver, corrigir ou apagar os dados da Conta Reflex a qualquer momento (apagar direto no app ou na página acima). Os pedidos sobre pagamentos são atendidos pelo Google.

## Crianças

O Reflex não é direcionado a crianças menores de 13 anos.

## Mudanças

Se esta política mudar, a nova versão será publicada neste endereço com a data atualizada.
