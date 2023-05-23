from src.domain.menu.MainMenu import MainMenu

main_menu = MainMenu.get_instance()

while True:
    main_menu.print_menu()
