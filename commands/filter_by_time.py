from datetime import datetime, date, timedelta

from commands.abs_command import AbsCommand
from commands.users_commands import UsersCommands


class FilterByTime(AbsCommand):
    name = 'Filter by time'

    def execute(self):
        command_id = int(input(
            'Select the appropriate number if you want to display:\n this day - 1\n this week - 2\n this month - 3\n last month - 4\n this year - 5\n select dates - 6\n')
        )

        if command_id == 1:
            for amount in self.dashboard:
                end_date = date.today() + timedelta(days=1)

                if date.today().strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)
        elif command_id == 2:
            for amount in self.dashboard:
                start_date = date.today() - timedelta(days=6)
                end_date = date.today() + timedelta(days=1)

                if start_date.strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)

        elif command_id == 3:
            for amount in self.dashboard:
                start_date = date.today().replace(day=1)
                end_date = date.today() + timedelta(days=1)
                if start_date.strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)

        elif command_id == 4:
            for amount in self.dashboard:
                start_date = date.today().replace(day=1, month=date.today().month - 1)
                end_date = date.today().replace(day=1)

                if start_date.strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)

        elif command_id == 5:
            for amount in self.dashboard:
                start_date = date.today().replace(day=1, month=1)
                end_date = date.today() + timedelta(days=1)
                if start_date.strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)

                    print(start_date.strftime('%Y%m%d%H%M'))
                    print(end_date.strftime('%Y%m%d%H%M'))

        elif command_id == 6:
            start_date = input('Provide start date as yyyy-mm-dd\n')
            end_date = input('Provide end date as yyyy-mm-dd\n')

            if start_date == '':
                start_date = datetime.now()
                for amount in self.dashboard:
                    if start_date.strftime('%Y%m%d%H%M') > amount.created.strftime('%Y%m%d%H%M'):
                        start_date = amount.created
            else:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')

            if end_date == '':
                end_date = datetime.now()
            elif len(end_date.strip()) == 10:
                end_date = datetime.strptime(end_date, '%Y-%m-%d')

            end_date = end_date + timedelta(days=1)

            for amount in self.dashboard:
                if start_date.strftime('%Y%m%d%H%M') <= amount.created.strftime('%Y%m%d%H%M') < end_date.strftime(
                        '%Y%m%d%H%M'):
                    print(amount)
