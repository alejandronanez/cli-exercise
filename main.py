import sys

from prompt_toolkit import PromptSession

# Create prompt object.
prompt_session = PromptSession()


# Add indexes to each one of the options
def format_options(list):
    result = []
    for index, value in enumerate(list):
        result.append(str(index + 1) + ') ' + value)

    return result


def show_options(options):
    option = prompt_session.prompt(
        """
Select one option:
%s
""" % "\n".join(format_options(options)))
    return int(option)


# Asks for new order, and then returns the new list (ordered)
def reoder_options(options):
    value_selected = prompt_session.prompt(
        """
What's your new favorite?:
%s
""" % "\n".join(format_options(options)))

    # Make the value an int, since what's coming from the terminal is a string.
    value_selected_as_int = int(value_selected)

    if value_selected_as_int == 7:
        print('Hasta la vista, baby')
        sys.exit()

    if value_selected_as_int > 5:
        print('You cannot chose anything greater than 5')
        reoder_options(options)

    # Grabbed from https://stackoverflow.com/a/2177716
    options[0], options[value_selected_as_int - 1] = options[value_selected_as_int - 1], options[0]
    return options


def main(options):
    # Ask the questions
    option_selected = show_options(options)

    if option_selected == 7:
        print('Hasta la vista, baby.')
        sys.exit()

    if option_selected == 6:
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
