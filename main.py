import asyncio
from playwright.async_api import async_playwright
import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://blaze.bet.br/pt/games/double")

        ultimos = []
        while True:
            await page.reload()
            await page.wait_for_selector(".entries .entry")
            results = await page.eval_on_selector_all(".entries .entry", "els => els.map(el => el.textContent.trim())")
            results = results[:10]

            if results != ultimos:
                ultimos = results
                ultima = results[0]
                msg = f"Últimos resultados: {results}\n"
                if ultima in ['2', '4', '8']:
                    msg += f"SINAL: Aposte na COR VERMELHA"
                else:
                    msg += f"SINAL: Aposte na COR PRETA"
                send_telegram_message(msg)
            await asyncio.sleep(10)

asyncio.run(main())
