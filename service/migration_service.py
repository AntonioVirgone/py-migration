import datetime

from service.directory_service import DirService
from service.excel_service import ExcelService
from service.split_array_service import SplitArrayService


class MigrationService:

    @staticmethod
    def create(filename, cardVersion, migrationVersion):
        cardList = ExcelService.convertXslxToList(filename=filename, cardVersion=cardVersion)

        cardListSplit = SplitArrayService.split(cardList, (len(cardList) // 5000) + 1)

        dirPath = DirService.create("migration_{0}".format(str(datetime.date.today())))

        listIndex = 0

        for list in cardListSplit:
            fileName = "{0}/{1}{2}__add_card.sql".format(dirPath, migrationVersion, listIndex)

            with open(fileName, 'w') as f:
                f.write(
                    "INSERT INTO card (id, card_code, chip_code, revision, version, insert_datetime, update_datetime) VALUES ")
                for card in list:
                    f.write("(gen_random_uuid(), '{0}', '{1}', '{2}', 1, now(), now()),".format(
                        str(card.code).replace("-", ""),
                        card.cip,
                        card.revision))

            listIndex = listIndex + 1
