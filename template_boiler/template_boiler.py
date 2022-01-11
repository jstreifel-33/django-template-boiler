def create_boiler(dest, name, template):
    with open(f"template_boiler/boilerplate/{template}", "r") as f:
        content = f.read()

    with open(f"{dest}/{name}{template}", "w") as f:
        f.write(content)


if __name__ == "__main__":
        
    destination = input("Please provide template path\n(use pwd to get absolute path)\n>")
    template_name = input("Template name?\n>")

    boiler_plate = ["_create.html", "_delete.html", "_list.html", "_update.html"]


    with open(f"template_boiler/boilerplate/base.html", "r") as f:
        content = f.read()

    with open(f"{destination}/base.html", "w") as f:
        content = f.write(content)


    for template in boiler_plate:
        create_boiler(destination, template_name, template)