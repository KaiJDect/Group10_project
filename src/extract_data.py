import zipfile
import os

REPO_NAME = "Group10_project"

def getProjectRoot():
    currentPath = os.getcwd()
    projectRoot = currentPath.split(REPO_NAME)[0] + REPO_NAME +"\\"

    return projectRoot

def extractFile(zipFilePath, destFilePath):
    projectRoot = getProjectRoot()
    dataPath = projectRoot + "data\\"

    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if not file_info.is_dir():
                with zip_ref.open(file_info) as source_file:
                    file_name = os.path.basename(file_info.filename)
                    destination_path = os.path.join(destFilePath, file_name)
                    with open(destination_path, 'wb') as dest_file:
                        dest_file.write(source_file.read())

def combineFiles(file1, file2):
    projectRoot = getProjectRoot()
    output_file = projectRoot + "data\\NSW\\forecastdemand_nsw.csv.zip"

    with open(output_file, 'wb') as outfile:
        for file in [file1, file2]:
            with open(file, 'rb') as infile:
                outfile.write(infile.read())

def main():
    projectRoot = getProjectRoot()
    extractFile(projectRoot + "data\\Australia\\a.zip", projectRoot + "extracted_data\\")
    extractFile(projectRoot + "data\\Australia\\b.zip", projectRoot + "extracted_data\\")
    extractFile(projectRoot + "data\\Australia\\c.zip", projectRoot + "extracted_data\\")
    extractFile(projectRoot + "data\\Australia\\d.zip", projectRoot + "extracted_data\\")

    combineFiles(projectRoot + "data\\NSW\\forecastdemand_nsw.csv.zip.partaa", projectRoot + "data\\NSW\\forecastdemand_nsw.csv.zip.partab")

    extractFile(projectRoot + "data\\NSW\\temperature_nsw.csv.zip", projectRoot + "extracted_data\\")
    extractFile(projectRoot + "data\\NSW\\forecastdemand_nsw.csv.zip", projectRoot + "extracted_data\\")
    extractFile(projectRoot + "data\\NSW\\totaldemand_nsw.csv.zip", projectRoot + "extracted_data\\")

if __name__=="__main__":
    main()