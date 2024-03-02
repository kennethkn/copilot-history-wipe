from selenium import webdriver
from selenium.webdriver.common.by import By

print("clear-bing-chats: Script started")
try:
    driver = webdriver.Edge()
    print("clear-bing-chats: Opened Edge browser")
    driver.get("https://www.bing.com/chat?form=NTPCHB")
    print("clear-bing-chats: Opened Bing Chat")
    while (
        not input(
            "clear-bing-chats: Sign into your Microsoft account before proceeding. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    while (
        not input(
            "clear-bing-chats: Make sure the 'Recents' panel containing your recent chats is visible. You can reload the page if it's not there. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    first_run = True
    while (
        True
        if first_run
        or input(
            "clear-bing-chats: DONE. Reload the page to see if there's more and press enter to rerun the script as needed. To quit, interrupt python (Ctrl+C)"
        )
        else True
    ):
        try:
            side_panel_shadow_root = (
                driver.find_element(By.CSS_SELECTOR, ".cib-serp-main")
                .shadow_root.find_element(By.CSS_SELECTOR, "cib-side-panel")
                .shadow_root
            )
            try:
                show_recent_btn = side_panel_shadow_root.find_element(
                    By.CSS_SELECTOR, ".show-recent"
                )
                if show_recent_btn.text == "See all recent chats":
                    show_recent_btn.click()
                    print("clear-bing-chats: Clicked 'See all recent chats' button")
                else:
                    print(
                        "clear-bing-chats: Assume 'See all recent chats' button is already clicked"
                    )
            except:
                print("clear-bing-chats: 'See all recent chats' button not found")
            cib_thread_hosts = side_panel_shadow_root.find_elements(
                By.CSS_SELECTOR, "cib-thread"
            )
            count = 0
            for th in cib_thread_hosts:
                driver.execute_script(
                    "arguments[0].click();",
                    th.shadow_root.find_element(By.CSS_SELECTOR, ".delete.icon-button"),
                )
                count += 1
                print(f"clear-bing-chats: Deleted a chat (Total: {count})")
        except Exception as e:
            print(e)
        first_run = False
except KeyboardInterrupt:
    print("\nclear-bing-chats: Keyboard interrupt detected. Quitting...")
    driver.quit()
except Exception as e:
    print(e)
