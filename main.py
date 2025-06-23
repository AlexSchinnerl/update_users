from gui import MainWindow, Input_Form, Apply_Button

def main():
    roles = MainWindow()
    input_form = Input_Form(roles)
    Apply_Button(roles, input_form)
    roles.mainloop()


if __name__ == "__main__":
    main()

