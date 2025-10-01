# explaining for skills test
from pyscript import display, document


def ordering_form(e):
    item1 = document.getElementById("menu1")
    item2 = document.getElementById("menu2")
    item3 = document.getElementById("menu3")
    item4 = document.getElementById("menu4")

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked)

    display(f'Your total is {total}', target="output")

    name = document.getElementById("name").value
    contact = document.getElementById("contact").value
    address = document.getElementById("address").value

    display(f"My name is {name} and my Contact number is {contact} I live at {address}", target="output")