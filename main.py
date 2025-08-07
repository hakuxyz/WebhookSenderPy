import requests
import json
import time

def send_webhook(url, content=None, username=None, avatar_url=None, embed=False):
    data = {
        "username": username or "WebhookSender",
        "avatar_url": avatar_url or None,
    }

    if embed:
        data["embeds"] = [{
            "title": "Embed Message",
            "description": content or "No content",
            "color": 0x3498db
        }]
    else:
        data["content"] = content or "No content"

    try:
        res = requests.post(url, json=data)
        if res.status_code in [200, 204]:
            print("[✓] Webhook sent successfully.")
        else:
            print(f"[!] Failed to send webhook: {res.status_code} | {res.text}")
    except Exception as e:
        print(f"[!] Error: {e}")


def mass_spam(url, content, amount, delay=0.5, embed=False):
    for i in range(amount):
        print(f"Sending {i+1}/{amount}...")
        send_webhook(url, content, embed=embed)
        time.sleep(delay)


def preview_webhook(content, embed=False):
    print("\n== Webhook Preview ==")
    if embed:
        print(f"[Embed]\nTitle: Embed Message\nDescription: {content}")
    else:
        print(f"[Message]\n{content}")
    print("="*25)


def show_menu():
    print("\n=== WebhookSender Python ===")
    print("1) Send Webhook")
    print("2) Mass Webhook Spam")
    print("3. Preview Message")
    print("4. Exit")


def main():
    while True:
        show_menu()
        try:
            choice = input(">").strip()
        except EOFError:
            break  # for jupyter/limited environments

        if choice == "1":
            url = input("Webhook URL: ").strip()
            content = input("Message: ").strip()
            embed = input("Use embed? (y/n): ").lower().startswith("y")
            username = input("Custom Username (leave empty for default): ").strip()
            avatar = input("Avatar URL (optional): ").strip()

            send_webhook(url, content, username, avatar, embed)

        elif choice == "2":
            url = input("Webhook URL: ").strip()
            content = input("Message to spam: ").strip()
            try:
                amount = int(input("Amount of messages: ").strip())
                delay = float(input("Delay between messages (sec): ").strip())
            except:
                print("[!] Invalid input.")
                continue
            embed = input("Use embed? (y/n): ").lower().startswith("y")
            mass_spam(url, content, amount, delay, embed)

        elif choice == "3":
            content = input("Enter message to preview: ").strip()
            embed = input("[?] Show as embed? (y/n): ").lower().startswith("y")
            preview_webhook(content, embed)

        elif choice == "4":
            print("[!] Exiting..")
            break
        else:
            print("[!] Invalid choice.")


if __name__ == "__main__":
    main()