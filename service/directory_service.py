import os


class DirService:

    @staticmethod
    def create(dirName):
        # Parent Directory path
        parent_dir = "./"

        # Path
        path = os.path.join(parent_dir, dirName)

        isExist = os.path.exists(path)
        print("directory '/{}' exist: {}".format(dirName, isExist))

        if not isExist:
            os.mkdir(path)
            print("Directory '% s' created" % dirName)

        return path
