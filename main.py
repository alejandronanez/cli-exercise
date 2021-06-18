import sys

codes = {
    'total_sortable_options': 5,
    'reorder_list': 6,
    'exit_program': 7,
}


# Add indexes to each one of the options
def format_options(options_list):
    result = []
    for index, value in enumerate(options_list):
        result.append(str(index + 1) + ') ' + value)

    return result


def show_options(options):
    option = input(
        """
Select one option:
%s
""" % "\n".join(format_options(options)))
    return int(option)


# Asks for new order, and then returns the new list (ordered)
def reoder_options(options):
    value_selected = int(input(
        """
What's your new favorite?:
%s
""" % "\n".join(format_options(options))))

    # Make the value an int, since what's coming from the terminal is a string.

    if value_selected == codes['exit_program']:
        print('Hasta la vista, baby')
        sys.exit()

    if value_selected > codes['total_sortable_options']:
        print('You cannot chose anything greater than 5')
        reoder_options(options)

    # Grabbed from https://stackoverflow.com/a/2177716
    # Replace options[0] with options[value_selected - 1] and viceversa
    options[0], options[value_selected - 1] = options[value_selected - 1], options[0]
    return options


def main(options):
    # Ask the questions
    option_selected = show_options(options)

    if option_selected == codes['exit_program']:
        print('Hasta la vista, baby.')
        sys.exit()

    if option_selected == codes['reorder_list']:
        prompt_options = reoder_options(options)
        main(prompt_options)

    main(options)


main([
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Change order',
    'End program'
])
