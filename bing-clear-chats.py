from selenium import webdriver
from selenium.webdriver.common.by import By

print("bing-clear-chats: Script started")
try:
    driver = webdriver.Edge()
    print("bing-clear-chats: Opened Edge browser")
    driver.get("https://www.bing.com/chat?form=NTPCHB")
    print("bing-clear-chats: Opened Bing Chat")
    while (
        not input(
            "bing-clear-chats: Sign into your Microsoft account before proceeding. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    while (
        not input(
            "bing-clear-chats: Make sure the 'Recents' panel containing your recent chats is visible. You can reload the page if it's not there. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    first_run = True
    while (
        True
        if first_run
        or input(
            "bing-clear-chats: DONE. Reload the page to see if there's more and press enter to rerun the script as needed. To quit, interrupt python (Ctrl+C)"
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
                    print("bing-clear-chats: Clicked 'See all recent chats' button")
                else:
                    print(
                        "bing-clear-chats: Assume 'See all recent chats' button is already clicked"
                    )
            except:
                print("bing-clear-chats: 'See all recent chats' button not found")
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
                print(f"bing-clear-chats: Deleted a chat (Total: {count})")
        except Exception as e:
            print(e)
        first_run = False
except KeyboardInterrupt:
    print("\nbing-clear-chats: Keyboard interrupt detected. Quitting...")
    driver.quit()
except Exception as e:
    print(e)
