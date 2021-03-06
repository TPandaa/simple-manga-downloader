class BaseManga:
    """The base class for the manga modules
    directory = manga dowload directory, has to be changed into a actual
    path before downloading
    check_only if True will cause all of the manga modules to not ask for
    user input
    """
    directory = None
    check_only = False

    @property
    def manga_dir(self):
        return self.directory / self.series_title

    def __bool__(self):
        return True

    def __len__(self):
        return len(self.chapters)
