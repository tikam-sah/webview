import flet as ft

def main(page: ft.Page):
    page.title = "WebView App"
    page.window_width = 400
    page.window_height = 700

    webview = ft.WebView(
        url="https://sms.ebinayah.com/",  # Change this to your website
        expand=True
    )

    page.add(webview)

ft.app(target=main)
