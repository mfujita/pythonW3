// See https://aka.ms/new-console-template for more information
using Backup2025;

//Console.WriteLine("Backup 2025");

List<string> directoryToBackup = new List<string>()
{
    //"C:\\estudos",
    "C:\\faculdades"
};

List<string> excludedDirectories = new List<string>()
{
    ".vs",
    "FileContentIndex",
    "packages"
};

MyBackup myBackup = new MyBackup(directoryToBackup);
myBackup.ListingEachDirectory();
myBackup.CreatePathExternalHd();
myBackup.CreateDirectoriesExternalHd();
Console.WriteLine();
myBackup.ListingEachDirectoryToGetFiles();
myBackup.DoBackup();
