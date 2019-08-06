import csv


class FileHandler:
    def create_users_file(self, users_list, *headers):
        head = [item for item in headers]
        try:
            with open('system_users.csv','w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=head)
                writer.writeheader()
                for roles, users in users_list.items():
                    writer.writerow(users)
                print
        except IOError:
            print('An input/output error occurred')

    def add_to_file(self):
        pass

    def override_file(self):
        pass

    def read_file(self):
        pass
