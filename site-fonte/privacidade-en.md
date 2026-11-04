# Reflex: Privacy Policy

*Last updated: November 4, 2026. Applies to the Reflex apps (phone), Reflex TV, Reflex for Windows and Reflex for Mac.*

**Responsible party:** REFLEXX, developer of Reflex. **Contact:** through the support e-mail shown on the Reflex page on Google Play.

## Summary

- **Your screen is yours alone.** The picture and sound Reflex streams go straight from your phone to your PC or TV, over your own Wi-Fi network. Nothing from your screen is recorded or sent to the internet, to us or to third parties.
- **No ads.** Reflex shows no ads and does not use the device advertising ID.
- **Anonymous usage count.** Once a day Reflex tells Google Analytics that it was opened, just so we know how many people use the app. It sends a random number created on the device, the version and the language, nothing that identifies you. You can turn it off.
- **Reflex Account (optional).** If you sign in with Google, we store your name, email and whether you have Reflex Pro, so Pro works on your phone and your PC. You can use Reflex without signing in and delete the account anytime.
- **Purchases through Google Play.** Reflex Pro is a subscription (monthly or yearly) sold through Google Play, which you cancel in the Play Store itself. We do not receive or store your payment details.

## What the app accesses and why

- **Screen capture:** to show the phone screen on the PC or TV. It only works after you tap start and accept the Android notice, and it stops when you turn it off.
- **Audio ("record audio" permission):** to stream app sound (videos, games, music). Reflex does not use the microphone.
- **Notifications:** to show that mirroring is on and let you stop it from there.
- **Local network:** to send the picture to the PC or TV and so they can find the phone on the network.
- **Accessibility (optional, only in the version with control):** to perform on the phone the clicks, swipes and text you enter on the connected PC. It only acts while mirroring is on and never reads or sends screen content outside your network.
- **Internet:** to check the Reflex Pro subscription on Google Play, look for updates, sign in to the Reflex Account (if you want) and send the anonymous usage count (below).

## Reflex Account

The Reflex Account is optional. It lets Reflex Pro subscribed on your phone also work in Reflex on your PC, and come back on its own when you change devices.

- **How you sign in:** with your Google account (on the phone, through Google's own window; on the PC, through the browser). We don't create a password and never receive your Google password.
- **What we store:** your Google account identifier, your name, your email, whether you want news by email, the Google Play subscription token linked to the account, its expiry date, and the dates the account was created and last used.
- **Why:** to unlock Reflex Pro on the devices where you signed in. Your email is only used to send news if you turn that option on, and you can turn it off anytime. We don't sell or share this data.
- **Where:** on a Reflex server at Cloudflare (Cloudflare Workers and D1 database), always over an encrypted connection (HTTPS). To check the subscription, the server queries Google Play.
- **How long:** while the account exists. When you delete the account, all of it is deleted right away.
- **How to delete:** in the app, Reflex Pro tab > Reflex Account > **Delete account**, or on the web at [reflex-conta.reflexapp.workers.dev/apagar](https://reflex-conta.reflexapp.workers.dev/apagar). The Google Play subscription continues until you cancel it in the Play Store.

## Anonymous usage count

Once a day, when you open Reflex (phone, TV or PC), the app sends Google Analytics a single notice with:

- a random number created by the app itself the first time (it is not the advertising ID or the device number, and it is not linked to any account);
- the app type (phone, TV or PC), the Reflex version and the chosen language.

No name, e-mail, Google account, app list or anything shown on the screen is sent. Google receives the internet address (IP) of the connection to estimate the country and does not keep it in reports. We only use totals (how many people used it per day and per platform). To turn it off: on the phone, in Settings > Privacy > **Anonymous usage statistics**; on the PC, in Settings > **Anonymous usage statistics**. Clearing the app data also deletes the random number.

## Data handled by third parties

| Service | Data | Purpose |
|---|---|---|
| Google Play (purchases) | Google account and purchase record | Process the Reflex Pro payment and unlock the subscription |
| Cloudflare (Reflex Account server) | Name, email, Google account identifier and Reflex Pro status | Store the Reflex Account, only if you sign in |
| Google (sign-in) | Google account | Confirm who is signing in to the Reflex Account |
| Google Analytics | App random number, platform, version, language and approximate country | Count how many people use Reflex (can be turned off) |

This data is handled by Google under the [Google Privacy Policy](https://policies.google.com/privacy). Cloudflare handles Reflex Account data under the [Cloudflare Privacy Policy](https://www.cloudflare.com/privacypolicy/). From the usage count we only see totals in the Google Analytics dashboard.

## Your rights

Under data protection laws such as Brazil's LGPD and the GDPR, you can ask about your data through the contact above. You can view, correct or delete your Reflex Account data anytime (delete it right in the app or on the page above). Requests about payments are handled by Google.

## Children

Reflex is not directed at children under 13.

## Changes

If this policy changes, the new version will be published at this address with the updated date.
