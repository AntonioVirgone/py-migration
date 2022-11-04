from service.migration_service import MigrationService

filename = "excel/card2_2022_2023.xlsx"

print("-------- Create migration files from '{}' --------".format(filename))
MigrationService.create(filename=filename, cardVersion="00002", migrationVersion="V1.14.")
