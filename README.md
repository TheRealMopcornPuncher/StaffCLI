# Welcome to StaffCLI!

StaffCLI is a terminal-only program that helps a user tune their instrument or identify the note of a sound being received by your microphone, entirely in the terminal!

Although there's not a major functional aspect to this program, it's more of an art project if anything, I made it to learn how people create updating menus in the terminal.. seriously... it's cool.

(Also, I know that I usually am I DIE-HARD C user, but I decided to use Python for the sake of my sanity since making a TUI in C is harder than installing Arch. (Probably))
```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  _______ _________ _______  _______  _______  _______  _       _________
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(  ____ \\__   __/(  ___  )(  ____ \(  ____ \(  ____ \( \      \__   __/
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⣠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| (    \/   ) (   | (   ) || (    \/| (    \/| (    \/| (         ) (   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| (_____    | |   | (___) || (__    | (__    | |      | |         | |   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(_____  )   | |   |  ___  ||  __)   |  __)   | |      | |         | |   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⢠⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ) |   | |   | (   ) || (      | (      | |      | |         | |   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠁⢠⣾⣿⠿⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀/\____) |   | |   | )   ( || )      | )      | (____/\| (____/\___) (___⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⣿⠁⢿⡄⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀\_______)   )_(   |/     \||/       |/       (_______/(_______/\_______/⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⡀⠙⠆⠸⣇⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣶⣤⠀⣿⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣷⣦⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
