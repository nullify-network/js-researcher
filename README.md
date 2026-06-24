<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:060606,60:141414,100:2e2e2e&text=JS%20Researcher&fontColor=ffffff&fontSize=58&fontAlignY=38&desc=JavaScript%20recon%20%C2%B7%20endpoint%20discovery&descAlignY=60&descColor=bdbdbd" width="100%" />

<a href="https://nullify.network"><img src="https://img.shields.io/badge/nullify.network-0a0a0a?style=for-the-badge&logo=firefox&logoColor=ffffff" /></a>
<a href="https://t.me/nullifynetwork"><img src="https://img.shields.io/badge/@nullifynetwork-0a0a0a?style=for-the-badge&logo=telegram&logoColor=ffffff" /></a>
<a href="https://github.com/nullify-network"><img src="https://img.shields.io/badge/nullify--network-0a0a0a?style=for-the-badge&logo=github&logoColor=ffffff" /></a>
<img src="https://img.shields.io/badge/python-3.8+-2e2e2e?style=for-the-badge&labelColor=0a0a0a&logo=python&logoColor=ffffff" />

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=2800&pause=900&color=ffffff&center=true&vCenter=true&width=620&lines=Crawl+JS+sources+from+any+target;Pull+hidden+endpoints+out+of+the+code;Map+the+attack+surface+before+attackers+do" />

</div>

<br/>

## ◆ What it does

`js-researcher` scrapes a target page for every JavaScript file it references, then digs through that code to surface internal paths and API endpoints that aren't visible in the UI — fast attack-surface mapping for recon.

| Stage | What happens |
|-------|--------------|
| **🛰️ Source discovery** | Parses the page HTML and collects all `.js` files from `<script src>` and `<a href>` |
| **🔍 Endpoint extraction** | Downloads each script and pulls path-like strings (`/api/...`, `/admin/...`) out of the source |
| **🧩 URL resolution** | Resolves relative and absolute sources correctly via `urljoin` |
| **🎯 Clean output** | Colour-coded, de-duplicated, sorted results straight to your terminal |

<br/>

## ◆ Install

```bash
git clone https://github.com/nullify-network/js-researcher.git
cd js-researcher
pip install requests beautifulsoup4 colorama
```

<br/>

## ◆ Usage

```bash
python3 js-researcher.py <target>
```

```bash
python3 js-researcher.py example.com
python3 js-researcher.py https://app.example.com
```

<br/>

## ◆ Example

```text
 [<3] JS Researcher.
 [<3] Coded by nullify-network

 [+] Sources found on https://example.com :
  [+] Checking  https://example.com/static/app.js :
   [+]> /api/v1/users
   [+]> /api/v1/session
   [+]> /admin/dashboard
  [+] Checking  https://example.com/static/vendor.js :
   [-] No endpoints found in https://example.com/static/vendor.js
```

<br/>

## ◆ Notes

- Sends a real browser `User-Agent` and a 15s timeout on every request.
- Handles `.js?v=123` cache-busted sources and relative paths.
- Discovery only — it lists what the JavaScript exposes; verifying those endpoints is on you.

<br/>

## ◆ Principles

> Only test what you have legal right to test. This tool is for authorized security testing, bug bounty, and research. You are responsible for how you use it.

<br/>

<div align="center">

<a href="https://nullify.network"><img src="https://img.shields.io/badge/🚀_Start_at_nullify.network-2e2e2e?style=for-the-badge&labelColor=0a0a0a" /></a>
<a href="https://t.me/nullifynetwork"><img src="https://img.shields.io/badge/Talk_to_us-0a0a0a?style=for-the-badge&logo=telegram&logoColor=ffffff" /></a>

<img src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=120&color=0:2e2e2e,40:141414,100:060606" width="100%" />

</div>
