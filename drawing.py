from Pixart import *
import turtle as t

# Main function with menu options
def main():
    t.speed(0)
    t.penup()
    t.goto(-300, 300)
    t.pensize(1)
    t.pencolor("black")
    t.pendown()

    while True:
        print("Choose an option:")
        print("1. Draw color string of your choice")
        print("2. Draw a checkerboard pattern")
        print("3. Draw a pattern from a file")
        print("q. Quit")

        choice = input("Enter your choice (1, 2, 3, or q): ")

        if choice == 'q':
            break
        elif choice == '1':
            draw_shape_from_string(t)
        elif choice == '2':
            clear_screen()
            draw_grid(t)
        elif choice == '3':
            print("Choose a pattern to draw:")
            print("1. star.txt")
            print("2. yoda.txt")
            print("3. redmario.txt")
            print("4. greenmario.txt")
            pattern_choice = input("Enter the number (1-4): ")

            # Simple if-else to select the file
            if pattern_choice == "1":
                clear_screen()
                draw_shape_from_file("character_files/star.txt")
            elif pattern_choice == "2":
                clear_screen()
                t.screensize(canvwidth=3500,canvheight=1000)
                t.goto(-370,300)
                draw_shape_from_file("character_files/yoda.txt")
            elif pattern_choice == "3":
                clear_screen()
                draw_shape_from_file("character_files/redmario.txt")
            elif pattern_choice == "4":
                clear_screen()
                draw_shape_from_file("character_files/greenmario.txt")
            else:
                print("Invalid choice. Please select a valid pattern.")
        else:
            print("Invalid choice. Please select 1, 2, 3, or q to quit.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()