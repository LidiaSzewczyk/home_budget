from commands.show_all import ShowAll


class UsersCommands:
    def __init__(self):
        self._id_to_update = ''
        self._update_category = ''
        self._update_content = ''
        self._update_content_created = ''
        self._filter_by_time = ''

    @property
    def id_to_update(self):
        self._id_to_update = input('Provide id of the expense you want modify.\n')
        return self._id_to_update

    @property
    def update_category(self):
        self._update_category = input(
            'Select the appropriate number if you want to change:\n category - 1\n name - 2\n amount - 3\n date of creation - 4\n')
        return self._update_category

    @property
    def update_content(self):
        self._update_content = input('Provide new value\n')
        return self._update_content

    @property
    def update_content_time(self):
        self._update_content_time = input('Provide new value as yyyy-mm-dd.\n')
        return self._update_content_time

    @property
    def filter_by_time(self):
        self._filter_by_time = input(
            'Select the appropriate number if you want to display:\n this day - 1\n this week - 2\n this month - 3\n last month - 4\n this year - 5\n select dates - 6\n')
        return self._filter_by_time
