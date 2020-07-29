class DetectMail:
    def __init__(self, file):
        self._file_path_ = file

    def list_file(self):
        with open(self._file_path_) as FILE:
            list_mail = FILE.readlines()
            return list_mail

    @staticmethod
    def separate_email(all_mail):
        gmail_list = list(filter(lambda x: "gmail.com" in x, all_mail))
        for element in gmail_list:
            all_mail.remove(element)
        return gmail_list, all_mail

    @staticmethod
    def mail_filter(gmails):

        for gmail_element in gmails:
            new_element = str(gmail_element.replace(".", ""))
            tmp = new_element.replace("gmailcom", "gmail.com")
            yield tmp

    @staticmethod
    def remove_duplicate(old_non_gmail, old_gmail):
        new_non_gmail = list(dict.fromkeys(old_non_gmail))
        new_gmail = list(dict.fromkeys(old_gmail))
        return new_non_gmail, new_gmail

    @staticmethod
    def return_output(all_mails, all_gmails):
        mails = all_mails + all_gmails

        for mail_element in mails:
            for j, letters in enumerate(mail_element):
                if letters == "@":
                    break
            username = mail_element[:j]
            domain = mail_element[j + 1 :]
            print(f"username : '{username}' \n domain : '{domain}")
            print("*=================*")


file_input = input("enter the address of file:")
my_obj = DetectMail(file_input)
list_all_mail = my_obj.list_file()
gmail_elements, non_gmail_mail = my_obj.separate_email(list_all_mail)
filtered_mail = list(my_obj.mail_filter(gmail_elements))
new_not_gmail, new_gmail = my_obj.remove_duplicate(non_gmail_mail, filtered_mail)
print(new_gmail)
print()
print(new_not_gmail)
my_obj.return_output(new_not_gmail, new_gmail)
