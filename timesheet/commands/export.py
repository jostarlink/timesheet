from _ast import Import

__author__ = 'vahid'

import sys
import csv
from timesheet.commands import Command
from timesheet.models import Task, Subject


class ExportCommand(Command):
    name = 'export'
    description = 'Export the database into csv file with columns: subject, task, start, end'

    def add_arguments(self):
        self.parser.add_argument('output', nargs='?', help="Output filename. if omitted, "
                                                           "the standard output will be used")
        self.parser.add_argument('-s', '--subject', action='append', default=[], help="Subject to filter the result, ")

    def do_job(self):

        if self.args.output:
            csv_file = open(self.args.output, 'w')
        else:
            csv_file = sys.stdout

        try:
            query = Task.query.join(Task.subject).order_by(Subject.entry_time, Task.start_time)
            if self.args.subject:
                query = query.filter(Subject.title.in_(self.args.subject))

            writer = csv.writer(csv_file)
            for task in query:
                writer.writerow([task.subject.title, task.title, task.start_time_string, task.end_time_string])
        finally:
            if csv_file and csv_file != sys.stdout:
                csv_file.close()