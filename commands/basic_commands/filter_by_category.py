from commands.abs_command import AbsCommand
from commands.by_category.show_elements_category import ShowElementsCategory
from commands.by_category.show_elements_select_category import ShowElementsSelectCategory
from commands.by_category.show_sum_elements_category import ShowSumElementsCategory
from commands.cli import Cli


class FilterByCategory(AbsCommand):
    name = 'Filter by category'

    def execute(self):
        commands = (ShowElementsCategory, ShowElementsSelectCategory, ShowSumElementsCategory)

        filter = Cli(commands)
        filter.get_user_command()
